from flask import Flask, redirect, url_for
from  flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_func():
    name = 'Naor Pinto'
    return render_template('home.html', name=name)


@app.route('/cv')
def cv_func():
    return render_template('cv1.html')


@app.route('/contactMe')
def contact_func():
    return render_template('cv2.html')


@app.route('/assignment8')
def assignment8_func():
    name = 'Naor Pinto'
    return render_template('assignment8.html',
                           name=name,
                           hobbies=('Travel', 'Music', 'Sneakers', 'Sport'),
                           sports=['Basketball', 'Gym', 'Ping Pong', 'Football'])


@app.route('/academic')
def academic_func():
    name = 'Naor Pinto'
    return render_template('academic_info.html',
                           name=name,
                           Technical_skills=('SQL', 'Tableau', 'Java', 'Excel'))


if __name__ == '__main__':
    app.run(debug=True)
