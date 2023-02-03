#Nama: MUHAMMAD ILHAM Z
#NIM: 182102024

from flask import Flask
from flask_restful import Resource, Api
from mhs import students

app = Flask(__name__)
api = Api(app)



class Student(Resource): 
    def get(self, name):
        for stds in students:
        	if stds['name'] == name:
        		return stds
        return{'Students':'None'}, 404		

class StudentList(Resource):
    def get(self):
       return{'Students':students}

class Course(Resource):
    def get(self, name):
        for stds in students:
        	if stds['name'] == name:
        		return stds['courses']
        return{'Students':'None'}, 404	


api.add_resource(Student, '/student/<string:name>')
api.add_resource(StudentList, '/students')
api.add_resource(Course, '/course/<string:name>')

app.run(port=5000, debug=True)
