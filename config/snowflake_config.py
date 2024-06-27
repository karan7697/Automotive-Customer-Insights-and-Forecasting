import os

SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER', 'your_user')
SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD', 'your_password')
SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT', 'your_account')
SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE', 'your_database')
SNOWFLAKE_WAREHOUSE = os.getenv('SNOWFLAKE_WAREHOUSE', 'your_warehouse')
SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA', 'your_schema')
