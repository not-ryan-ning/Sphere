# Sphere
**Technology has become a new form of social stratification.**

Sphere is a full-stack social platform that aims to make technology and education more accessible to underrepresented users.

This is done by matching **volunteer tutors** to grassroots, or **underrepresented students** based on analysing their needs and similarities using Cohere's **natural language processing** API.

On the Sphere platform, you can:
1. Sign up as a tutor or student, and get matched with the other based on similarities - an email is sent automatically from Sphere once a match has been formed.
3. Connect with other similar students in case of a lack of tutors. 

### Running the Program 
Download the files and run the **`main.html`** in the front-end folder.

### Technical Documentation
The **front-end** is constructed with **`HTML`**, **`CSS`**, and **`JavaScript`**.
- **`main.html`** contains the main window GUI.
- **`student_form.html`** contains the student sign up GUI.
- **`tutor_form.html`** contains the tutor sign up GUI.
- **`sphere_cohere.html`** contains the social platform GUI.
- **`styles.css`** contains the style sheet.
- **`app.js`** contains `JavaScript` code to pass user input to the backend to be stored in the `MySQL` database.

The **back-end** is constructed using **`SMPT`**, **`MySQL`**, **`BeautifulSoup`** and **`Cohere`**.
- **`Sphere_cohere.py`** parses user input from the front-end using `BeautifulSoup`. It also matches students using `Cohere` API's natural langauge processing capabilities. Lastly, it emails students and/or tutors in case of a match, using `SMTP`. 
- **`Sphere_create_database.py`** creates the `MySQL` database when the program is initialized.
- **`Sphere_update_database.py`** updates the `MySQL` database when a user inputs data. It also has matching and notification capabilities similar to `Sophere_cohere.py` file. 
- **`Sphere_use_database_to_input.py`** parses data from front-end using `BeautifulSoup` the *first time* any data is input. 
