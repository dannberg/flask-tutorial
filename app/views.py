from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Dann'}
	posts = [ #fake array of posts
			{
					'author': {'nickname': 'John'},
					'body': 'Beautiful day in New York!'
			},
			{
					'author': {'nickname': 'Susan'},
					'body': 'The movie Dogville was so cool!'
			},
			{
					'author': {'nickname': 'Avital'},
					'body': 'I just want to dance.'
			}
	]
	return render_template('index.html',
													title='Home',
													user=user,
													posts=posts)
