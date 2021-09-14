import pandas as pd
import sqlalchemy
from crawler.db_login import *
from sqlalchemy.exc import SQLAlchemyError


# TODO: Differenciate if Database is accessed externally or via
#       local host
# TODO: Error Handling check if Data is writen to db or is accesible
# TODO: Server auf IONOS mieten und da die Datenbank aufziehen
#       Vertragslaufzeit 12 Monate / 30 Tage geldzurück garantie
#       Vorher den Vertrag kündigen! Mal ausprobieren!

def database_conn():
    return sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                    format(database_username, database_password,
                                           database_ip, database_name))


def write_to_db(df):
    print(df)
    # write to database
    try:
        df.to_sql(con=database_conn(), name='locality_info', if_exists='replace')
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)


def read_from_db():
    try:
        df_sql = pd.read_sql_table(table_name='locality_info', con=database_conn())
        print(df_sql)
        return df_sql

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        print(error)
