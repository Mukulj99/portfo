
from hashlib import new
from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def page_name(page_name):
    return render_template(f"{page_name}")


def write_database_text(argument):
    with open('database.txt', 'a') as file:
        email = argument['email']
        subject = argument['subject']
        message = argument['message']

        file.write(f'\n{email},{subject},{message}')


def write_database_csv(argument):
    with open('database.csv', 'a', newline='') as database:
        email = argument['email']
        subject = argument['subject']
        message = argument['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_database_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'data not saved in database, try again in sometime'
    else:
        return 'Something went wrong! Try again'
