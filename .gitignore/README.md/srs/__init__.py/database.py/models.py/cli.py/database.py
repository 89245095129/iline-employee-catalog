
import psycopg2
from configparser import ConfigParser
from prettytable import PrettyTable

def config(filename='config/database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    return {k: v for k, v in parser.items(section)}

def connect():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None