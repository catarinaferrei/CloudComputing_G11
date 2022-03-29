from config import db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)  
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name,email,password):
        self.name = name
        self.email = email  
        self.password = password

class UserPreferences(db.Model):
    preferences_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,unique=True,nullable=False)
    color = db.Column(db.String(80), unique=False, nullable=True)
    fuel = db.Column(db.String(120), unique=False, nullable=True)  
    transmission = db.Column(db.String(120), unique=False, nullable=True)
    max_price = db.Column(db.Integer, unique=False, nullable=True)
    year = db.Column(db.Integer, unique=False, nullable=True)
    manufacturer = db.Column(db.String(120), unique=False, nullable=True)

    def __init__(self, user_id,color,transmission,max_price,year,manufacturer,fuel):
        self.user_id = user_id
        self.color = color  
        self.transmission = transmission
        self.max_price = max_price
        self.year = year
        self.manufacturer = manufacturer
        self.fuel = fuel
