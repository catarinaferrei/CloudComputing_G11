from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from user_pb2 import (
    UserRequest,
    UserPreferences,
    UserPreferencesResponse,
)
import user_pb2_grpc
from models import Users,UserPreferences
from config import db,app

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
  user = Users.query.get(id)
  del user.__dict__['_sa_instance_state']
  return jsonify(user.__dict__)

@app.route('/users', methods=['GET'])
def get_users():
  users = []
  for user in db.session.query(Users).all():
    del user.__dict__['_sa_instance_state']
    users.append(user.__dict__)
  return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
  body = request.get_json()
  existingUser = db.session.query(UserPreferences).filter_by(email=body['email']).one_or_none()

  if existingUser is None:
    db.session.add(createUser(body))
    session.flush()

    userPreferences = createUserPreferences(user_id,body)

    db.session.add(userPreferences)
    db.session.commit()    
    return "user created"
  else:
    abort(409, f'User already exists')

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
  body = request.get_json()

  existingUser = db.session.query(UserPreferences).filter_by(user_id=id).one_or_none()

  if existingUser is not None:
    db.session.query(Users).filter_by(id=id).update(
    dict(createUser(body)))
    db.session.query(UserPreferences).filter_by(user_id=id).update(
    dict(createUserPreferences(body)))
    db.session.commit()
    return "user updated"
  else:
    abort(409, f'User doesnt exist')
   

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
  existingUser = db.session.query(UserPreferences).filter_by(user_id=body[id]).one_or_none()

  if existingUser is not None:
    db.session.query(UserPreferences).filter_by(user_id=id).delete()
    db.session.query(Users).filter_by(id=id).delete()
    db.session.commit()
    return "user deleted"
  else: 
    abort(409, f'User doesnt exist')

def get_user_preferences(id):
  user_preferences = db.session.query(UserPreferences).filter_by(user_id=id).first()
  if user_preferences is not None:
    del user_preferences.__dict__['_sa_instance_state']
    return jsonify(user_preferences.__dict__)
  else:
    abort(409, f'User preferences dont exist')


def createUser(body):
  name = body['name']
  email = body['email']
  password = body['password']
        
  return Users(name,email,password)

def createUserPreferences(user_id,body):
  color = body['Preferences.color']
  transmission = body['Preferences.transmission']
  max_price = body['Preferences.max_price']
  year = body['Preferences.year']
  manufacturer = body['Preferences.manufacturer']
        
  return UserPreferences(user_id,color,transmission,max_price,year,manufacturer)

class UserService(user_pb2_grpc.UsersServicer):
    def Preferences(self, request, context):
      user_preferences = get_user_preferences(request.user_id) 
      if user_preferences is None:
        raise NotFound("User not found")

      return UserPreferencesResponse(preferences=user_preferences)

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    user_pb2_grpc.add_UsersServicer_to_server(
        UserService(), server
    )

    server.add_insecure_port("[::]:50055")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
  app.run()
  serve()