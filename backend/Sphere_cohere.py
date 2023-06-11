#Sphere_cohere

import mysql.connector
import Sphere_create_database as s1
import smtplib
from email.mime.text import MIMEText
import json
import requests
from bs4 import BeautifulSoup

response = requests.get('http://localhost:63342/NSBE/frontend/main.html?_ijt=uo17gsi11a3qq68gfsa16p4auu&_ij_reload=RELOAD_ON_SAVE')

# Extract HTML content of webpage
html_content = response.content

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the form on the webpage and extract the relevant data
form = soup.find('form')
username = ''

for input_tag in form.find_all('input'):
    username = input_tag.get('username')

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

similarity_score_set = set()
score_list = []
student_1 = [student for student in student_list if student[0] == username][0]

for student2 in student_list:
    similarity_score_set.add([student2[0], get_similarity_score(student_1[9], student2[9])])
    score_list.append(get_similarity_score(student_1[9], student2[9]))

greatest_list = [my_list for my_list in similarity_score_set if my_list[2] == max(score_list)][0]
student_2 = [student for student in student_list if student[0] == greatest_list[0]][0]
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
to_email = student_1[4]  # Replace with the email address of the recipient
subject = "You have been matched with another student!"
message_body = f"Hello {student_1[2]},\n\nYou have been matched with {student_2[2]}.\n\nBest, \nSphere Education"

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
to_email = student_2[4]  # Replace with the email address of the recipient
subject = "You have been matched with a Student!"
message_body = f"Hello {student_2[2]},\n\nYou have been matched with a {student_1[2]}.\n\nBest, \nSphere Education"

message = MIMEText(message_body)
message["From"] = from_email
message["To"] = to_email
message["Subject"] = subject

# Send the email
smtp_connection.sendmail(from_email, to_email, message.as_string())

# Close the SMTP connection
smtp_connection.quit()
