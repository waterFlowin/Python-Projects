import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	session['answer'] = ""
	session['number'] = random.randrange(1,101)
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
	guess = request.form['num']
	guess = int(guess)

	if guess < session['number']:
		session['answer'] = "Too Low"
	elif guess > session['number']:
		session['answer'] = "Too High"
	else:
		session['answer'] = str(guess) + " Got em."
		

	return render_template('index.html')

app.run(debug=True)