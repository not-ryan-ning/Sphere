#Sphere_3

import mysql.connector
from backend import Sphere_create_database
import requests
from bs4 import BeautifulSoup
from flask import Flask, request

mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                               passwd="password",
                               database="Sphere7")
mycursor = mydb.cursor()
mycursor.execute("USE Sphere7")

app = Flask(__name__)

@app.route('/student-form', methods=['POST'])
def student_form():
    data = request.get_json()
    username = data['username']
    pwd = data['pwd']
    name = data['name']
    age = data['age']
    email = data['email']
    grade = data['grade']
    subject = data['subject']
    days = data['days']
    hours = data['hours']
    particular_topics = data['particular_topics']
    proficiency = data['proficiency']

    return Sphere_create_database.Student(username=username,
                                          pwd=pwd,
                                          name=name,
                                          age=int(age),
                                          email=email,
                                          grade=int(grade),
                                          subject=subject,
                                          days=process_days(days),
                                          hours=int(hours),
                                          particular_topics=particular_topics,
                                          proficiency=int(proficiency))

@app.route('/student-form', methods=['POST'])
def tutor_form():
    data = request.get_json()
    username = data['username']
    pwd = data['pwd']
    name = data['name']
    age = data['age']
    email = data['email']
    grade = data['grade']
    subject = data['subject']
    days = data['days']
    hours = data['hours']
    particular_topics = data['particular_topics']
    cover_letter = data['cover_letter']
    resume = data['resume']

    return Sphere_create_database.Tutor(username=username,
                                        pwd=pwd,
                                        name=name,
                                        age=int(age),
                                        email=email,
                                        grade=int(grade),
                                        subject=subject,
                                        days=process_days(days),
                                        hours=int(hours),
                                        particular_topics=particular_topics,
                                        cover_letter=cover_letter,
                                        resume=resume)




    # # Send HTTP request to website containing form
    # response = requests.get(url)
    #
    # # Extract HTML content of webpage
    # html_content = response.content
    #
    # # Parse HTML content with BeautifulSoup
    # soup = BeautifulSoup(html_content, 'html.parser')
    #
    # # Find the form on the webpage and extract the relevant data
    # form = soup.find('form')
    # checkbox_values = []
    # for input_tag in form.find_all('input'):
    #     # Check if input element is a checkbox
    #     if input_tag.get('type') == 'checkbox':
    #         # Check if checkbox is checked
    #         if input_tag.get('checked') is not None:
    #             checkbox_values.append(input_tag.get('value'))
    #
    # if student:
    #     for input_tag in form.find_all('input'):
    #         username = input_tag.get('username')
    #         pwd = input_tag.get('pwd')
    #         name = input_tag.get('name')
    #         age = input_tag.get('age')
    #         email = input_tag.get('email')
    #         grade = input_tag.get('grade')
    #         subject = input_tag.get('subject')
    #         days = checkbox_values
    #         hours = input_tag.get('hours')
    #         particular_topics = input_tag.get('particular_topics')
    #         proficiency = input_tag.get('proficiency')
    #         return Sphere_create_database.Student(username=username,
    #                                               pwd=pwd,
    #                                               name=name,
    #                                               age=age,
    #                                               email=email,
    #                                               grade=grade,
    #                                               subject=subject,
    #                                               days=process_days(days),
    #                                               hours=hours,
    #                                               particular_topics=particular_topics,
    #                                               proficiency=proficiency)
    # else:
    #     for input_tag in form.find_all('input'):
    #         username = input_tag.get('username')
    #         pwd = input_tag.get('pwd')
    #         name = input_tag.get('name')
    #         age = input_tag.get('age')
    #         email = input_tag.get('email')
    #         grade = input_tag.get('grade')
    #         subject = input_tag.get('subject')
    #         days = checkbox_values
    #         hours = input_tag.get('hours')
    #         particular_topics = input_tag.get('particular_topics')
    #         cover_letter = input_tag.get('cover_letter')
    #         resume = input_tag.get('resume')
    #         return Sphere_create_database.Tutor(username=username,
    #                                             pwd=pwd,
    #                                             name=name,
    #                                             age=age,
    #                                             email=email,
    #                                             grade=grade,
    #                                             subject=subject,
    #                                             days=process_days(days),
    #                                             hours=hours,
    #                                             particular_topics=particular_topics,
    #                                             cover_letter=cover_letter,
    #                                             resume=resume)

def process_days(days: list) -> str:
    my_str = ''
    for day in days:
        if day.lower() == 'monday':
            my_str += '1'
        elif day.lower() == 'tuesday':
            my_str += '2'
        elif day.lower() == 'wednesday':
            my_str += '3'
        elif day.lower() == 'thursday':
            my_str += '4'
        elif day.lower() == 'friday':
            my_str += '5'
        elif day.lower() == 'saturday':
            my_str += '6'
        else:
            my_str += '7'
    return my_str

@app.route('/')
def index():
    student1 = student_form()
    student1.input_row()

    tutor1 = tutor_form()
    tutor1.input_row()

index()


# app = Flask(__name__)
#
#
# @app.route('/student-form', methods=['POST'])
# def submit_form():
#     username = request.form['username']
#     pwd = request.form['pwd']
#     name = request.form['name']
#     age = request.form['age']
#     email = request.form['email']
#     grade = request.form['grade']
#     subject = request.form['subject']
#     days = request.form['days']
#     hours = request.form['hours']
#     particular_topic = request.form['particular_topic']
#     proficiency = request.form['proficiency']
#
#     # Process the form data as needed (e.g., store in a database, perform calculations, etc.)
#
#
# @app.route('/tutor-form', methods=['POST'])
# def submit_form():
#     username = request.form['username']
#     pwd = request.form['pwd']
#     name = request.form['name']
#     age = request.form['age']
#     email = request.form['email']
#     grade = request.form['grade']
#     subject = request.form['subject']
#     days = request.form['days']
#     hours = request.form['hours']
#     particular_topic = request.form['particular_topic']
#     cover_letter = request.form['cover_letter']
#     resume = request.form['resume']

#     # Process the form data as needed (e.g., store in a database, perform calculations, etc.)
#
#

if __name__ == '__main__':
    app.run()
