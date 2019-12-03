from record import Record
import csv
import sys

str_aws_region = "eu-west-1"

int_records_to_put = 100
str_filename="employ_data.csv"
list_records=[]

file_employ_data=open(str_filename, "w")

sys.stdout.write("Generating " + str(int_records_to_put) + " records... ")
for dict_record in Record().generate(int_records_to_put):  # generate int_users_to_put users
	# print(record)
	list_records.append(dict_record)
print("done, list_records contains " + str(len(list_records)) + " records." )

sys.stdout.write("Writing " + str_filename + " in CSV format... ")
csvwriter=csv.writer(file_employ_data)

# write each record in the list
int_counter=0
for dict_record in list_records:
	# if we are writing the first record, write the header row
	if(int_counter==0):
		csvwriter.writerow(dict_record.keys())

	csvwriter.writerow(dict_record.values())
	int_counter=int_counter+1

print("done.")
file_employ_data.close()



