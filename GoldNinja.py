import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ninja'

@app.route('/')
def index():
	gold = 0
	return render_template('/index.html')

@app.route('/process_money', methods = ['POST'])
def money():
	if request.form['building'] == 'farm':
	session['farm'] = random.randrange(10, 20)
	gold += session['farm']

	if request.form['building'] == 'cave':
		session['farm'] = random.randrange(5, 10)
	gold += session['cave']

	

