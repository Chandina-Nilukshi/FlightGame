import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='project',
            charset='utf8mb4',
            collation='utf8mb4_general_ci',
            autocommit=True
        )
        if connection.is_connected():
            # print("connection successful")
         return connection
    except mysql.connector.Error as err:
        print(f'error: {err}')
        return None
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        # print("connection closed")