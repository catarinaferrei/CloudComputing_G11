from concurrent import futures
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from user_pb2 import (
    UserRequest,
    UserPreferences,
    UserPreferencesResponse,
)
import user_pb2_grpc

from config import Session,User_Preferences

session = Session()

def get_user_preferences(id):
  user_preferences = session.query(User_Preferences).filter_by(user_id=id).first()
  if user_preferences is not None:
      return user_preferences 

class UserService(user_pb2_grpc.UsersServicer):
    def Preferences(self, request, context):
      user_preferences = get_user_preferences(request.user_id) 
      if user_preferences is None:
        raise NotFound("User not found")

      userpref = UserPreferences(
        id = user_preferences.preferences_id,
        color = user_preferences.color,
        fuel = user_preferences.fuel,
        transmission = user_preferences.transmission,
        manufacturer = user_preferences.manufacturer,
        year = user_preferences.year,
        max_price = user_preferences.max_price)

      return UserPreferencesResponse(preferences=userpref)

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    user_pb2_grpc.add_UsersServicer_to_server(
        UserService(), server
    )

    server.add_insecure_port("[::]:5001")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
  serve()