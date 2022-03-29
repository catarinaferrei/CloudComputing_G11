from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker,declarative_base
import os

Base = declarative_base()

engine = create_engine(url=os.environ.get('DATABASE_URL'))

Session = sessionmaker()
Session.configure(bind=engine)

class User_Preferences(Base):
    __tablename__ = 'user_preferences'
    preferences_id = Column(Integer, primary_key=True)
    user_id = Column(Integer,unique=True,nullable=False)
    color = Column(String(80), unique=False, nullable=True)
    fuel = Column(String(120), unique=False, nullable=True)  
    transmission = Column(String(120), unique=False, nullable=True)
    max_price = Column(Integer, unique=False, nullable=True)
    year = Column(Integer, unique=False, nullable=True)
    manufacturer = Column(String(120), unique=False, nullable=True)

    def __init__(self, user_id,color,transmission,max_price,year,manufacturer,fuel):
        self.user_id = user_id
        self.color = color  
        self.transmission = transmission
        self.max_price = max_price
        self.year = year
        self.manufacturer = manufacturer
        self.fuel = fuel