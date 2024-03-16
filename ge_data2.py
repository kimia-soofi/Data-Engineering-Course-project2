import uuid
import json
import time
import logging
import requests
from datetime import datetime
from kafka import KafkaProducer

def get_data():
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    return res

def format_data(res):
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{location['street']['number']} {location['street']['name']}, {location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']
    # Additional data fields
    data['nationality'] = res['nat']
    data['cell'] = res['cell']
    data['age'] = res['dob']['age']
    return data

def stream_data():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], max_block_ms=5000)

    curr_time = time.time()
    while True:
        if time.time() > curr_time + 60: #1 minute
            break
        try:
            res = get_data()
            res = format_data(res)
            print(f"Sending data : {res}")

            producer.send('users-info', json.dumps(res).encode('utf-8'))


            print('done')
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            continue

if __name__ == "__main__":
    stream_data()
