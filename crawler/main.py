from crawler.over_pass_api import *

# TODO bei Serverproblemen neue starten nach zeit ablauf !
# TODO Overpass API Limits abchecken
# TODO Pandas Dataframe push to Database XAMPP! Methoden richtig
# TODO verknüpüfen + DOKU
# TODO Error Handling bei over_pass_api anpassen!
# TODO To many requests hier einen delay einbauen limits API anschauen!
# TODO relative Pfade anpassen

# call API
get_amenity_info("München", "bar|cafe|pub|restaurant")
