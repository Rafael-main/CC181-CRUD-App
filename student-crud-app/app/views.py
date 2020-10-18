from flask import render_template, request, redirect, jsonify, flash, url_for
from app import app
import app.models as models

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = models.Student()
    if request.method == 'POST':
        idid = request.values.get('inputID')
        first = request.values.get('inputFirst')
        last = request.values.get('inputLast')
        college = request.values.get('inputCollege')
        course = request.values.get('inputCourse')
        year = request.values.get('inputYear')
        user.create(idid, first, last, college, course, year)
        flash("Record Created!", "success")
        return redirect('/')
    
    rows = user.read()
    return render_template('index.html', rows=rows)

@app.route('/edit', methods=['POST'])
def edit():
    user = models.Student()
    if request.method == 'POST':
        edit_idid = request.values.get('editInputID')
        edit_first = request.values.get('editInputFirst')
        edit_last = request.values.get('editInputLast')
        edit_college = request.values.get('editInputCollege')
        edit_course = request.values.get('editInputCourse')
        edit_year = request.values.get('editInputYear')
        user.update(edit_idid, edit_first, edit_last, edit_college, edit_course, edit_year)
        flash("Record Edited!", "success")
        return redirect('/')

@app.route('/delete', methods=['POST'])
def delete():
    user = models.Student()
    if request.method == 'POST':
        del_id = request.values.get('delInputID')
        user.delete(del_id)
        flash("Record Deleted!", "success")
        return redirect('/')