from sqlalchemy import create_engine
import pandas as pd
import time

engine = create_engine('mysql+pymysql://root:test@localhost/db_1')


def to_sql():
    df = pd.read_csv('train.csv')
    df.columns = [c.lower() for c in df.columns]
    df.to_sql("fin", engine)


def from_sql():
    df = pd.read_sql_query('select * from "fin"', con=engine)
    df.to_csv('train.csv')


if __name__ == "__main__":
    to_sql()
    #from_sql()
    print("Датасет загружен в базу данных!")

