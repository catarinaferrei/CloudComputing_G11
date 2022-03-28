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

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Users(db.Model):
  user_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=False, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)  
  password = db.Column(db.String(120), unique=True, nullable=False)

class UserPreferences(db.Model):
  preferences_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer,unique=True,nullable=False)
  color = db.Column(db.String(80), unique=False, nullable=True)
  fuel = db.Column(db.String(120), unique=False, nullable=True)  
  transmission = db.Column(db.String(120), unique=False, nullable=True)
  max_price = db.Column(db.Integer, unique=False, nullable=True)
  year = db.Column(db.Integer, unique=False, nullable=True)
  manufacturer = db.Column(db.String(120), unique=False, nullable=True)

def __init__(self, title, content):
    self.title = title
    self.content = content 

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
  db.session.add(Users(body['title'], body['content']))
  db.session.commit()
  return "user created"

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
  body = request.get_json()
  db.session.query(Users).filter_by(id=id).update(
    dict(title=body['title'], content=body['content']))
  db.session.commit()
  return "user updated"

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
  db.session.query(Users).filter_by(id=id).delete()
  db.session.commit()
  return "user deleted"

def get_user_preferences(id):
  user_preferences = db.session.query(UserPreferences).filter_by(user_id=id).first()
  del user_preferences.__dict__['_sa_instance_state']
  return jsonify(user_preferences.__dict__)

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
  app.run(debug=True)
  serve()