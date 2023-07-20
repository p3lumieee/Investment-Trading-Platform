from socket import *
import mysql.connector as mysql

HOST = '127.0.0.1' # or  '127.0. 0.1'
PORT = 5000
BUFSIZE = 1024

ADDRESS = (HOST, PORT)
# 1 socket
server_socket = socket(AF_INET, SOCK_STREAM)
# 2 bind
server_socket.bind(ADDRESS)
# 3 listen
server_socket.listen(5)
data = None
content = None
counter = 1
while True:

    print('Waiting for connection ...')
    # 4. accept
    (client, address) = server_socket.accept()
    print(f'... connection from : {address}')
    message = client.recv(BUFSIZE)
    page = str(message.decode())

    if counter == 1:
        data = page
        counter += 1
    else:
        content = page
        counter = 1
        print(data, content)

    # Create an instance of the BankDatabase class
    db = mysql.connect(host="localhost",
                        user="root",
                        password="Moraanu7",
                        database="Investment")

    cursor = db.cursor()
    # cursor.execute("CREATE DATABASE Investment")

    # cursor.execute("SHOW DATABASES")
    # databases = cursor.fetchall()
    # print(databases)

    # cursor.execute("CREATE TABLE users ("
    #                "name VARCHAR(255), "
    #                "user_name VARCHAR(255), "
    #                "password VARCHAR(14), "
    #                "clientID VARCHAR(7)"
    #                ")")

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print(tables)

