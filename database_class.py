import mysql.connector as mysql


class Database:
    def __init__(self, host, user, password, database):
        self.conn = None
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

    def show_table(self):
        self.cursor.execute("SHOW TABLES")
        tables = self.cursor.fetchall()
        for table in tables:
            print(table)

    def insert_values(self, query, values):
        self.cursor.execute(query, values)
        self.db.commit()
        print(self.cursor.rowcount, "records inserted")

    def select_records(self, query):
        # query = "SELECT * FROM Branch"
        self.cursor.execute(query)
        records = self.cursor.fetchall()

        for record in records:
            print(record)

    def update_records(self, query):
        self.cursor.execute(query)
        self.db.commit()

    def get_column(self, query):
        self.cursor.execute(query)
        usernames = self.cursor.fetchall()
        return usernames

    def close_connection(self):
        self.cursor.close()
        self.db.close()


