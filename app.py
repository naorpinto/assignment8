import app as app
from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session
from flask import jsonify
import requests
from interact_with_DB import interact_db


app = Flask(__name__)
app.secret_key = '123'


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
                                          'user4': {'nickname': 'ariel1', 'name': 'Ariel', 'email': 'ariel@gmail.com'},
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


# assignment10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)


@app.route('/insert_user', methods=['POST'])
def insert_user_func():
    #get the data
    nickname = request.form['nickname']
    name = request.form['name']
    email = request.form['email']

    #insert to DB
    query = "INSERT INTO users(nickname, name, email) VALUES ('%s','%s','%s');" % (nickname, name, email)
    interact_db(query=query, query_type='commit')

    #come back to assignment10
    return redirect('/assignment10')


@app.route('/delete_user', methods=['POST'])
def delete_user_func():
    user_nickname = request.form['D_nickname']
    query = "DELETE FROM users WHERE nickname='%s';" % user_nickname
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')


@app.route('/update_user', methods=['POST'])
def update_user_func():
    u_nickname = request.form['user_nickname']
    new_email = request.form['user_email']
    query = "UPDATE users SET email='%s' WHERE nickname='%s';" % (new_email, u_nickname)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')


@app.route('/assignment11/users')
def assignment11_users_func():
    query = ' select * from users;'
    users = interact_db(query=query, query_type='fetch')
    response = jsonify(users)
    return response


def get_user(user_num):
    res = requests.get(f'https://reqres.in/api/users/{user_num}')
    res = res.json()
    return res


@app.route('/assignment11/outer_source')
def assignment11_outer_source_func():
    user_num = 3
    if "number" in request.args:
        user_num = int(request.args['number'])
    the_user = get_user(user_num)
    return render_template('assignment11_outerSource.html', User=the_user)


@app.route('/assignment12/restapi_users', defaults={'user_id': 5})
@app.route('/assignment12/restapi_users/<int:user_id>')
def assignment12_func(user_id):
    query = ' select * from users where id=%s;' % user_id
    user = interact_db(query=query, query_type='fetch')
    if len(user) == 0:
        return_dic = { 'status': 'Failed', 'message': 'This  was not found'}
    else:
        return_dic = {'status': 'Success', 'id': user[0].id, 'name': user[0].name, 'email': user[0].email,
                       'nickname': user[0].nickname}
    return jsonify(return_dic)


if __name__ == '__main__':
    app.run(debug=True)
