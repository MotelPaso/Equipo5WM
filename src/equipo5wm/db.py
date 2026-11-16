import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

database_url = os.getenv("DATABASE_URL")
database_user = os.getenv("DATABASE_USER")
database_pass = os.getenv("DATABASE_PASSWORD")
database_port = os.getenv("DATABASE_PORT")
database_name = os.getenv("DATABASE_NAME")

connection = pymysql.connect(host=database_url,
                            database=database_name,
                            user=database_user,
                            password=database_pass,
                            port=int(database_port))

with connection as c:
    with c.cursor() as cursor:
        sql = "SHOW TABLES"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)