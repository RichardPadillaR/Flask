from flask_app import app, bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.users import Users  

@app.route('/')          
def all_users():
    users = Users.get_all_users()
    return render_template("users_login.html", all_users = users)

@app.route('/', methods = ['POST'])
def create_users():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    if len('password') < 8:
        flash("Password needs to be at least 8 characters.")
        return redirect('/')
    elif request.method == "POST":
        user_info = {
            'first_name' : request.form["first_name"],
            'last_name' : request.form["last_name"],
            'email' : request.form["email"],
            'password' : pw_hash,
        }
        if not Users.validate_order(user_info):
            return redirect('/')
        else: 
            user_id = Users.create_new_user(user_info)
            session['user_id'] = user_id
    return redirect('/')

@app.route('/login_user', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user_in_db = Users.get_user_email(data)
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

@app.route('/dashboard')
def user_data():
    data = {
        'id' : session['user_id']
    } 
    user_info = Users.get_one_user(data)
    return render_template("user_info.html", user_info = user_info)

@app.route('/logout')
def user_logout():
    session.pop('user_id')
    return redirect('/')