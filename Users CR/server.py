from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
from users import user  
@app.route('/', methods = ['GET' ,'POST'])          
def all_users():
    users = user.get_all()
    return render_template("all_users.html", all_users = users)

@app.route('/user_form')
def user_form():
    return render_template("create_user.html")

@app.route('/create_user', methods = ["GET","POST"])
def create_user():
    if request.method == "POST":
        data = {
            "first_name" : request.form["first_name"],
            "last_name" : request.form["last_name"],
            "email" : request.form["email"]
            }
        user.save(data)
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True, port = 5100) 