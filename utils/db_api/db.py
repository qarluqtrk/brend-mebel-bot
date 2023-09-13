import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("auth")
        self.cursor = self.connection.cursor()
        self.create_user()

    def create_user(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY,
                name VARCHAR,
                phone_number VARCHAR,
                longitude VARCHAR,
                latitude VARCHAR
            )
        """)
        self.connection.commit()

    # ...

    def add_user(self, name, phone_number, longitude, latitude):
        self.cursor.execute("""
            insert into user (name, phone_number, longitude, latitude)
            values (?, ?, ?, ?)
        """, (name, phone_number, longitude, latitude))
        self.connection.commit()

    def all_user(self):
        self.cursor.execute(f"""
            SELECT * from user
        """)
        return self.cursor.fetchall()

    def get_user(self, id):
        self.cursor.execute("""
            select * from user where id=?
        """, (id,))
        return self.cursor.fetchone()

    def delete_user(self, id):
        self.cursor.execute("""
            delete from user where id=?
        """, (id,))
        self.connection.commit()


class Comment:
    def __init__(self):
        self.connection = sqlite3.connect("comment")
        self.cursor = self.connection.cursor()
        self.create_comment()

    def create_comment(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS comment(
                id INTEGER PRIMARY KEY,
                comment VARCHAR,
                user_id INTEGER
            )
        """)
        self.connection.commit()

    def add_comment(self, comment, user_id):
        self.cursor.execute("""
            INSERT INTO comment (comment, user_id)
            VALUES (?, ?)
        """, (comment, user_id))
        self.connection.commit()

    def all_comment(self):
        self.cursor.execute("""
            SELECT * FROM comment
        """)
        return self.cursor.fetchall()
