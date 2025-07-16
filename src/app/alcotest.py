import psycopg2
from time import process_time

STEP = 100
request = "SELECT * FROM alcohol WHERE alcohol_name LIKE '%beer%';"

def exec_request(request):
    result = tuple()
    
    connection, cursor = connect()
    cursor.execute(request)
    result = cursor.fetchall()
    disconnect(cursor, connection)
    
    return result

def connect():
    connection = psycopg2.connect(dbname='alcotest', user='postgres', 
                        password='75863302', host='localhost')
    cursor = connection.cursor()
    
    return connection, cursor

def disconnect(cursor, connection):
    cursor.close()
    connection.close()
    
def main():
    full_time = 0
    
    for i in range (STEP): 
        time_1 = process_time()
        result = exec_request(request)
        time_2 = process_time()
        full_time = full_time + time_2 - time_1
    
    full_time = full_time/STEP
        
    print(full_time)
    
main()