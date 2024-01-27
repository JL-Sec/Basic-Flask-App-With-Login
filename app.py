from flask import Flask, render_template, redirect, url_for, request, g
import sqlite3
import hashlib
import logging

# Configure logging
logging.basicConfig(filename='logging\\app.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


app = Flask(__name__)
db_storage = "data\\test.db"

# Function to get the database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(db_storage)
    return db

# Function to get the database cursor
def get_cursor():
    db = get_db()
    return db.cursor()

# Function to search for users:
def searchUser(searchName, searchPassword):
    try:
        cursor = get_cursor()
        hashedPassword = hashlib.md5(searchPassword.encode()).hexdigest()


############################################ --- The following is SQL injectable --- ###########################################################
        
        # res = cursor.execute(f"SELECT username, password FROM users WHERE username='{searchName}' AND password='{hashedPassword}'")
        # result = cursor.fetchall()

############################################################# Fixed Below #####################################################################
        
        query ="SELECT username, password FROM users WHERE username=? AND password=?"
        cursor.execute(query, (searchName,hashedPassword))
        result = cursor.fetchall()       

############################################################################################################################################### 

        if result:
            data = result[0]
            print(data[0], data[1])
            return True
        else:
            print('Invalid Login')
            return False

    except Exception as e:
        logging.error(f'Error: {e}')
        return False
    
    finally:
        if cursor:
            cursor.close()

@app.route('/loginn', methods=['POST', 'GET'])
def login2():
    error = None
    if request.method == 'POST':
        # Pulling variables from form
        username = request.form.get("username")
        password = request.form.get("password")
        print(username, password)
        y = searchUser(username, password)

        if y:
            return "User Logged In"  # render a template
        else:
            return "Access Denied"  # render a template
    else:
        return render_template('login.html')  # render a template     

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/super_secret')
def super_secret():
    return "Flag0987youwin!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
