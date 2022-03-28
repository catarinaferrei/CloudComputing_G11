from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from models import Users,UserPreferences
from config import db,app


def signin(email,password):
    user = db.session.query(Users).filter_by(email=body['email']).first()

    if user is not None:
        if user.password == password:
            return generateJWTToken(user)
    else:
        abort(409, f'Email or password are invalid.')

def generateJWTToken(user):
