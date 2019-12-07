# kafka_etl
ETL example with kafka, S3, Lambda
Based on https://docs.aws.amazon.com/msk/latest/developerguide/getting-started.html

Must use Python 2.7.16 for testdata package. The requirements can be installed in a virtualenv with:
<code>virtualenv -p `which python` venv_python2</code>
<code>pip install -r requirements_python2.txt</code>
...same for python3 environment

The cloudformation template takes ~15 mins to complete.

aws kafka get-bootstrap-brokers seems to have a problem - get them from the AWS console



