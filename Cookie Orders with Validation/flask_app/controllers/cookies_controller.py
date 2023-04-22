from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.cookies import Cookies

@app.route('/cookies', methods = ['GET' ,'POST'])          
def all_cookie_orders():
    cookies = Cookies.get_all_cookies()
    return render_template("cookies.html", all_cookies = cookies)


@app.route('/create_cookie_order', methods = ['GET'])
def cookies_form():
    return render_template("create_cookies.html")

@app.route('/create_cookie_order', methods = ['POST'])
def create_cookie_order():
    if request.method == "POST":
        customer_info = {
            'customer_name' : request.form["customer_name"],
            'cookie_type' : request.form["cookie_type"],
            'number_of_boxes' : request.form["number_of_boxes"],
        }
        if not Cookies.validate_order(customer_info):
            return redirect('/create_cookie_order')
        else: 
            Cookies.create_new_order(customer_info)
    return redirect('/cookies')

@app.route("/cookies/edit/<int:cookie_orders_id>", methods = ['GET'])
def show_cookie_order(cookie_orders_id):
    data = {
        'id' : cookie_orders_id,
    }
    edit_cookie = Cookies.get_one_cookie(data)
    return render_template("edit_cookie.html", edit_cookie = edit_cookie)

@app.route('/cookies/edit/<int:cookie_orders_id>', methods = ['POST'])
def update_cookie_order(cookie_orders_id):
    if request.method == "POST":
        customer_info = {
            'id' : cookie_orders_id,
            'customer_name' : request.form["customer_name"],
            'cookie_type' : request.form["cookie_type"],
            'number_of_boxes' : request.form["number_of_boxes"],
        }
        if not Cookies.validate_order(customer_info):
            return redirect('/cookies/edit/<int:cookie_orders_id>')
        else: 
            Cookies.update_cookie(customer_info)
    return redirect('/cookies')