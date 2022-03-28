FROM python

RUN mkdir /repair_service
WORKDIR /repair_service

COPY requirements.txt /repair_service
RUN pip install -r requirements.txt

RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/recommendations.proto
            -set_serial 1 -out server.pem

EXPOSE 50051
ENTRYPOINT [ "python", "car_repair_service.py" ]