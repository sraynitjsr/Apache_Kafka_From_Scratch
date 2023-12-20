from confluent_kafka import Consumer, KafkaError

bootstrap_servers = 'localhost:9092'
kafka_topic = 'my_kafka_topic'
group_id = 'python-consumer-group'

consumer_config = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(consumer_config)
consumer.subscribe([kafka_topic])

try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(f"Error: {msg.error()}")
                break

        print(f"Received message: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
