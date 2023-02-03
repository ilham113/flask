# Nama: Muhammad Ilham Z
# NIM:  182102024

from flask import Flask
from flask_restful import Resource, Api
from data import students

app = Flask(__name__)
api = Api(app)

class StudentList(Resource):
    def get(self):
       return{'Students':students}

class Student(Resource): 
    def get(self, name):
        for stds in students:
        	if stds['name'] == name:
        		return stds
        return{'Students':'None'}, 404		

class StudentName(Resource):
    def get(self):
        names = []
        for stds in students:
            names.append(stds['name'])
        return {'StudentNames': names}

class StudentDept(Resource):
    def get(self,dept):
        for stds in students:
            if stds['dept'] == dept:
                names = []
                for stds in students:
                    if stds['dept'] == dept:
                        names.append(stds['name'])
                return {'StudentNames': names}
        return{'StudentNames':'None'}, 404
        

#        names = []
#        for stds in students:
#            if stds['dept'] == dept:
#                names.append(stds['name'])
#        return {'StudentNames': names}        

class Course(Resource):
    def get(self, name):
        for stds in students:
        	if stds['name'] == name:
        		return stds['courses']
        return{'Students':'None'}, 404	

       
api.add_resource(StudentList, '/students')
api.add_resource(Student, '/student/<string:name>')
api.add_resource(StudentName, '/student/name')
api.add_resource(StudentDept, '/student/name/<string:dept>')
api.add_resource(Course, '/course/<string:name>')

app.run(port=5000, debug=True)
