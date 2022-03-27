from multiprocessing.dummy import Condition
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from config import db
""" The models.py module is created to provide the Car and CarSchema classes 
creates the tables for the database"""

# This class defines movies
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


# This class defines list of Titles that a movie have
#class CarPost(db.Model):
#    __tablename__ = "carpost"
#    CarPostid = db.Column(db.Integer, primary_key=True)
#    carId = db.Column(db.Integer,  db.ForeignKey('car.carid'))
#    postDate = db.Column(db.DateTime)
#    postName = db.Column(db.String)
#    def __init__(self,car_post_id,car_id,post_date,post_name):
#        self.car_post_id = car_post_id
#        self.car_id = car_id
#        self.post_date = post_date
#        self.post_name = post_name

class CarSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Car #serialize this class
        #include_relationships = True #problem
        load_instance = True
        sqla_session = db.session
        # exclude = ("tconst",)
    # ver se essse default "" nao explode


#class CarPostSchema(SQLAlchemyAutoSchema):
    """ This class exists to get around a recursion issue
    """
#    car_post_id = fields.Int()
#    carid = fields.Int()
#    post_date = fields.Date()
#    post_name = fields.Str()

#class NoteSchema(SQLAlchemyAutoSchema):
#    class Meta:
#        model = CarPost
#        sqla_session = db.session
#    person = fields.Nested('CarPostSchema', default=None)

#class NotePersonSchema(SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """
#    person_id = fields.Int()
#    lname = fields.Str()
#    fname = fields.Str()
#    timestamp = fields.Str()
    
 
