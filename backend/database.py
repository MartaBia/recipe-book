import psycopg2

class Database():
    def __init__(self):
        self.conn = psycopg2.connect(
            host='localhost',
            port='5432',
            database='cookbook',
            user='postgres',
            password='password'
        )

    def execute(self, query, params=None):
        cur = self.conn.cursor()
        cur.execute(query, params)
        self.conn.commit()
        cur.close()

    def fetch_one(self, query, params=None):
        cur = self.conn.cursor()
        cur.execute(query, params)
        result = cur.fetchone()
        cur.close()
        return result
    
    def fetch_all(self, query, params=None):
        cur = self.conn.cursor()
        cur.execute(query, params)
        result = cur.fetchall()
        cur.close()
        return result
