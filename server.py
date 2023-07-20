import time
from socket import *
import mysql.connector as mysql
from database_class import Database
import pickle
from pickler import ShoppingSystem
import random

# Create an instance of the Database class
mydb = Database(host="localhost",
                user="root",
                password="Moraanu7",
                database="Investment"
                     )
# cursor = mydb.cursor()
# cursor.execute("CREATE DATABASE Investment")
#
# cursor.execute("SHOW DATABASES")
# databases = cursor.fetchall()
# print(databases)

# cursor.execute("CREATE TABLE users ("
#                "name VARCHAR(255), "  change to email
#                "user_name VARCHAR(255), "
#                "password VARCHAR(14), "
#                "clientID VARCHAR(7), "
#                "balance integer"
#                ")")
mydb.connect()
query = ("CREATE TABLE transaction("
         "ClientID VARCHAR(7), "
         "Crypto VARCHAR(25), "
         "Date VARCHAR(45), "       # change from VARCHAR to date
         "Buy_or_sell VARCHAR(5), "
         "Quantity VARCHAR(100), "
         "Cost VARCHAR(100)"
         ")")
mydb.create_table(query)
mydb.show_table()
mydb.select_records("SELECT * FROM users")


HOST = '127.0.0.1' # or  '127.0. 0.1'
PORT = 5005
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
    page_object = pickle.loads(message)
    page = page_object[0]
    item = page_object

    if counter == 1:
        data = page
        counter += 1
        if page == "action1":
            query = f"SELECT clientID FROM users WHERE user_name = '{username}'"
            clientID = mydb.get_column(query)
            clientID = clientID[0][0]
            print(clientID, "this is unique")
            client.send(clientID.encode())
    else:
        content = item
        counter = 1
        print(data, content)
        print(content[0])
        # time.sleep(1.0)
        if data == "page1":     # receiving user details and gen. clientID
            query = "INSERT INTO users (name, user_name, password, clientID) " \
                    "VALUES (%s, %s, %s, %s)"
            clientid = content[0]
            clientid = f"{clientid[0:2]}" * 2 + str(random.randint(2, 20))
            values = (content[0], content[1], content[2], clientid)
            username = content[1]
            mydb.insert_values(query, values)

        if data == "page2":     #adding the initial investment amount
            amount = int(content[0])
            print(amount, username)
            query = f"UPDATE users SET balance = {amount} WHERE user_name = '{username}'"
            mydb.update_records(query)

        if data == "page3":     # receive transaction details and
            me = ""             # store in the transaction table





