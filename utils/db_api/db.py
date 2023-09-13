import sqlite3


class Comment:
    def __init__(self):
        self.connection = sqlite3.connect("p3.db")
        self.cursor = self.connection.cursor()
        self.create_user()

    def create_user(self):
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
        self.cursor.execute(f"""
            SELECT * from comment
        """)
        return self.cursor.fetchall()

    #
    # def get_user(self, id):
    #     self.cursor.execute("""
    #         select * from user where id=?
    #     """, (id,))
    #     return self.cursor.fetchone()
    #
    # # def update_user(self, id, name, age, phone_number, email, photo):
    # #     self.cursor.execute("""
    # #         update user set name=?, age=?, phone_number=?, email=?, photo=?
    # #         where id=?
    # #     """, (name, age, phone_number, email, photo, id))
    # #     self.connection.commit()
    #
    # def update_user_name(self, id, name):
    #     self.cursor.execute("""
    #         update user set name=? where id=?
    #     """, (name, id))
    #     self.connection.commit()
    #
    # def update_user_age(self, id, age):
    #     self.cursor.execute("""
    #         update user set age=? where id=?
    #     """, (age, id))
    #     self.connection.commit()
    #
    # def update_user_phone(self, id, phone_number):
    #     self.cursor.execute("""
    #         update user set phone_number=? where id=?
    #     """, (phone_number, id))
    #     self.connection.commit()
    #
    # def update_user_email(self, id, email):
    #     self.cursor.execute("""
    #         update user set email=? where id=?
    #     """, (email, id))
    #     self.connection.commit()
    #
    # def update_user_photo(self, id, photo):
    #     self.cursor.execute("""
    #         update user set photo=? where id=?
    #     """, (photo, id))
    #     self.connection.commit()
    #
    # def delete_user(self, id):
    #     self.cursor.execute("""
    #         delete from user where id=?
    #     """, (id,))
    #     self.connection.commit()
    #
    #
