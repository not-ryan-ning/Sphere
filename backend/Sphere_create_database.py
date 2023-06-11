#Sphere_create_database

import mysql.connector


mydb = mysql.connector.connect(host="localhost",\
                               user="root",\
                               passwd="password")
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Sphere7")
mycursor.execute("USE Sphere7")

student_table = "CREATE TABLE IF NOT EXISTS student " \
                "(username varchar(20) Primary key, " \
                "password varchar(20), " \
                "name varchar(30), " \
                "age int(2), " \
                "email varchar(30), " \
                "grade int(2), " \
                "subject varchar(10), " \
                "days varchar(7), " \
                "hours int(2), " \
                "particular_topics varchar(100), " \
                "proficiency int(1))"

mycursor.execute(student_table)

tutor_table = "CREATE TABLE IF NOT EXISTS tutor " \
              "(username varchar(20) PRIMARY KEY, " \
              "password varchar(20), " \
              "name varchar(30), " \
              "age int(2), " \
              "email varchar(30), " \
              "grade int(2), " \
              "subject varchar(10), " \
              "days varchar(7), " \
              "hours int(2), " \
              "particular_topics varchar(100), " \
              "cover_letter varchar(100), " \
              "cover_letter_pdf BLOB, " \
              "resume varchar(100), " \
              "resume_pdf BLOB)"

mycursor.execute(tutor_table)

class User():
    """A class of users, which can be either students or tutors.
    This is an abstract class."""

    username: str
    pwd: str
    name: str
    age: int
    email: str
    grade: int
    subject: str
    days: str
    hours: int
    particular_topics: str

    def __init__(self,
                 username: str,
                 pwd: str,
                 name: str,
                 age: int,
                 email: str,
                 grade: int,
                 subject: str,
                 days: str,
                 hours: int,
                 particular_topics: str) -> None:
        """Initialize this event with the given timestamp."""
        self.username = username
        self.pwd = pwd
        self.name = name
        self.age = age
        self.email = email
        self.grade = grade
        self.subject = subject
        self.hours = hours
        self.days = days
        self.particular_topics = particular_topics

class Student(User):
    """A class of students, which is a subclass of the User class."""
    proficiency: int

    def __init__(self,
                 username: str,
                 pwd: str,
                 name: str,
                 age: int,
                 email: str,
                 grade: int,
                 subject: str,
                 days: str,
                 hours: int,
                 particular_topics: str,
                 proficiency: int) -> None:
        """Initialises the Student class."""
        User.__init__(self=self,
                      username=username,
                      pwd=pwd,
                      name=name,
                      age=age,
                      email=email,
                      grade=grade,
                      subject=subject,
                      days=days,
                      hours=hours,
                      particular_topics=particular_topics)
        self.proficiency = proficiency

    def input_row(self) -> None:
        """Inputs the username of the user into the db."""
        sql = "INSERT INTO student (username, password, name, age, email, grade, subject, days, hours, " \
              "particular_topics, proficiency) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.username, self.pwd, self.name, self.age, self.email, self.grade,
               self.subject, self.days, self.hours, self.particular_topics, self.proficiency)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

class Tutor(User):
    """A class of tutors, which is a subclass of the User class."""
    cover_letter: str
    resume: str

    def __init__(self,
                 username: str,
                 pwd: str,
                 name: str,
                 age: int,
                 email: str,
                 grade: int,
                 subject: str,
                 days: str,
                 hours: int,
                 particular_topics: str,
                 cover_letter: str,
                 resume: str) -> None:
        """Initialises the Student class."""
        User.__init__(self=self,
                      username=username,
                      pwd=pwd,
                      name=name,
                      age=age,
                      email=email,
                      grade=grade,
                      subject=subject,
                      days=days,
                      hours=hours,
                      particular_topics=particular_topics)
        self.cover_letter = cover_letter
        self.resume = resume
        with open(cover_letter, 'rb') as file:
            self.cover_letter_pdf = file.read()
        with open(resume, 'rb') as file:
            self.resume_pdf = file.read()

    def input_row(self) -> None:
        """Inputs the username of the user into the db."""
        sql = "INSERT INTO student (username, password, name, age, email, grade, subject, days, hours, " \
              "particular_topics, cover_letter, cover_letter_pdf, resume, resume_pdf) " \
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.username, self.pwd, self.name, self.age, self.email, self.grade,
               self.subject, self.days, self.hours, self.particular_topics, self.cover_letter, self.cover_letter_pdf,
               self.resume, self.resume_pdf)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    # def input_row(self,
    #               username: str,
    #               pwd: str,
    #               name: str,
    #               age: int,
    #               email: str,
    #               grade: int,
    #               subject: str,
    #               days: str,
    #               hours: int,
    #               cover_letter: str,
    #               cover_letter_pdf: bytes,
    #               resume: str,
    #               resume_pdf: bytes) -> None:
    #     """Inputs the username of the user into the db."""
    #     sql = "INSERT INTO student (username, pwd, name, age, email, grade, subject, days, hours, " \
    #           "particular_topic, cover_letter, cover_letter_pdf, resume, resume_pdf) " \
    #           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #     val = (username, pwd, name, age, email, grade,
    #            subject, days, hours, cover_letter, cover_letter_pdf,
    #            resume, resume_pdf)
    #     mycursor.execute(sql, val)
    #     mydb.commit()
    #     print(mycursor.rowcount, "record inserted.")
