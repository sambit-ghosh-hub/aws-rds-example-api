# Using A PostgreSQL database to build an API

This project is part of an article I have written on how to use AWS RDS to build an API with PostgreSQL as database to store some user data. It can be found [here](https://medium.com/@sambit-ghosh/how-to-deploy-a-database-on-aws-rds-and-use-it-to-build-an-api-a5797b4e6d46).

This project can be used as a template to build a python flask based API with database connection to any hosted PostgreSQL database. 

## Setup Instructions:
First make sure you have a working PostgreSQL database up and running somewhere and obtain its URL, port and other credentials needed to access it.

You need to create a file called ".env" and store the following environment variables and their appropriate values
>DATABASE_URL=localhost

>DATABASE_PORT=5432

>DATABASE_NAME=database-1

>DATABASE_USER=postgres

>DATABASE_PASS=password

Also make sure to install the requirements using :
```bash
pip install -r requirements.txt
```

If something is not working check the [article](https://medium.com/@sambit-ghosh/how-to-deploy-a-database-on-aws-rds-and-use-it-to-build-an-api-a5797b4e6d46) and make sure you followed correctly.