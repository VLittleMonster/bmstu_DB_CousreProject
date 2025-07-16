import psycopg2

def connect():
    connection = psycopg2.connect(dbname='alcomarket', user='postgres', 
                        password='75863302', host='localhost')
    cursor = connection.cursor()
    
    return connection, cursor

def user_connect(user_login, user_password):
    connection = psycopg2.connect(dbname='alcomarket', user=user_login, 
                        password=user_password, host='localhost')
    cursor = connection.cursor()
    
    return connection, cursor

def disconnect(cursor, connection):
    cursor.close()
    connection.close()