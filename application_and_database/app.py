from flask import Flask, render_template, request, redirect, url_for
import mysql.connector as mysql


app = Flask(__name__, template_folder = "templates")

# Connect to db
db = mysql.connect(host = "localhost", user = "root", passwd = "12345", database = "results")
cursor = db.cursor()

# Make a new table test for experimentation
cursor.execute("DROP TABLE IF EXISTS test;")
cursor.execute("CREATE TABLE test(hash INT, file BLOB);")

@app.route('/')
def index():
    return(render_template("index.html"))

# Saves the received file from user to the database
@app.route('/upload', methods = ['POST'])
def uppload_file():
    print('here...')
    if request.method == 'POST':
        print(request.form.to_dict())
        print(list(request.files.values()))
        for uploaded_file in request.files.values(): 
            cursor = db.cursor()
            sql_query = "INSERT INTO test(hash, file) VALUES(%s,%s)"
            # Hashes will be unique, this in only for testing
            blob_tuple = (1, uploaded_file.read())
            cursor.execute(sql_query, blob_tuple)
            db.commit()
    return(redirect(url_for('index')))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
