
FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY recommendations/ /service/recommendations/
COPY ca.pem /service/recommendations/

WORKDIR /service/recommendations
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/user.proto
RUN openssl req -nodes -newkey rsa:4096 -subj /CN=recommendations \
                -keyout client.key -out client.csr
RUN --mount=type=secret,id=ca.key \
    openssl x509 -req -in client.csr -CA ca.pem -CAkey /run/secrets/ca.key \
                 -set_serial 1 -out client.pem

 WORKDIR /service/recommendations
RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/cars.proto
RUN openssl req -nodes -newkey rsa:4096 -subj /CN=recommendations \
                -keyout client.key -out client.csr
RUN --mount=type=secret,id=ca.key \
    openssl x509 -req -in client.csr -CA ca.pem -CAkey /run/secrets/ca.key \
                 -set_serial 1 -out client.pem


EXPOSE 5000
ENV FLASK_APP=recommendations.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]