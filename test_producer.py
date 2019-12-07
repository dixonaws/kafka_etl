from kafka import KafkaProducer

str_bootstrap_servers="localhost:9092"
producer=KafkaProducer(bootstrap_servers=str_bootstrap_servers)
producer.send("test", b"hello world!")
producer.send("test", key=b"message_two", value=b"this is kafka_python!")
producer.flush()

