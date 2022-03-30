FROM python:3.7
WORKDIR /cars

COPY . /cars
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "cars.py"]
