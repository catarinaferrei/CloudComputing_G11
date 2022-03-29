FROM python

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5001
ENTRYPOINT ["python", "user_grpc.py"]