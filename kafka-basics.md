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

#### 7. Consuming Data:

###### Use the Kafka console consumer to read and process data from the topic via => bin/kafka-console-consumer.sh --topic my-topic --bootstrap-server localhost:9092
###### This command will display messages from the "my-topic" topic as they are produced.

#### 8. Building a Kafka Producer and Consumer in Code:

###### To build a Kafka producer and consumer in our choosen programming language of like Java, GoLang or others, we will need to use the Kafka client libraries.

###### These libraries provide APIs to interact with Kafka topics and messages.
