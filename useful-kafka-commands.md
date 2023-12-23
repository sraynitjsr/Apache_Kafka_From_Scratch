### 1. Create a Topic:
#### kafka-topics.sh --create --bootstrap-server <bootstrap_servers> --topic <topic_name> --partitions <num_partitions> --replication-factor <replication_factor>
###### <bootstrap_servers>: Comma-separated list of broker addresses.
###### <topic_name>: Name of the Kafka topic.
###### <num_partitions>: Number of partitions for the topic.
###### <replication_factor>: Replication factor for the topic.

### 2. List Topics:
#### kafka-topics.sh --list --bootstrap-server <bootstrap_servers>
###### Lists all available topics.

### 3. Describe a Topic:
#### kafka-topics.sh --describe --bootstrap-server <bootstrap_servers> --topic <topic_name>
###### Provides information about a specific topic, including partitions, replicas, and configuration.

### 4. Delete a Topic:
#### kafka-topics.sh --delete --bootstrap-server <bootstrap_servers> --topic <topic_name>
###### Deletes the specified topic.

### 5. Produce Messages:
#### kafka-console-producer.sh --broker-list <bootstrap_servers> --topic <topic_name>
###### Allows you to manually produce messages to a topic via the command line.

### 6. Consume Messages:
#### kafka-console-consumer.sh --bootstrap-server <bootstrap_servers> --topic <topic_name> --from-beginning
###### Allows you to consume messages from a topic via the command line.

### 7. Alter Topic Configuration:
#### kafka-configs.sh --bootstrap-server <bootstrap_servers> --entity-type topics --entity-name <topic_name> --alter --add-config <config_key>=<config_value>
###### Modifies the configuration of a topic.

### 8. Alter the Number of Partitions:
#### kafka-topics.sh --alter --bootstrap-server localhost:9092 --topic my_topic --partitions 5
###### This command allows us to change the number of partitions for a topic. 

### 9. Change Replication Factor While Altering:
#### kafka-topics.sh --alter --bootstrap-server localhost:9092 --topic my_topic --partitions 5 --replication-factor 3
###### This example not only changes the number of partitions to 5 but also sets the replication factor to 3.
