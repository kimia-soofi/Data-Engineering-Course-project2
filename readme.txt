docker-compose  -f .\docker-compose.yml up -d
------------------------------------------------
wsl:
ap-get update
apt-get install python3
apt-get install python3-pip
pip install requests kafka-python
cronjob:
crontab cronjob
download data with ge_data2.py file
------------------------------------------------
kafka:
docker-compose logs kafka
docker exec -it miniproject-kafka-1 bash
topics:
kafka-topics.sh --create --topic users-info --bootstrap-server localhost:9092 --partitions 4 --replication-factor 1
kafka-topics.sh --create --topic users-info-with-timestamp --bootstrap-server localhost:9092 --partitions 4 --replication-factor 1
kafka-topics.sh --create --topic users-info-labeled --bootstrap-server localhost:9092 --partitions 4 --replication-factor 1
kafka-topics.sh --bootstrap-server localhost:9092 --list
see data of consumer1:
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic users-info --from-beginning
--------------------------------------------------
postgres:
docker exec -it postgres bash
backup:
su postgres
pg_basebackup -D /backup/standalone-"$(date +%Y-%m-%dT%H-%M)" -c fast -P -R 
in postgresql.conf file:
archive_mode = on		# enables archiving; off, on, or always
archive_command = 'test ! -f /archive/%f && cp %p /archive/%f'		# command to use to archive a WAL file
wal_level = replica			# minimal, replica, or logical
now our backup is on
again go to postgres container:
docker exec -it postgres psql -U postgres -d dblab bash
CREATE TABLE enriched_data (
    id VARCHAR(50),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    address VARCHAR(255),
    post_code VARCHAR(20),
    email VARCHAR(100),
    username VARCHAR(50),
    dob TIMESTAMP,
    registered_date TIMESTAMP,
    phone VARCHAR(20),
    picture VARCHAR(255),
    nationality VARCHAR(10),
    cell VARCHAR(20),
    age INTEGER,
    timestamp TIMESTAMP,
    label VARCHAR(10)
);

for see datas:
SELECT * FROM enriched_data;

