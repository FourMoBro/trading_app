import psycopg2
import config

connection = psycopg2.connect(config.DB_FILE)

cursor = connection.cursor()






connection.commit()