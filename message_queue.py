from kafka import KafkaProducer
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_message(data):
    producer.send('data_topic', json.dumps(data).encode('utf-8'))
