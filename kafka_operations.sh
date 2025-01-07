#!/bin/bash

create_topic() {
  kubectl exec -it sray-cp-kafka-0 -n sray -- /bin/bash -c '/bin/kafka-topics.sh --create --topic my_test_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 --if-not-exists'
  if [ $? -ne 0 ]; then
    echo "Error creating topic. Exiting..."
    exit 1
  fi
}

produce_messages() {
  for i in $(seq 1 10); do
    kubectl exec -it sray-cp-kafka-0 -n sray -- /bin/bash -c "echo \"Message $i\" | /bin/kafka-console-producer.sh --broker-list localhost:9092 --topic my_test_topic"
  done
}

consume_messages() {
  kubectl exec -it sray-cp-kafka-0 -n sray -- /bin/bash -c '/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic my_test_topic --group my_consumer_group --from-beginning --timeout-ms 1000'
}

get_coordinator() {
  COORDINATOR=$(kubectl exec -it sray-cp-kafka-0 -n sray -- /bin/bash -c '/bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my_consumer_group | grep -oP "Coordinator:\s+\K\S+"')
  if [ -z "$COORDINATOR" ]; then
    echo "Error: Unable to determine Kafka coordinator."
    exit 1
  else
    echo "The Kafka coordinator for consumer group my_consumer_group is: $COORDINATOR"
  fi
}

main() {
  create_topic
  produce_messages
  consume_messages
  get_coordinator
}

main
