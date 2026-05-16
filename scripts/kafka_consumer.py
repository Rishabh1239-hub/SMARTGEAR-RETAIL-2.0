from kafka import KafkaConsumer
import json

print("Starting Consumer...")

consumer = KafkaConsumer(
    'smartgear_sales',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=None,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Connected to Kafka.")
print("Listening to Kafka topic...")

for message in consumer:
    print("Received:", message.value)