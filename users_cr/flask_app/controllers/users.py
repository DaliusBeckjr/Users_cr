from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user

@app.route('/')
def root():
    return redirect("/users/dashboard")

@app.route('/users/dashboard')
def users_dashboard():
    # import user - to call method you need to use lowercase
    # before entering the class
    # equal to a var that is doing a method call to our get_all user(cls)
    # method
    users = user.User.get_all_users()
    # or users = User.get_all_users() for from user import User
    print(" ")
    print(users)
    print(" ")
    return render_template('users_dashboard.html', all_users=users)


@app.route('/users/show/<int:id>')
def show_user(id):
    # since this is the second way to do it we are putting the data 
    # dictionary here
    data={
        'id': id # key of id being = to the id coming from the URL
    }
    return render_template('show_user.html', one_user=user.User.get_one_user(data))


@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/create', methods=['POST'])
def create_user():
    data={
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    user.User.save_user(data)
    return redirect('/users/dashboard')