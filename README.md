# kafka_etl
ETL example with kafka, S3, Lambda
Based on https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html

Must use Python 2.7.16 for testdata package. The requirements can be installed in a virtualenv with:<br>
<code>virtualenv -p `which python` venv_python2</code><br>
<code>pip install -r requirements_python2.txt</code>
...same for python3 environment
<p>
The cloudformation template takes ~15 mins to complete in AWS (tested in us-east-1 and eu-central-1).

aws kafka get-bootstrap-brokers seems to have a problem - get them from the AWS console

### generate_records.py
A simple program to generate a CSV file with fake data<br>
Usage:
<code>python generate_records.py <number of records> <output file.csv></code>




