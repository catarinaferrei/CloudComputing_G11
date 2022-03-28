FROM python

RUN mkdir /repair_service
WORKDIR /repair_service

COPY requirements.txt /repair_service
RUN pip install -r requirements.txt

RUN mkdir /repair_service/protobufs
COPY ../protobufs/car_repair_service.proto /repair_service/protobufs

RUN python -m grpc_tools.protoc -I ./protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/car_repair_service.proto
            -set_serial 1 -out server.pem

EXPOSE 5005
ENTRYPOINT [ "python", "car_repair_service.py" ]