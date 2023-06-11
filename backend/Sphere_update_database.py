#Sphere_update_database

import mysql.connector
from backend import Sphere_create_database as s1
import smtplib
from email.mime.text import MIMEText
import requests
import json


mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                               passwd="password",
                               database="Sphere7")
mycursor = mydb.cursor()
mycursor.execute("USE Sphere7")


API_KEY = 'h3fhEidJXs4UZVuv5O2YBtfK04hKWtJATB8kCKuY'

def get_similarity_score(description1, description2) -> float:
    url = 'https://api.cohere.ai/v1/similarity'
    headers = {'Authorization': f'Token {API_KEY}', 'Content-Type': 'application/json'}
    data = {'text1': description1, 'text2': description2}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()['score']
    else:
        return 0.0

def matched(student: s1.Student, tutor: s1.Tutor) -> bool:
    if student.subject == tutor.subject and student.hours <= tutor.hours \
            and get_similarity_score(student.particular_topics, tutor.particular_topics) > 0:
        return True
    return False

def make_class_student(info_tuple: tuple) -> s1.Student:
    return s1.Student(username=info_tuple[0],
                      pwd=info_tuple[1],
                      name=info_tuple[2],
                      age=info_tuple[3],
                      email=info_tuple[4],
                      grade=info_tuple[5],
                      subject=info_tuple[6],
                      days=info_tuple[7],
                      hours=info_tuple[8],
                      particular_topics=info_tuple[9],
                      proficiency=info_tuple[10])

def make_class_tutor(info_tuple: tuple) -> s1.Tutor:
    return s1.Tutor(username=info_tuple[0],
                    pwd=info_tuple[1],
                    name=info_tuple[2],
                    age=info_tuple[3],
                    email=info_tuple[4],
                    grade=info_tuple[5],
                    subject=info_tuple[6],
                    days=info_tuple[7],
                    hours=info_tuple[8],
                    particular_topics=info_tuple[9],
                    cover_letter=info_tuple[10],
                    resume=info_tuple[12])

mycursor.execute("SELECT * FROM student")
student_list = mycursor.fetchall()

mycursor.execute("SELECT * FROM tutor")
tutor_list = mycursor.fetchall()

for student in student_list:
    for tutor in tutor_list:
        if matched(make_class_student(student), make_class_tutor(tutor)):
            # SENDING MAIL TO STUDENT
            # Set up the SMTP connection
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            smtp_username = "sphere.edu.circle@gmail.com"  # Replace with your Gmail address
            smtp_password = "lbimngdouyxyhsvf"  # Replace with your generated App password
            smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
            smtp_connection.ehlo()
            smtp_connection.starttls()
            smtp_connection.login(smtp_username, smtp_password)

            # Set up the email message
            from_email = "sphere.edu.circle@gmail.com"  # Replace with your Gmail address
            to_email = student[4]  # Replace with the email address of the recipient
            subject = "You have been matched with a Tutor!"
            message_body = f"Hello {student[2]},\n\nYou have been matched with {tutor[2]}.\n\nBest, \nSphere Education"

            message = MIMEText(message_body)
            message["From"] = from_email
            message["To"] = to_email
            message["Subject"] = subject

            # Send the email
            smtp_connection.sendmail(from_email, to_email, message.as_string())

            # Close the SMTP connection
            smtp_connection.quit()

            # SENDING MAIL TO TUTOR
            # Set up the SMTP connection
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            smtp_username = "sphere.edu.circle@gmail.com"  # Replace with your Gmail address
            smtp_password = "lbimngdouyxyhsvf"  # Replace with your generated App password
            smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
            smtp_connection.ehlo()
            smtp_connection.starttls()
            smtp_connection.login(smtp_username, smtp_password)

            # Set up the email message
            from_email = "sphere.edu.circle@gmail.com"  # Replace with your Gmail address
            to_email = tutor[4]  # Replace with the email address of the recipient
            subject = "You have been matched with a Student!"
            message_body = f"Hello {tutor[2]},\n\nYou have been matched with {student[2]}.\n\nBest, \nSphere Education"

            message = MIMEText(message_body)
            message["From"] = from_email
            message["To"] = to_email
            message["Subject"] = subject

            # Send the email
            smtp_connection.sendmail(from_email, to_email, message.as_string())

            # Close the SMTP connection
            smtp_connection.quit()
