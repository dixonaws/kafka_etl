import csv
from kafka import KafkaProducer

# return a list containing one record for each line in a CSV file
def read_file(str_filename):
    lst_file_contents=[]
    file_filename=open(str_filename, "r")

    for str_lines in file_filename:
        lst_file_contents.append(file_filename.readline())

    file_filename.close()
    return(lst_file_contents)

# insert into the kafka topic buffer (don't flush)
def insert_into_kafka_topic(kafka_producer, str_topic_name, str_message):
    bytes_message=bytes(str_message, "utf-8")
    kafka_producer.send(str_topic_name, bytes_message)


def main():
    str_filename="records.csv"
    str_bootstrap_servers = "localhost:9092"
    kafka_producer = KafkaProducer(bootstrap_servers=str_bootstrap_servers)

    lst_records=read_file(str_filename)

    print("lst_records contains " + str(len(lst_records)) + " records")

    str_topic_name="test"

    # insert each record into the kafka topic buffer
    for str_record in lst_records:
        print(type(str_record))
        insert_into_kafka_topic(kafka_producer, str_topic_name, str_record)

    # finally write to the buffer (flush the buffer to kafka all at once)
    kafka_producer.flush()

main()