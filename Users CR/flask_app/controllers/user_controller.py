from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.users import User

@app.route('/', methods = ['GET' ,'POST'])          
def all_users():
    users = User.get_all()
    return render_template("all_users.html", all_users = users)

@app.route('/users/<int:user_id>')
def user_info(user_id):
    data = {
        "id": user_id
    }
    user_data = User.get_one(data)
    return render_template("user_data.html", user = user_data)

@app.route('/edit_user/<int:user_id>/edit')
def edit_user(user_id):
    data = {
        "id": user_id
    }
    user_data = User.get_one(data)
    return render_template("edit_user_data.html", user = user_data)

@app.route('/edit_user/<int:user_id>/edit', methods = ["POST"])
def return_updated_info(user_id):
    data = {
        "id": user_id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.edit_user(data)
    return redirect('/')

@app.route('/delete_user/<int:user_id>')
def delete_current_user(user_id):
    data = {
        "id": user_id
    }
    User.delete(data)
    return redirect("/")

@app.route('/user_form')
def user_form():
    return render_template("create_user.html")

@app.route('/create_user', methods = ["GET", "POST"])
def create_user():
    if request.method == "POST":
        data = {
            'first_name' : request.form["first_name"],
            'last_name' : request.form["last_name"],
            'email' : request.form["email"]
        }
        User.save(data)
    return redirect('/')
