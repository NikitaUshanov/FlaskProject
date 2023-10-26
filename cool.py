from sqlalchemy import create_engine
import pandas as pd
from config import Config
import time

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)


def to_sql():
    df = pd.read_csv('train.csv')
    df.columns = [c.lower() for c in df.columns]
    df.to_sql("fin", engine)

def article_to_sql():
    df = pd.read_json("article.json")
    df.to_sql("article", engine)


def from_sql():
    df = pd.read_sql_query('select * from "fin"', con=engine)
    df.to_csv('train.csv')


if __name__ == "__main__":
    to_sql()
    article_to_sql()
    print("Датасеты загружен в базу данных!")
