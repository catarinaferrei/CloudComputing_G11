from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Users(db.Model):
  user_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=False, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)  
  password = db.Column(db.String(120), unique=True, nullable=False)


def __init__(self, title, content):
    self.title = title
    self.content = content 

@app.route('/users/<id>', methods=['GET'])
def get_item(id):
  item = Users.query.get(id)
  del item.__dict__['_sa_instance_state']
  return jsonify(item.__dict__)

@app.route('/users', methods=['GET'])
def get_items():
  items = []
  for item in db.session.query(Users).all():
    del item.__dict__['_sa_instance_state']
    items.append(item.__dict__)
  return jsonify(items)

@app.route('/users', methods=['POST'])
def create_item():
  body = request.get_json()
  db.session.add(Users(body['title'], body['content']))
  db.session.commit()
  return "user created"

@app.route('/users/<id>', methods=['PUT'])
def update_item(id):
  body = request.get_json()
  db.session.query(Users).filter_by(id=id).update(
    dict(title=body['title'], content=body['content']))
  db.session.commit()
  return "user updated"

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
  db.session.query(Users).filter_by(id=id).delete()
  db.session.commit()
  return "user deleted"
