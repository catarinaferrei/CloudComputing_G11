from cars import  app
from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app) #--> here 
 
#app = Flask(__name__)
"""Module that contains the database for the ms.car and API calls to the web server
"""
class Car(db.Model):
    __tablename__ = "car"
    carid = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(100))
    price = db.Column(db.Integer) 
    year = db.Column(db.String(4))  # YYYY eg 1990
    manufacturer = db.Column(db.String(100))
    model = db.Column(db.String(100))
    condition = db.Column(db.String(100))
    fuel = db.Column(db.String(100))
    transmission = db.Column(db.String(100))
    posting_date = db.Column(db.String(100))
    
    
    def __init__(self, carid,region,price,year,manufacturer,model,condition,fuel,transmission,posting_date):
        self.carid = carid
        self.region = region
        self.price = price
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.condition = condition
        self.fuel = fuel
        self.transmission = transmission
        self.posting_date = posting_date



@app.route('/cars/<id>', methods=['GET'])
def get_car(id):
  user = Car.query.get(id)
  del user.__dict__['_sa_instance_state']
  return jsonify(user.__dict__)

@app.route('/cars', methods=['GET'])
def get_cars():
  cars = []
  for car in db.session.query(Car).all():
    del car.__dict__['_sa_instance_state']
    cars.append(car.__dict__)
  return jsonify(cars)

@app.route('/cars', methods=['POST'])
def create_car():
  body = request.get_json()
  db.session.add(Car(body['title'], body['content']))
  db.session.commit()
  return "car created"

@app.route('/cars/<id>', methods=['DELETE'])
def delete_car(id):
  db.session.query(Car).filter_by(id=id).delete()
  db.session.commit()
  return "car deleted"

@app.route('/cars/filtered',defaults={'region':None,'price':None,'year':None,'manufacturer':None,'model':None,'condition':None})
def read_filtered(region, price, year,manufacturer, model, condition):
  """
    This function responds to a request for cars/filtered?region=&&price=&&year=&&manufacturer=&&model=&&condition

    :param:         search filters (region, price, year,manufacturer, model and condition)
    :return:        CarList
    """

  query = db.session.query(Car) 
  car =  []
  if request.args.get('region'): 
     query = query.filter(Car.region == request.args.get('region'))
  if price:
            query = query.filter(Car.price==price)
  if year:
            query = query.filter(Car.year == year)
  if manufacturer:
            query = query.filter(Car.manufacturer==manufacturer)
  if model:
            query = query.filter(Car.model == model) 
  if condition:
            query = query.filter(Car.condition==condition)

  #carList = query.limit(30).all()
  for data in query.limit(30).all():
    del data.__dict__['_sa_instance_state']
    car.append(data.__dict__)
  return jsonify(car)
  



