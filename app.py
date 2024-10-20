from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message='')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex = request.form['regex']
    matches = re.findall(regex, test_string)
    
    if matches:
        message = f"Matches found: {', '.join(matches)}"
    else:
        message = "No matches found."
        
    return render_template('index.html', message=message)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        message = f"'{email}' is a valid email address."
    else:
        message = f"'{email}' is not a valid email address."
        
    return render_template('index.html', message=message)

#if __name__ == '__main__':
 #   app.run(debug=True)
