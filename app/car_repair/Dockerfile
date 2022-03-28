FROM python

RUN mkdir /car_repair
WORKDIR /car_repair

COPY car_repair/requirements.txt /car_repair
RUN pip install -r requirements.txt

RUN mkdir /car_repair/protobufs
COPY protobufs/car_repair_service.proto /car_repair/protobufs

RUN python -m grpc_tools.protoc -I protobufs --python_out=/car_repair \
           --grpc_python_out=/car_repair protobufs/car_repair_service.proto

COPY car_repair/app /car_repair

RUN ls .

EXPOSE 5005
ENTRYPOINT [ "python", "car_repair_service.py" ]