from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os

import sys

sys.path.insert(0,'../')

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
  existingUser = db.session.query(Users).filter_by(email=body['email']).one_or_none()

  if existingUser is None:
    user = createUser(body)
    db.session.add(user)
    db.session.flush()

    userPreferences = createUserPreferences(user.user_id,body)

    db.session.add(userPreferences)
    db.session.commit()    
    return "user created"
  else:
    abort(409, f'User already exists')

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
  body = request.get_json()

  existingUser = db.session.query(Users).filter_by(user_id=id).one_or_none()

  if existingUser is not None:
    db.session.query(Users).filter_by(id=id).update(dict(createUser(body)))
    db.session.query(UserPreferences).filter_by(user_id=id).update(dict(createUserPreferences(body)))
    db.session.commit()
    return "user updated"
  else:
    abort(409, f'User doesnt exist')
   

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
  existingUser = db.session.query(Users).filter_by(user_id=body[id]).one_or_none()

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
  color = body['Preferences']['color']
  transmission = body['Preferences']['transmission']
  max_price = body['Preferences']['max_price']
  year = body['Preferences']['year']
  manufacturer = body['Preferences']['manufacturer']
  fuel = body['Preferences']['fuel']
        
  return UserPreferences(user_id,color,transmission,max_price,year,manufacturer,fuel)

if __name__ == "__main__":
  app.run()