

import psycopg2

class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='autosalon',
            user='postgres',
            host='localhost',
            password='1'
        )

    def manager(self, *args, sql, commit=False, fetchone=False, fetchall=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    db.commit()
                elif fetchone:
                    return cursor.fetchone()
                elif fetchall:
                    return cursor.fetchall()
