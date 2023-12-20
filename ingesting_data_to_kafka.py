from confluent_kafka import Producer
import json

bootstrap_servers = 'localhost:9092'

kafka_topic = 'my_kafka_topic'

producer_config = {
    'bootstrap.servers': bootstrap_servers,
    'client.id': 'python-producer'
}

producer = Producer(producer_config)

def produce_message(message):
    try:       
        producer.produce(kafka_topic, key=None, value=json.dumps(message))

        producer.flush()

        print(f"Produced message: {message}")

    except Exception as e:
        print(f"Error producing message: {e}")

sample_data = [
    {'id': 1, 'name': 'John Doe'},
    {'id': 2, 'name': 'Jane Smith'},
]

for data_point in sample_data:
    produce_message(data_point)

producer.close()
