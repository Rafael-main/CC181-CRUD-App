from flask import Flask, jsonify
import sqlite3
from sqlite3 import Error
import os
import json

class Student():
    def __init__(self):
        self.DATABASE = '/students_data.db'
        self.basedir = os.path.abspath(os.path.dirname(__file__))

    def create(self, student_id=None,student_first_name=None,student_last_name=None,student_college=None,student_course=None,student_gender=None,student_year=None,student_dept=None):
        self.id = student_id
        self.first_name = student_first_name
        self.last_name = student_last_name
        self.college = student_college
        self.course = student_course
        self.gender = student_gender
        self.year = student_year
        self.dept = student_dept
        params = (self.id, self.first_name, self.last_name, self.college, self.course, self.year,self.gender,self.dept)
        
        conn = sqlite3.connect(self.basedir + self.DATABASE)
        cur = conn.cursor()
        insert_table_query = """ INSERT INTO students VALUES (NULL,?,?,?,?,?,?,?,?) """
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
        select_table_query = " SELECT STUDENT_ID, STUDENT_FIRST_NAME, STUDENT_LAST_NAME, STUDENT_COLLEGE, STUDENT_COURSE, STUDENT_YEAR,STUDENT_GENDER,STUDENT_DEPT FROM students "
        try:
            cur.execute(select_table_query)
            data = cur.fetchall()
            return data
        except Error as e:
            print(e)
        finally:
            conn.close()

    def update(self, student_id=None,student_first_name=None,student_last_name=None,student_college=None,student_course=None,student_gender=None,student_year=None,student_dept=None,student_edit=None):
        self.u_id = student_id
        self.u_first = student_first_name
        self.u_last = student_last_name
        self.u_col = student_college
        self.u_course = student_course
        self.u_gender = student_gender
        self.u_yr = student_year
        self.u_dept = student_dept
        self.this_id = student_edit

        params = (self.u_id,self.u_first, self.u_last, self.u_col, self.u_course, self.u_yr, self.u_gender, self.u_dept,self.this_id)

        conn = sqlite3.connect(self.basedir + self.DATABASE)
        cur = conn.cursor()
        update_table_query = """ UPDATE students 
        SET STUDENT_ID = ?,
        STUDENT_FIRST_NAME = ?, 
        STUDENT_LAST_NAME = ?,
        STUDENT_COLLEGE = ?,
        STUDENT_COURSE = ?,
        STUDENT_GENDER = ?,
        STUDENT_YEAR = ?,
        STUDENT_DEPT = ? 
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

class College():
    def __init__(self):
        self.DATABASE = '/students_data.db'
        self.basedir = os.path.abspath(os.path.dirname(__file__))

    def read(self):
        conn = sqlite3.connect(self.basedir + self.DATABASE)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        select_table_query = " SELECT * FROM  college "
        try:
            cur.execute(select_table_query)
            data = cur.fetchall()
            return data
        except Error as e:
            print(e)
        finally:
            conn.close()
# class Course():
#     def __init__(self):
#         self.DATABASE = '/students_data.db'
#         self.basedir = os.path.abspath(os.path.dirname(__file__))

#         conn = sqlite3.connect(self.basedir + self.DATABASE)
#         cur = conn.cursor()
#         insert_table_query_dept = " INSERT INTO course VALUES(?,?)"
#         params = [
#             ("BACHELOR OF SCIENCE IN CERAMIC ENGINEERING", "MRET"),
#             ("BACHELOR OF SCIENCE IN METALLURGICAL ENGINEERING", "MRET"),
#             ("BACHELOR OF SCIENCE IN CHEMICAL ENGINEERING", "CET"),
#             ("BACHELOR OF SCIENCE IN CIVIL ENGINEERING", "CE"),
#             ("BACHELOR OF SCIENCE IN MECHANICAL ENGINEERING", "MET"),
#             ("BACHELOR OF SCIENCE IN BIOLOGY(GENERAL)", "BS"),
#             ("BACHELOR OF SCIENCE IN BIOLOGY(BOTANY)", "BS"),
#             ("BACHELOR OF SCIENCE IN BIOLOGY(MARINE BIOLOGY)", "BS"),
#             ("BACHELOR OF SCIENCE IN BIOLOGY(ZOOLOGY)", "BS"),
#             ("BACHELOR OF SCIENCE IN CHEMISTRY", "CHEM"),
#             ("BACHELOR OF SCIENCE IN MATHEMATICS", "MAT"),
#             ("BACHELOR OF SCIENCE IN STATISTICS", "MAT"),
#             ("BACHELOR OF SCIENCE IN PHYSICS", "P6"),
#             ("BACHELOR OF SCIENCE IN COMPUTER SCIENCE", "CS"),
#             ("BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY", "ITIS"),
#             ("BACHELOR OF SCIENCE IN INFORMATION SYSTEM", "ITIS"),
#             ("BACHELOR OF SCIENCE IN COMPUTER APPLICATIONS", "CA"),
#             ("BACHELOR OF ELEMENTARY EDUCATION SCIENCE AND MATHEMATICS", "DSME"),
#             ("BACHELOR OF SECONDARY EDUCATION BIOLOGY", "DSME"),
#             ("BACHELOR OF SECONDARY EDUCATION CHEMSTRY", "DSME"),
#             ("BACHELOR OF SECONDARY PHYSICS", "DSME"),
#             ("BACHELOR OF SECONDARY MATHEMATICS", "DSME"),
#             ("BACHELOR OF ELEMENTARY EDUCATION LANGUAGE EDUCATION", "DPRE"),
#             ("BACHELOR OF ELEMENTARY SECONDARY EDUCATION FILIPINO", "DPRE"),
#             ("BACHELOR OF PHYSICAL EDUCATION", "DPE"),
#             ("BACHELOR OF TECHNOLOGY AND LIVELIHOOD EDUCATION MAJOR IN HOME ECONOMICS", "DTTE"),
#             ("BACHELOR OF PHYSICAL TECHNOLOGY-VOCATIONAL TEACHER EDUCATION MAJOR IN DRAFTING TECHNOLOGY", "DTTE"),
#             ("BACHELOR OF PHYSICAL TECHNOLOGY AND LIVELIHOOD EDUCATION MAJOR IN INDUSTRIAL ARTS", "DTTE"),
#             ("BACHELOR OF SCIENCE IN PSYCHOLOGY", "PSYCH"),
#             ("BACHELOR OF ARTS IN ENGLISH", "ENG"),
#             ("BACHELOR OF ARTS IN FILIPINO AND OTHER LANGUAGES", "FIL"),
#             ("BACHELOR OF ARTS IN HISTORY", "HIS"),
#             ("BACHELOR OF ARTS IN POLITICAL SCIENCE", "POL"),
#             ("BACHELOR OF ARTS IN SOCIOLOGY", "SOCIO"),
#             ("BACHELOR OF SCIENCE IN ACCOUNTANCY", "ACC"),
#             ("BACHELOR OF SCIENCE IN ECONOMICS", "ECO"),
#             ("BACHELOR OF SCIENCE IN BUSINESS ADMINISTRATION MAJOR IN BUSINESS ECONOCMICS", "ECO"),
#             ("BACHELOR OF SCIENCE IN BUSINESS ADMINISTRATION MAJOR IN MARKETING MANAGEMENT", "MRKT"),
#             ("BACHELOR OF SCIENCE MAJOR IN ENTREPRENEURSHIP", "MRKT"),
#             ("BACHELOR OF SCIENCE IN HOSPITAL MANAGEMENT", "HRM"),
#             ("BACHELOR OF SCIENCE IN NURSING", "CON")
#         ]

#         try:
#             cur.executemany(insert_table_query_dept, params)
#             conn.commit()
#         except Error as e:
#             print(e)
#         finally:
#             conn.close()

#     def read(self):
#         conn = sqlite3.connect(self.basedir + self.DATABASE)
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         select_table_query = " SELECT COURSE_NAME, COLLEGE_CODE FROM course "
#         # select_table_query = " SELECT * FROM course "
#         try:
#             cur.execute(select_table_query)
#             data = cur.fetchall()
#             # result = cur.execute(select_table_query)
#             # items = []
#             # for row in result:
#             #     items.append({'COURSE_NAME':row[1]})

#             # print(json.dumps({'items':items}))
#             return data
#         except Error as e:
#             print(e)
#         finally:
#             conn.close()
        
#     def update_on_college(self, college_code):
#         conn = sqlite3.connect(self.basedir + self.DATABASE)
#         conn.row_factory = sqlite3.Row
#         cur = conn.cursor()
#         select_table_query = " SELECT * FROM course WHERE COLLEGE_CODE = ? "
#         try:
#             result = cur.execute(select_table_query, (college_code,))
#             # items = []
#             # for row in result:
#                 # items.append({'COURSE_NAME':row[1]})
#             data = [{"COURSE_NAME": row[1]} for row in result]
#             # print(json.dumps({'items':items}))
#             # print(jsonify({'items':items}))
#             return data
#         except Error as e:
#             print(e)
#         finally:
#             conn.close()


# class Department():
#     def __init__(self):
#         self.DATABASE = '/students_data.db'
#         self.basedir = os.path.abspath(os.path.dirname(__file__))

        # conn = sqlite3.connect(self.basedir + self.DATABASE)
        # cur = conn.cursor()
        # insert_table_query_dept = " INSERT or IGNORE INTO department VALUES(?,?,?)"
        # params = [
        #     ("CS", "DEPARTMENT OF COMPUTER SCIENCE", "CCS"),
        #     ("ITIS", "DEPARTMENT OF INFORMATION TECHNOLOGY", "CCS"),
        #     ("CA", "DEPARTMENT OF COMPUTER APPLICATION", "CCS"),
        #     ("CHEM", "DEPARTMENT OF CHEMISTRY", "CSM"),
        #     ("P6", "DEPARTMENT OF PHYSICS", "CSM"),
        #     ("MAT", "DEPARTMENT OF MATHEMATICS AND STATISTICS", "CSM"),
        #     ("BS", "DEPARTMENT OF BIOLOGICAL SCIENCES", "CSM"),
        #     ("NURS", "DEPARTMENT OF NURSING", "CON"),
        #     ("MRET", "DEPARTMENT OF MATERIALS AND RESOURCES ENGINEERING AND TECHNOLOGY", "COET"),
        #     ("CET", "DEPARTMENT OF CHEMICAL ENGINEERING AND TECHNOLOGY", "COET"),
        #     ("CE", "DEPARTMENT OF CIVIL ENGINEERING", "COET"),
        #     ("EEET", "DEPARTMENT OF ELECTRICAL AND ELECTRONICS ENGINEERING AND TECHNOLOGY", "COET"),
        #     ("MET", "DEPARTMENT OF MECHANICAL ENGINEERING AND TECHNOLOGY", "COET"),
        #     ("DSME", "DEPARTMENT OF SCIENCE AND MATHEMATICS EDUCATION", "CED"),
        #     ("DPRE", "DEPARTMENT OF PROFESSIONAL EDUCATION", "CED"),
        #     ("DPE", "DEPARTMENT OF PHYSICAL EDUCATION", "CED"),
        #     ("DTTE", "DEPARTMENT OF TECHNOLOGY TEACHER EDUCATION", "CED"),
        #     ("PSYCH", "DEPARTMENT OF PSYCHOLOGY", "CASS"),
        #     ("ENG", "DEPARTMENT OF ENGLISH", "CASS"),
        #     ("FIL", "DEPARTMENT OF FILIPINO & OTHER LANGUAGES", "CASS"),
        #     ("HIS", "DEPARTMENT OF HISTORY", "CASS"),
        #     ("POL", "DEPARTMENT OF POLITICAL SCIENCE", "CASS"),
        #     ("SOCIO", "DEPARTMENT OF SOCIOLOGY", "CASS"),
        #     ("ACC", "DEPARTMENT OF ACCOUNTANCY", "CBAA"),
        #     ("ECO", "DEPARTMENT OF ECONOMICS", "CBAA"),
        #     ("MRKT", "DEPARTMENT OF MARKETING", "CBAA"),
        #     ("HRM", "DEPARTMENT OF HOSPITALITY AND TOURISM MANAGEMENT", "CBAA") 
        # ]

        # try:
        #     cur.executemany(insert_table_query_dept, params)
        #     conn.commit()
        # except Error as e:
        #     print(e)
        # finally:
        #     conn.close()

class Joined():
    def __init__(self):
        self.DATABASE = '/students_data.db'
        self.basedir = os.path.abspath(os.path.dirname(__file__))

    def read_on_all(self):
        query = """SELECT college.COLLEGE_NAME, 
                department.DEPT_NAME, 
                course.COURSE_NAME 
                FROM department 
                INNER JOIN course ON department.DEPT_ID=course.DEPT_ID
                INNER JOIN college ON department.COLLEGE_CODE=college.COLLEGE_CODE"""

        conn = sqlite3.connect(self.basedir + self.DATABASE)
        cur = conn.cursor()
        conn.row_factory = sqlite3.Row
        try: 
            cur.execute(query)
            data = cur.fetchall()
            return data
        except Error as e:
            print(e)
        finally:
            conn.close()
    
    def read_on_colCourse(self):
        query = """SELECT college.COLLEGE_NAME,
                course.COURSE_NAME 
                FROM department 
                INNER JOIN course ON department.DEPT_ID=course.DEPT_ID
                INNER JOIN college ON department.COLLEGE_CODE=college.COLLEGE_CODE"""

        conn = sqlite3.connect(self.basedir + self.DATABASE)
        cur = conn.cursor()
        conn.row_factory = sqlite3.Row
        try: 
            cur.execute(query)
            data = cur.fetchall()
            return data
        except Error as e:
            print(e)
        finally:
            conn.close()

    def select_college(self, code):
        query = """SELECT college.COLLEGE_NAME,
                department.DEPT_NAME
                FROM department 
                INNER JOIN course ON department.DEPT_ID=course.DEPT_ID
                INNER JOIN college ON department.COLLEGE_CODE=college.COLLEGE_CODE
                WHERE course.COURSE_NAME=?"""

        conn = sqlite3.connect(self.basedir + self.DATABASE)
        cur = conn.cursor()
        conn.row_factory = sqlite3.Row
        try: 
            cur.execute(query,(code,))
            data = cur.fetchall()
            return data
        except Error as e:
            print(e)
        finally:
            conn.close()

    def read_all_course(self):
        query = """SELECT department.COLLEGE_CODE,
                course.COURSE_NAME
                FROM department 
                INNER JOIN course ON department.DEPT_ID=course.DEPT_ID
                INNER JOIN college ON department.COLLEGE_CODE=college.COLLEGE_CODE"""

        conn = sqlite3.connect(self.basedir + self.DATABASE)
        cur = conn.cursor()
        conn.row_factory = sqlite3.Row
        try: 
            cur.execute(query)
            data = cur.fetchall()
            return data
        except Error as e:
            print(e)
        finally:
            conn.close()



if __name__ == "__main__":
    Student()
    Joined()
    College()