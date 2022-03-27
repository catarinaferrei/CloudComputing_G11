import sys
from flask import abort, make_response
from config import db, app
from models import Car, CarPost, CarPostSchema

def read_all():
    """
    This function responds to a request for /api/car/carpost
    with the complete list of posts
    :return:                json list of all posts for all cars
    """
    # Query the database for all the notes
    carposts = CarPost.query.all()

    # Serialize the list of notes from our data
    car_post_schema = CarPostSchema(many=True, exclude=["person.notes"]) #ver o q excludes
    data = car_post_schema.dump(carposts).data
    return data

def create(car_id, carpost):
    """
    This function creates a new carpost related to the passed in car_id.
    :param car_id:       Id of the car in which the post is related to
    :param carpost:            The JSON containing the post data
    :return:                201 on success
    """
    # get the parent person
    car = Car.query.filter(Car.carid == car_id).one_or_none()

    # Was a person found?
    if car is None:
        abort(404, f"Car not found for Id: {car_id}")

    # Create a note schema instance
    schema = CarPostSchema()
    new_carpost = schema.load(carpost, session=db.session).data

    # Add the carpost to the car and database
    car.carpost.append(new_carpost)
    db.session.commit()

    # Serialize and return the newly created note in the response
    data = schema.dump(new_carpost).data

    return data, 201

def read_one(car_id, car_post_id):
    """
    This function responds to a request for
    /cars/{id}/carposting/{carpostid}
    with one matching post for the associated car

    :param car_id:          Id of car the post is related to
    :param car_post_id:         Id of the post
    :return:                json string of post contents
    """
    # Query the database for the note
    carpost = (
        CarPost.query.join(Car, Car.car_id == CarPost.car_post_id)
        .filter(Car.car_id == car_id)
        .filter(CarPost.car_post_id== car_post_id)
        .one_or_none()
    )

    if carpost is not None: # serialize the data that is retrieved from db into json to be consumed by the API
        carpost_schema = CarPostSchema()
        data = carpost_schema.dump(carpost).data
        return data

    # Otherwise, nope, didn't find that note
    else:
        abort(404, f"Carpost not found for Id: {car_post_id}")

def delete_one(car_id, car_post_id):
    """
    This function responds to a delete for
    /cars/{id}/carposting/{carpostid}
    with one matching post for the associated car

    :param car_id:          Id of car the post is related to
    :param car_post_id:         Id of the post
    :return:            200 on successful delete, 404 if not found
    """
    # Query the database for the post
    carpost = (
        CarPost.query.join(Car, Car.car_id == CarPost.car_post_id)
        .filter(Car.car_id == car_id)
        .filter(CarPost.car_post_id== car_post_id)
        .one_or_none()
    )

    if carpost is not None:
        db.session.delete(carpost)
        db.session.commit()
        return make_response(
            "Car {car_post_id} deleted".format(car_post_id=car_post_id), 200
        )

    # Otherwise, nope, didn't find that movie
    else:
        abort(
            404,
            "post not found for Id: {car_post_id}".format(car_post_id=car_post_id),)
    