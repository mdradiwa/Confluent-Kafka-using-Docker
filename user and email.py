from time import sleep
from json import dumps
from kafka import KafkaProducer
import requests
import csv

topic_name='students'
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))

url = 'https://dummyjson.com/users'
# request data
response = requests.get(url)
# read and parse the data using json()
res = response.json()
users = res["users"]
data = []

for user in users:
    data.append({'user_name':user['firstName'],
           'age':user['age'],
           'gender': user['gender'],
           'email': user['email']
           })
    print(data)
    producer.send(topic_name, value=data)
    sleep(5)

field_names = ['user_name', 'age', 'gender', 'email']
    
with open('Users.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(data)