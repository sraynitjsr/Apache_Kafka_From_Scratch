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

