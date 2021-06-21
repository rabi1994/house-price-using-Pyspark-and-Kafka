# house-price-using-Pyspark-and-Kafka
## house pricing using Pyspark and Kafka
## environment : Linux
### recommendation : run preprocessing file first to see how the data work , all the lines in big_data.ipynb explained nut if you have any question feel free to ask
### activation of pyspark :
#### 1)open terminal 
#### 2)write Pypark
#### 3) open file big_data.ipynb
#### 4) run all cells by order 
### activation of Kafka:
#### 1)open terminal 
#### 2) run the following code by order: 
##### 	pip install kafka-python
#####   alias cdk='cd /usr/local/kafka/kafka'
#####   cdk
#####   bin/zookeeper-server-start.sh    config/zookeeper.properties &
#####   bin/kafka-server-start.sh        config/server.properties &
#####   bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic sales
#####   python producer1.py &
#####   python producer2.py &
### all the files is here :) 
### for any question or idea feel free to ask :)

