#!/bin/bash

bin/kafka-topics.sh --create --zookeeper $ZookeeperConnectString --replication-factor 3 --partitions 1 --topic $topic
