import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html', date=datetime.now())

@app.route('/sent', methods=['POST', 'GET'])
def message_sent():
	if request.method == 'POST':
		user_name = request.form['fullname']
		user_email = request.form['emailaddress']
		user_subject = request.form['subject']
		user_message = request.form['message']
		date = 'hello'

		email = EmailMessage()
		email['from'] = user_name
		email['to'] = 'evan@dennisons.ca'
		email['subject'] = f'Evan\'s Website ({user_email}): {user_subject}'
		email.set_content(user_message)

		with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
			smtp.ehlo()
			smtp.starttls()
			smtp.login('website.evandennison@gmail.com', 'R0bert2@@5')
			smtp.send_message(email)

		return render_template('sent.html', name=user_name, date=datetime.now())

	else:
		return 'something went wrong. try again'

#Start server by:

#1: $ . venv/bin/activate

#2: export FLASK_APP=server.py

#3: export FLASK_ENV=development

#4: flask run