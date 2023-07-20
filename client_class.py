from socket import *
import mysql.connector as mysql
import pickle

class Send:
    def __init__(self, host, port, bufsize):
        self.HOST = host
        self.PORT = port
        self.BUFSIZE = bufsize
        self.ADDRESS = (self.HOST, self.PORT)

    def send(self, message, switch):
        # 1 socket
        s = socket(AF_INET, SOCK_STREAM)
        s.connect(self.ADDRESS)
        if switch == 1:
            pick_object = pickle.dumps(message)
            s.send(pick_object)
            message = s.recv(self.BUFSIZE)
            return message.decode()
        else:
            pick_object = pickle.dumps(message)
            s.send(pick_object)
        s.close()

    # def receive(self):
    #     s = socket(AF_INET, SOCK_STREAM)
    #     s.connect(self.ADDRESS)
    #     message = s.recv(self.BUFSIZE)
    #     return message





class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db = None
        self.cursor = None

    def connect(self):
        self.db = mysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.db.cursor()

    def create_table(self, query):
        self.cursor.execute(query)

    def show_tables(self):
        self.cursor.execute("SHOW TABLES")
        tables = self.cursor.fetchall()
        for table in tables:
            print(table)

    def insert_values(self, query, values):
        self.cursor.executemany(query, values)
        self.db.commit()
        print(self.cursor.rowcount, "records inserted")

    def select_records(self, query):
        # query = "SELECT * FROM Branch"
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        for record in records:
            print(record)

    def close_connection(self):
        self.cursor.close()
        self.db.close()