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

