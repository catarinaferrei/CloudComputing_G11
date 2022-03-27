"""
This is the car module and supports all the ReST actions for the
Car collection
"""
import sys

from flask import abort, make_response

from config import db, app
from models import Car,  CarSchema

def create(cars):
    """
    This function creates a new car in the car structure
    based on the passed-in car data
    :return:        201 on success, 406 on Car exists
    """
    car_id = cars.get("carid")
    car_postid = cars.get('postid')
    car_region = cars.get("region")
    car_price= cars.get("price")
    car_year = cars.get("year")
    car_manufacturer = cars.get("manufacturer")
    car_model = cars.get("model")
    car_condition = cars.get("condition") 
    car_fuel = cars.get("fuel") 
    car_posting_date = cars.get("posting_date")

    # title_genre_genre = title_genre
    # 
#        .filter(Movie.genre == title_genre) \
    existing_car = Car.query.filter(Car.carid == car_id) \
        .filter(Car.postid == car_postid) \
        .filter(Car.region == car_region) \
        .filter(Car.price == car_price) \
        .filter(Car.year == car_year) \
        .filter(Car.manufacturer == car_manufacturer) \
        .filter(Car.model == car_model) \
        .filter(Car.condition == car_condition) \
        .filter(Car.fuel == car_fuel) \
        .filter(Car.posting_date == car_posting_date) \
        .one_or_none()

    # Can we insert this movie?
    # Can we insert this person?
    if existing_car is None:

        # Create a person instance using the schema and the passed-in person
        schema = CarSchema()
        new_car = schema.load(cars, session=db.session).data

        # Add the person to the database
        db.session.add(new_car)
        db.session.commit()

        # Serialize and return the newly created person in the response
        return schema.dump(new_car).data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409, f'Car  exists already')



@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete(car_id):
    """
    This function deletes a car from the car structure
    :param car_id:   Id of the car to delete
    :return:            200 on successful delete, 404 if not found
    """
    ## Get the car requested
    cars = Car.query.filter(Car.carid == car_id).one_or_none()
    if cars is not None:
        db.session.delete(cars)
        db.session.commit()
        return make_response(
            "Car {car_id} deleted".format(car_id=car_id), 200
        )

    # Otherwise, nope, didn't find that movie
    else:
        abort(
            404,
            "Car not found for Id: {car_id}".format(car_id=car_id),
        )


def read():
    """
    This function responds to a request for /api/car
    with the complete lists of car
    :return:        json string of list of car
    """
    try:
        cars = Car.query.all()
        # Serialize the data into json format to be consumed by the API
        car_schema = CarSchema(many=True)
        data = car_schema.dump(cars)
        return data
    except:
        db.session.rollback()
        abort(404, "Rollback Error")



def read_one(car_id):
    """
    This function responds to a request for /api/car/{car_id}
    with one matching person from people

    :param car_id:   Id of person to find
    :return:            car matching id
    """
    # Build the initial query
    try:
        cars = Car.query.filter(Car.carid == car_id).one_or_none()
        if cars is not None:
            car_schema = CarSchema()
            return car_schema.dump(cars)

        else:
            abort(404, f"Car not found for Id: {car_id}")
    except:
        db.session.rollback()
        abort(404, "Rollback Error")

def read_filtered(region, price, year,manufacturer, model, condition):
    """
    This function responds to a request for cars/filtered?region=&&price=&&year=&&manufacturer=&&model=&&condition

    :param:         search filters (region, price, year,manufacturer, model and condition)
    :return:        CarList
    """
    query = db.session.query(Car)
    try:
        
        #get the regiom 
        if region: 
            query = query.filter(Car.region == region)
        if price:
            query = query.filter(Car.price==price)
        if year:
            query = query.filter(Car.year == year)
        if manufacturer:
            query = query.filter(Car.manufacturer==manufacturer)
            print('query', query.all())
        if model:
            query = query.filter(Car.model == model) 
        if condition:
            query = query.filter(Car.condition==condition)

        carList = query.limit(30).all()

        if carList is not None:
            # Serialize the data for the response
            car_schema = CarSchema(many=True)
            data = car_schema.dump(carList)
            return data

        else:
            abort(404, f"Car not found for Filters")
    except:
        db.session.rollback()
        abort(404, "Rollback Error")



