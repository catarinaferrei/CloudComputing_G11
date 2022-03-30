FROM python:3.7
WORKDIR /app
COPY . /app
RUN python3 -m pip install -r requirements.txt
ENTRYPOINT ["cars.py"]
CMD [ "python3" ]

