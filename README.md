# Basic Flask App with login - SQLite3 Backend

"I am using this to practice learning python"



The app is a simple user authentication system, so far using:
- **Flask** - to serve the app
- **SQLite** - as the back end database
- **hashlib** - for password hashing. 

Below, you'll find information about the structure of your app, its functionality, and some notes on improvements.

## **SQL Injection Prevention Practice:** 

The original code included an SQL injection vulnerability. This has been fixed by using parameterised queries. This is wihin the searchUser function and has been highlighted using code comments.

## Installation

**Clone the Repository:**

`git clone https://github.com/JL-Sec/Basic-Flask-App-with-Login.git`

`cd Basic-Flask-App-With-Login`


**Install Dependencies:**

`pip install Flask`

## Usage

**Run the Application:**

`python app.py`

**Access the App:**

Open your web browser and go to http://127.0.0.1:5000/.

Navigate to the login page by visiting http://127.0.0.1:5000/loginn.

### Test Authentication:
- Use the provided login form to enter a username and password. The sqlite database contains one user:
    - username: `jack123` password: `Password`

- If the login is successful, you will see "User Logged In"; otherwise, you will see "Access Denied."

## Features

- **User Authentication:** The app allows users to log in with a username and password.

- **SQLite Database:** User information is stored in an SQLite database (test.db).
    Password Hashing: Passwords are hashed using the MD5 algorithm before storage.

## Structure

**app.py:** The main Flask application file.

**templates/:** Contains HTML templates for rendering pages.

**data/:** Holds the SQLite database file (test.db).

**logging/:** Stores application logs (app.log).

## Future Developments

- Register new user functionality
- Session management - Add user cookies
- Rate limiting for brute force attacks
- Password recovery functionality






