from flask import Flask, render_template, request, redirect, url_for, send_file
import mysql.connector as mysql
import hashlib
from tasks import compute_forces
from io import BytesIO
import sys
from time import sleep

app = Flask(__name__, template_folder = "templates")

# Connect to db
db = mysql.connect(host = "db", user = "root", passwd = "12345",
                   database = "results", buffered = True, autocommit = True)
cursor = db.cursor()

# Make a new table test for experimentation
cursor.execute("DROP TABLE IF EXISTS test;")
cursor.execute("CREATE TABLE test(hash TEXT, file BLOB);")

@app.route('/')
def index():
    return(render_template("index.html"))


# Saves the received file from user to the database
@app.route('/upload', methods = ['POST'])
def uppload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file_to_upload'].read()
        hash_value = hashlib.sha256(uploaded_file).hexdigest()
    return(redirect(url_for('result', hash_value = hash_value)))


# Download file with forces
@app.route('/result/<hash_value>', methods = ['GET'])
def result(hash_value):
    # Check if the result is already in the database
    sql_query = f'SELECT * FROM test WHERE hash = "{hash_value}";'
    cursor.execute(sql_query)
    row = cursor.fetchone()
    if (row is not None):
        file = BytesIO(row[1])
        return(send_file(file, attachment_filename = "res_saved.txt", as_attachment = True))

    task = compute_forces.delay()

    # Waiting for the task to complete
    while True:
        sleep(1)
        if task.ready():
            result = task.get()
            break

    sql_query_new = "INSERT INTO test(hash, file) VALUES(%s, %s)"

    # Save result in local directory
    file_name = "res.txt"
    file_ = open(file_name, 'w+')
    file_.write(result)
    file_.write("\n")
    file_.close()
    file_to_save = open(file_name, "r").read()
    blob_tuple = (hash_value, file_to_save)
    cursor.execute(sql_query_new, blob_tuple)

    return(send_file(file_name, attachment_filename=file_name, as_attachment = True))
 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
