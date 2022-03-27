import os
from config import db #Line 2 imports the db instance from the config.py module.
from models import Car

# Data to initialize database with
CAR = [
    {'carid': 1, 
    'region': 'NY',
    'price': 3000,
    'year': '2014',
    'manufacturer': 'Farrell',
    'model': 'Farrell4',
    'condition': 'good',
    'fuel': 'gas',
    'transmission': 'manual',
    'posting_date': '2010/05/05'
    },

    {'carid': 2, 
    'region': 'UK',
    'price': 3001,
    'year': '2012',
    'manufacturer': 'Farrell',
    'model': 'Farrell4',
    'condition': 'good',
    'fuel': 'gas',
    'transmission': 'manual',
    'posting_date': '2010/05/05'},

    {'carid': 3, 
    'region': 'NY',
    'price': 3302,
    'year': '2016',
    'manufacturer': 'Farrell',
    'model': 'Farrell4',
    'condition': 'good',
    'fuel': 'gas',
    'transmission': 'automatoc',
    'posting_date': '02/04/2010'}
]

#CARPOST = [
#    {'CarPostid':20,
#    'carId':2,
#    'postDate':'2020/07/05'},

#   {'CarPostid':21,
#    'carId':1,
#    'postDate':'2020/07/05'},

#    {'CarPostid':22,
#    'carId':3,
#    'postDate':'2020/07/05'}
#]

# Delete database file if it exists currently
if os.path.exists('car.db'):
    os.remove('car.db')

# Create the database
db.create_all()

# Iterate over the Car structure and populate the database
for car in CAR:
    p = Car(carid=car['carid'], 
    region=car['region'],
    price=car['price'],year=car['year'],manufacturer=car['manufacturer'],
    model=car['model'],condition=car['condition'],fuel=car['fuel'],transmission=car['transmission'],
    posting_date=car['posting_date'])


    db.session.add(p) #commits Car object to db
    db.session.commit()



