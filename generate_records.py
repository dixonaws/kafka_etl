import json
import boto3
from record import Record
import csv

str_aws_region = "eu-west-1"

int_records_to_put = 100

file_employ_data=open("employ_data.csv", "w")
list_records=[]

for dict_record in Record().generate(int_records_to_put):  # generate int_users_to_put users
	# print(record)
	list_records.append(dict_record)

csvwriter=csv.writer(file_employ_data)

print(len(list_records))

csvwriter.writerow(list_records.pop().keys())

for dict_record in list_records:
	print(dict_record)
	csvwriter.writerow(dict_record.values())



