import pandas as pd
import sqlalchemy
from config import snowflake_config

def get_data():
    engine = sqlalchemy.create_engine(
        f'snowflake://{snowflake_config.SNOWFLAKE_USER}:{snowflake_config.SNOWFLAKE_PASSWORD}@{snowflake_config.SNOWFLAKE_ACCOUNT}/{snowflake_config.SNOWFLAKE_DATABASE}/{snowflake_config.SNOWFLAKE_SCHEMA}?warehouse={snowflake_config.SNOWFLAKE_WAREHOUSE}'
    )
    query = """
    SELECT * FROM automotive_data
    """
    df = pd.read_sql(query, engine)
    return df

def main():
    df = get_data()
    df.to_csv('data/raw_data.csv', index=False)

if __name__ == "__main__":
    main()
