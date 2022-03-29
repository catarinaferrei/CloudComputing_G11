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

import sys
  
sys.path.insert(0, '../flask')

from user import get_user_preferences

class UserService(user_pb2_grpc.UsersServicer):
    def Preferences(self, request, context):
      print('hello')
      user_preferences = get_user_preferences(request.user_id) 
      if user_preferences is None:
        raise NotFound("User not found")

      return UserPreferencesResponse(userpreferences_to_proto(user_preferences))

def userpreferences_to_proto(preferences):
    userpreferences = UserPreferences(
        id = userpreferences.preferences_id,
        region = "usa",
        price = userpreferences.max_price,
        year = userpreferences.year,
        manufacturer = userpreferences.manufacturer,
        model = userpreferences.model,
        condition = "",
        fuel = userpreferences.fuel,
        transmission = userpreferences.transmission,
        posting_date = ""
    )
    
    return userpreferences

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