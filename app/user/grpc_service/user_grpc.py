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

class UserService(user_pb2_grpc.UsersServicer):
    def Preferences(self, request, context):
      print('hello')
      #user_preferences = get_user_preferences(request.user_id) 
      #if user_preferences is None:
      #  raise NotFound("User not found")

      userpref = UserPreferences(id = request.user_id,color = "color",max_price = 10,year = 12,manufacturer ="manufacturer",fuel = "fuel",transmission ="transmission")
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