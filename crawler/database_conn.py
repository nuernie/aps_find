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


df = pd.DataFrame({'num_legs': [13, 4, 8, 18],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]})
print(df)
# write to database
try:
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                   format(database_username, database_password,
                                                          database_ip, database_name))
    df.to_sql(con=database_connection, name='locality_info', if_exists='replace')
except SQLAlchemyError as e:
    error = str(e.__dict__['orig'])
    print(error)

# read from database
df_sql = pd.read_sql_table('locality_info', database_connection)
print(df_sql)
# 1 vCore CPU 3GHz ohne graphische oberfläche!
# vnc console vnc viewer / 