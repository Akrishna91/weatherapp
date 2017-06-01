import requests
import psycopg2
import psycopg2.extras
from datetime import datetime
import logging

api_key = "adaa706e25105836"

def fetch_data():
    url = "http://api.wunderground.com/api/adaa706e25105836/conditions/q/CA/Bangalore.json"
    r = requests.get(url).json()
    data = r['current_observation']

    location = data['observation_location']['full']
    weather = data['weather']
    temp =  data['temp_f']
    humidity = data['relative_humidity']
    icon_url = data['icon_url']
    observation_time = data['observation_time']
    try:
        conn = psycopg2.connect(dbname='weather', user='postgres', host='localhost', password='12345678')
        print ("DB connected successfully")
    except:
        print(datetime.now(), "unable to connect to the database")
        logging.exception("Unable to connect to the database")
        return
    else:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #write data to db
    cur.execute("""INSERT INTO station_reading(location, weather, temp, humidity, icon_url, observation_time)
                VALUES (%s, %s, %s, %s, %s, %s)""", (location, weather, temp, humidity, icon_url, observation_time))
    conn.commit()
    cur.close()
    conn.close()

    print("Data written", datetime.now())
fetch_data()