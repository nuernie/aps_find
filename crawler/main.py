from crawler.over_pass_api import *
from database_conn import*
# TODO Overpass API Limits abchecken
# TODO Pandas Dataframe push to Database XAMPP! Methoden richtig
# TODO verknüpüfen + DOKU
# TODO Error Handling bei over_pass_api anpassen!
# TODO To many requests hier einen delay einbauen limits API anschauen!
# TODO relative Pfade anpassen

# call API
df = get_amenity_info("München", "bar|cafe|pub|restaurant")
# transform dataset
df = transform_dataset(df)
# write to db
write_to_db(df)
# read from db
df = read_from_db()



