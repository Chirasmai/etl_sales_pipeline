# load.py

from sqlalchemy import create_engine
import pandas as pd

def load_data(df, db_url, table_name):
    """
    Load DataFrame into database table
    """
    engine = create_engine(db_url)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Data loaded successfully into table '{table_name}'")
