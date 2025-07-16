import psycopg2
from connection import connect, disconnect, user_connect

def exec_user_request(request, user_login, user_password):
    result = tuple()
    
    connection, cursor = user_connect(user_login, user_password)
    cursor.execute(request)
    result = cursor.fetchall()
    disconnect(cursor, connection)
    
    return result

def exec_request(request):
    result = tuple()
    
    connection, cursor = connect()
    cursor.execute(request)
    result = cursor.fetchall()
    disconnect(cursor, connection)
    
    return result

def exec_user_active_request(request, user_login, user_password):
    result = tuple()
    
    connection, cursor = user_connect(user_login, user_password)
    cursor.execute(request)
    connection.commit()
    disconnect(cursor, connection)

def exec_active_request(request):
    result = tuple()
    
    connection, cursor = connect()
    cursor.execute(request)
    connection.commit()
    disconnect(cursor, connection)

def enter_req():
    request = "SELECT * FROM users"
    exec_request(request)