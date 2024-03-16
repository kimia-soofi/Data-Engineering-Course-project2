from kafka import KafkaConsumer, KafkaProducer
import json
from datetime import datetime
print("Connecting to consumer ...")
# Set up Kafka consumer
consumer = KafkaConsumer('users-info', bootstrap_servers='localhost:9092', auto_offset_reset='earliest',enable_auto_commit=True, group_id='my-group1')

# Set up Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for message in consumer:
    data = json.loads(message.value.decode('utf-8'))
    data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(data)
    producer.send('users-info-with-timestamp', json.dumps(data).encode('utf-8'))
