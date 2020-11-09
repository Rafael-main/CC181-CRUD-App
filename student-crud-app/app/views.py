from flask import render_template, request, redirect, jsonify, flash, url_for, json
from app import app
import app.models as models

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = models.Student()
    college = models.College()
    rows_college = college.read()
    course = models.Joined()
    rows_course = course.read_all_course()
    rows_student = user.read()
    return render_template('index.html', rows_course=rows_course, rows=rows_student, rows_college=rows_college)

@app.route('/some_list', methods=['GET'])
def some_list():
    user = models.Joined()
    rows_deptcolcor = user.read_on_all()
    return render_template('dept_course.html', rows=rows_deptcolcor)

@app.route('/_add', methods=['POST'])
def add():
    user = models.Student()
    col = models.Joined()
    if request.method == 'POST':
        idid = request.form['inputID']
        first = str(request.form['inputFirst']).capitalize()
        last = str(request.form['inputLast']).capitalize()
        course = request.form['inputCourse']
        gender = request.form['inputGender']
        year = int(request.form['inputYear'])
        data_col_dept = col.select_college(course)
        college = data_col_dept[0][0]
        dept = data_col_dept[0][1]

        
        user.create(idid, first, last, college, course, gender, year, dept)
        flash("Record Created!", "success")
        return redirect('/')


@app.route('/_edit', methods=['POST'])
def edit():
    user = models.Student()
    col = models.Joined()
    if request.method == 'POST':
        edit_idid = request.form['editInputID']
        edit_first = str(request.form['editInputFirst']).capitalize()
        edit_last = str(request.form['editInputLast']).capitalize()
        edit_course = request.form['editInputCourse']
        edit_year = int(request.form['editInputYear'])
        data_col_dept = col.select_college(edit_course)
        edit_college = data_col_dept[0][0]
        edit_dept = data_col_dept[0][1]
        user.update(edit_idid, edit_first, edit_last, edit_college, edit_course, edit_year,edit_dept)
        flash("Record Edited!", "success")
        return redirect('/')

@app.route('/_delete', methods=['POST'])
def delete():
    user = models.Student()
    if request.method == 'POST':
        del_id = request.values.get('delInputID')
        user.delete(del_id)
        flash("Record Deleted!", "success")
        return redirect('/')
