from kafka import KafkaConsumer, KafkaProducer
import json
import random
import time
print("Connecting to consumer ...")

consumer2 = KafkaConsumer('users-info-with-timestamp', auto_offset_reset='earliest',enable_auto_commit=True, bootstrap_servers=['localhost:9092'])
producer2 = KafkaProducer(bootstrap_servers=['localhost:9092'])
for message in consumer2:
    
    data = json.loads(message.value.decode('utf-8'))
    data['label'] = random.choice(['A', 'B', 'C'])
    print(data)
    producer2.send('users-info-labeled', json.dumps(data).encode('utf-8'))





