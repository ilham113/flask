# -*- coding: utf-8 -*-
#NAMA : Muhammad Ilham Z
#NIM : 182102024
#

from flask import Flask, json, jsonify, request, render_template

app = Flask(__name__)

students= [
{
 'name': 'Daenerys Targaryen',
 'gpa': 3.7,
 'courses':[
         {
         'name': 'calculus',
         'credit': 3,
         'score': 'A-'
         },
         {
         'name': 'programming',
         'credit': 4,
         'score': 'B+'    
         }
         ]
},
{
 'name': 'Jhon Snow',
 'gpa': 3.4,
 'courses':[
         {
         'name': 'calculus',
         'credit': 3,
         'score': 'B'
         },
         {
         'name': 'programming',
         'credit': 4,
         'score': 'A'    
         }
         ]
}]
 
# GET /student
@app.route('/student/')
def get_students():
    return jsonify({'students':students})

# GET /student/<string:name>
@app.route('/student/<string:name>')
def get_student(name):
   for student in students:
      if student ['name'] == name :
         return jsonify(student)
   return jsonify({'massage': 'students not found'})

# GET /student/<string:name>/course
@app.route('/student/<string:name>/course')
def get_course_in_student(name):
   for student in students:
      if student ['name'] == name :
         return jsonify({'course': student['courses']})
   return jsonify({'massage': 'student not found'})

#GET /student/<string:name>/GPA
@app.route('/student/<string:name>/GPA')
def get_GPA(name):
   for student in students:
      if student ['name'] == name :
         return jsonify({'GPA': student['gpa']})
   return jsonify({'massage': 'student not found'})

app.run(port=5000)