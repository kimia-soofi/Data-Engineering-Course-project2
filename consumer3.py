import psycopg2
from kafka import KafkaConsumer
import json

conn =psycopg2.connect(
    dbname='dblab',
    user='postgres',
    password='postgres123',
    host='localhost',
    port='5434'
)
cur = conn.cursor()

consumer3 = KafkaConsumer('users-info-labeled', auto_offset_reset='earliest',enable_auto_commit=True,bootstrap_servers=['localhost:9092'])

start_time = time.time()
for message in consumer3:
    # Check if 5 seconds have passed
    if time.time() - start_time >= 5:
        break

    data = json.loads(message.value.decode('utf-8'))
    print(data)
    sql = """
        INSERT INTO enriched_data (
            id, first_name, last_name, gender, address, post_code,
            email, username, dob, registered_date, phone, picture,
            nationality, cell, age, timestamp, label
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
    """
    values = (
        data['id'], data['first_name'], data['last_name'], data['gender'],
        data['address'], data['post_code'], data['email'], data['username'],
        data['dob'], data['registered_date'], data['phone'], data['picture'],
        data['nationality'], data['cell'], data['age'], data['timestamp'],
        data['label']
    )
    cur.execute(sql, values)
    conn.commit()

# Close database connection
cur.close()
conn.close()