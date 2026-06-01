import os
# import requests
from dotenv import load_dotenv

import pymysql

load_dotenv()

def get_connection():
    # connect to database
    return pymysql.connect(
        host=os.getenv("HOST"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        database=os.getenv("DATABASE"),
        
    )