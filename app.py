from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session


app = Flask(__name__)
app.secret_key='123'


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


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9_func():
    if request.method == 'GET':
        if 'search' in request.args:
            search_word = request.args['search']
            return render_template('assignment9.html', search_user=search_word,
                                   users={'user1': {'nickname': 'naor24', 'name': 'Naor', 'email': 'naor@gmail.com'},
                                          'user2': {'nickname': 'noam28', 'name': 'Noam', 'email': 'noam@gmail.com'},
                                          'user3': {'nickname': 'kobe8', 'name': 'Kobe', 'email': 'kobe@gmail.com'},
                                          'user4': {'nickname': 'ariel1','name': 'Ariel', 'email': 'ariel@gmail.com'},
                                          'user5': {'nickname': 'amit14', 'name': 'Amit', 'email': 'amit@gmail.com'}})
        return render_template('assignment9.html')

    if request.method == 'POST':
        username = request.form['username']
        nickname = request.form['nickname']
        session['username'] = username
        session['nickname'] = nickname
        return render_template('assignment9.html', u_name=username, u_nickname=nickname)


@app.route('/logout')
def logout_func():
    session['username'] = ''
    return redirect(url_for('assignment9_func'))


if __name__ == '__main__':
    app.run(debug=True)
