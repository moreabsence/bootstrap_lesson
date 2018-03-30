from flask import Flask, render_template, request

my_flask_app = Flask(__name__)


@my_flask_app.route('/')
def index():
	return render_template('index.html', title='Свежие новости')

@my_flask_app.route('/all/')
def all_news():
	return render_template('all_the_news.html')

@my_flask_app.route('/login/', methods=['POST'])
def login():
	return render_template('login.html', email=request.form.get('email'), password=request.form.get('pass'))

if __name__ =='__main__':
	my_flask_app.run(debug=True)