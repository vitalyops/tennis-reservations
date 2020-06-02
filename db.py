import psycopg2

class PostgreSQL():
    def __init__(self, db="mydb", user="postgres"):
        self.conn = psycopg2.connect(database=db, user=user)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()
