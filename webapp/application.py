from flask import Flask, render_template, request
import re

application = Flask(__name__)

def validate_regex(input_string, regex_pattern):
    
    matches = re.findall(regex_pattern, input_string)
    return matches

def validate_gmail(email_address):
    gmail_pattern = r'^[a-zA-Z0-9._%+-]+@gmail.com$'
    if re.match(gmail_pattern, email_address):
        return "Valid Gmail address."
    else:
        return "Not a valid Gmail address."
    

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/validate', methods=['POST'])
def validate():
    input_string = request.form['inputString']
    regex_pattern = request.form['regexPattern']

   
    matched_results = validate_regex(input_string, regex_pattern)

    return render_template('result.html', input_string=input_string, regex_pattern=regex_pattern, matched_results=matched_results)


@application.route('/validate-gmail', methods=['POST'])
def validate_gmail_address():
    email_address = request.form['emailAddress']

   
    gmail_result = validate_gmail(email_address)

    return render_template('result2.html', input_string="", regex_pattern="", matched_results=[], gmail_result=gmail_result,email_address=email_address)

if __name__ == "__main__":
    application.run(debug=True,host="0.0.0.0")
