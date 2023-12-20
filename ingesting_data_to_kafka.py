from confluent_kafka import Producer
import json

bootstrap_servers = 'localhost:9092'
kafka_topic = 'my_kafka_topic'

producer_config = {
    'bootstrap.servers': bootstrap_servers,
    'client.id': 'python-producer'
}

producer = Producer(producer_config)

def produce_messages(messages):
    try:
        for message in messages:
            producer.produce(kafka_topic, key=None, value=json.dumps(message))
        producer.flush()
        print(f"Produced messages: {messages}")
    except Exception as e:
        print(f"Error producing messages: {e}")

bulk_data = [
    {'id': 1, 'name': 'Schin'},
    {'id': 2, 'name': 'Virat'},
]

batch_size = 3

for i in range(0, len(bulk_data), batch_size):
    batch = bulk_data[i:i + batch_size]
    produce_messages(batch)

producer.close()
