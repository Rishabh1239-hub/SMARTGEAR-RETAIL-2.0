import pandas as pd
from kafka import KafkaProducer
import json
import time

# Load streaming dataset
df = pd.read_csv("data/streaming_sales.csv")

# ==============================
# CONFLUENT CLOUD CONFIGURATION
# ==============================

BOOTSTRAP_SERVER = "YOUR_BOOTSTRAP_SERVER"
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

TOPIC_NAME = "smartgear_orders"

# ==============================
# KAFKA PRODUCER
# ==============================

producer = KafkaProducer(

    bootstrap_servers="pkc-xrnwx.asia-south2.gcp.confluent.cloud:9092",

    security_protocol="SASL_SSL",

    sasl_mechanism="PLAIN",

    sasl_plain_username="7XHH3PL6L2222QGY",

    sasl_plain_password="cflt9bdQzBtFKjdbkJnaPgb1Upiz2f3JJzlSAx2B1WaPVOwMYJsNILj7H7qRrC1w",

    value_serializer=lambda v: json.dumps(v).encode("utf-8")

)

print("Starting Kafka Producer...")

# ==============================
# STREAM DATA CONTINUOUSLY
# ==============================

for index, row in df.iterrows():

    message = {

        "order_id": int(row["order_id"]),

        "timestamp": str(row["timestamp"]),

        "store_id": int(row["store_id"]),

        "product": str(row["product"]),

        "quantity": int(row["quantity"]),

        "price": float(row["price"]),

        "region": str(row["region"])

    }

    producer.send(TOPIC_NAME, value=message)

    print(f"Sent: {message}")

    time.sleep(2)

producer.flush()

print("Streaming Completed.")