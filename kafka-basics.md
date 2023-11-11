### Apache Kafka is a distributed streaming platform that is designed to handle real-time data streams at scale.

### It is commonly used for building real-time data pipelines and event-driven applications.

#### 1. Understanding the Core Concepts:

###### Before diving into the setup, it's important to understand some core concepts as mentioned below :-
######## Topics: Kafka organizes data into topics, which are logical channels for data streams.
######## Producers: Producers are responsible for publishing data to Kafka topics.
######## Brokers: Kafka brokers are the servers that store and manage the data.
######## Consumers: Consumers read and process data from Kafka topics.
######## Partitions: Kafka topics can be divided into partitions, which enable parallelism and distribution of data.

#### 2. Installation => Follow Office Apache Doc Based on OS Type, Linux Preferred

#### 3. Starting Zookeeper:

###### Kafka relies on Apache ZooKeeper for distributed coordination. Start a ZooKeeper server by running the command -> bin/zookeeper-server-start.sh config/zookeeper.properties

#### 4. Starting Kafka Brokers:

###### Start Kafka brokers using the command -> bin/kafka-server-start.sh config/server.properties
######## Note => This starts a single Kafka broker. In a production environment, you would typically have multiple brokers for fault tolerance and scalability.

#### 5. Creating a Kafka Topic:

###### We can create a Kafka topic using the kafka-topics.sh script => bin/kafka-topics.sh --create --topic my-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
###### This command creates a topic named "my-topic" with one partition and one replication factor.

#### 6. Producing Data:

###### We can use the Kafka console producer to publish data to the topic => bin/kafka-console-producer.sh --topic my-topic --bootstrap-server localhost:9092
###### We can now type messages, and they will be published to the "my-topic" topic.
