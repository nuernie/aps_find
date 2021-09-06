import pandas as pd
import sqlalchemy
from crawler.db_login import *
from sqlalchemy.exc import SQLAlchemyError



df = pd.DataFrame({'num_legs': [12, 4, 8, 18],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]})
print(df)
try:
    database_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                                   format(database_username, database_password,
                                                          database_ip, database_name))
    df.to_sql(con=database_connection, name='locality_info', if_exists='replace')
except SQLAlchemyError as e:
    error = str(e.__dict__['orig'])
    print(error)
