import mysql.connector
def connection():
    conn =mysql.connector.connect(
                            host="localhost",
                           user ="root",
                           passwd ="root",
                           database ="sakila")
    

    return conn

