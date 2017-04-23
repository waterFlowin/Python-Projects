import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'Secrets'

@app.route('/')
def index():
	if 'gold' not in session:
		session['gold'] = 0
	if 'log' not in session:
		session['log'] = [] #has to be an array?
	return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def add_gold():
	if request.form['place'] == 'Farm':
		newgold = random.randrange(10,21)
		session['gold'] += newgold
	elif request.form['place'] == 'Cave':
		newgold = random.randrange(5,11)
		session['gold'] += newgold
	elif request.form['place'] == 'House':
		newgold = random.randrange(2,6)
		session['gold'] += newgold
	elif request.form['place'] == 'Casino':
		newgold = random.randrange(-50,51)
		session['gold'] += newgold

	place = request.form['place']
	session['log'].append({'amount':newgold, 'place':place})

	if len(session['log']) > 5:
		session['log'] = session['log'][-5:]
		#copied this from group assignment. I don't fully understand [-5:] yet

	return redirect('/')

app.run(debug=True)