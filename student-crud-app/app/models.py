from flask import Flask
import sqlite3
from sqlite3 import Error
import os


class Student():
    def __init__(self):

        self.DATABASE = '/students_data.db'
        self.basedir = os.path.abspath(os.path.dirname(__file__))
        conn = None

        try:
            if conn is None:
                conn = sqlite3.connect(self.basedir + self.DATABASE)

            create_table_query = """ CREATE TABLE IF NOT EXISTS students (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                STUDENT_ID TEXT UNIQUE NOT NULL,
                STUDENT_FIRST_NAME TEXT NOT NULL,
                STUDENT_LAST_NAME TEXT NOT NULL,
                STUDENT_COLLEGE TEXT NOT NULL,
                STUDENT_COURSE TEXT NOT NULL,
                STUDENT_YEAR INTEGER NOT NULL
            ) """

            cur = conn.cursor()
            cur.execute(create_table_query)
        except Error as e:
            print(e)
        finally:
            conn.close()

    def create(self, student_id=None,student_first_name=None,student_last_name=None,student_college=None,student_course=None,student_year=None):
        self.id = student_id
        self.first_name = student_first_name
        self.last_name = student_last_name
        self.college = student_college
        self.course = student_course
        self.year = student_year
        params = (self.id, self.first_name, self.last_name, self.college, self.course, self.year)
        
        conn = sqlite3.connect(self.basedir + self.DATABASE)
        cur = conn.cursor()
        insert_table_query = """ INSERT INTO students VALUES (NULL,?,?,?,?,?,?) """
        try:
            cur.execute(insert_table_query, params)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

    def read(self):
        conn = sqlite3.connect(self.basedir + self.DATABASE)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        select_table_query = " SELECT STUDENT_ID, STUDENT_FIRST_NAME, STUDENT_LAST_NAME, STUDENT_COLLEGE, STUDENT_COURSE, STUDENT_YEAR FROM students "
        try:
            cur.execute(select_table_query)
            data = cur.fetchall()
            return data
        except Error as e:
            print(e)
        finally:
            conn.close()



    def update(self, student_id=None,student_first_name=None,student_last_name=None,student_college=None,student_course=None,student_year=None):
        self.u_id = student_id
        self.u_first = student_first_name
        self.u_last = student_last_name
        self.u_col = student_college
        self.u_course = student_course
        self.u_yr = student_year

        params = (self.u_first, self.u_last, self.u_col, self.u_course, self.u_yr, self.u_id)

        conn = sqlite3.connect(self.basedir + self.DATABASE)
        cur = conn.cursor()
        update_table_query = """ UPDATE students 
        SET STUDENT_FIRST_NAME = ?, 
        STUDENT_LAST_NAME = ?,
        STUDENT_COLLEGE = ?,
        STUDENT_COURSE = ?,
        STUDENT_YEAR = ? 
        WHERE STUDENT_ID = ? """

        try:
            cur.execute(update_table_query, params)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()
                                

    def delete(self, id):
        self.del_id = id
        delete_table_query = " DELETE FROM students WHERE STUDENT_ID=? "
        params = (self.del_id,)
        conn = sqlite3.connect(self.basedir + self.DATABASE)
        cur = conn.cursor()
        try:
            cur.execute(delete_table_query,params)
            conn.commit()
        except Error as e:
            print(e)
        finally:
            conn.close()

if __name__ == "__main__":
    Student()
    
