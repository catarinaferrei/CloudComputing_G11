from car_repair_service_pb2 import AddRequest
from car_repair_service_pb2_grpc import CarRepairServiceStub
import grpc

repair_service_channel = grpc.insecure_channel("localhost:5001")

service = CarRepairServiceStub( repair_service_channel )

request = AddRequest(
    car_id=1
)
response = service.Add(request, None)
print(response.car_id)
