FROM python:3.6-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

#WORKDIR /service/recommendations
#RUN pip install -r requirements.txt
#RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
#           --grpc_python_out=. ../protobufs/cars.proto
#RUN openssl req -nodes -newkey rsa:4096 -subj /CN=recommendations \
#                -keyout client.key -out client.csr
#RUN --mount=type=secret,id=ca.key \
#    openssl x509 -req -in client.csr -CA ca.pem -CAkey /run/secrets/ca.key \
#                 -set_serial 1 -out client.pem

ENV FLASK_APP=recommendations.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=90"]