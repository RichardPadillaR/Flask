from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.trees import Trees
from flask_app.models.users import Users

@app.route('/dashboard', methods = ['GET' ,'POST'])          
def get_all_trees():
    if session['user_id'] == None:
        flash('Please Log in first!')
        return redirect('/')
    else :
        data = {
        'id' : session['user_id']
    } 
    user_info = Users.get_one_user(data)
    all_users_trees = Users.get_user_trees(data)
    all_trees = Trees.all_trees()
    return render_template("reported_trees.html",all_users_trees = all_users_trees, all_trees = all_trees,  user_info = user_info)

@app.route('/new/tree', methods = ['GET'])
def new_tree_data():
    if session['user_id'] == None:
        flash('Please Log in first!')
        return redirect('/')
    data = {
        'id' : session['user_id']
    } 
    user_info = Users.get_one_user(data)
    return render_template("report_tree.html", user_info = user_info)

@app.route('/new/tree', methods = ['POST'])
def new_tree():
    if session['user_id'] == None:
        flash('Please Log in first!')
        return redirect('/')
    else:
        request.method == "POST"
        tree_info = {
            'species' : request.form["species"],
            'location' : request.form["location"],
            'reason' : request.form["reason"],
            'date_planted' : request.form["date_planted"],
            'users_id' : session['user_id'],
        }
        if not Trees.validate_tree(tree_info):
            return redirect('/new/tree')
        else: 
            Trees.create_new_tree(tree_info)
    return redirect('/dashboard')

@app.route("/tree/edit/<int:reported_trees_id>", methods = ['GET'])
def show_reported_tree(reported_trees_id):
    if session['user_id'] == None:
        flash('Please Log in first!')
        return redirect('/')
    else:
        tree_id = {
        'id' : reported_trees_id
    } 
    user_id = {
        'id' : session['user_id']
    } 
    user_info = Users.get_one_user(user_id)
    reported_trees = Trees.get_one_tree(tree_id)
    return render_template("edit_tree.html", reported_trees = reported_trees, user_info = user_info)

@app.route('/tree/edit/<int:reported_trees_id>', methods = ['POST'])
def update_tree(reported_trees_id):
    if session['user_id'] == None:
        flash('Please Log in first!')
        return redirect('/')
    else:
        request.method == "POST"
        tree_info = {
            'id' : reported_trees_id,
            'species' : request.form["species"],
            'location' : request.form["location"],
            'reason' : request.form["reason"],
            'date_planted' : request.form["date_planted"],
            'Users_id' : session['user_id'],
        }
        if not Trees.validate_tree(tree_info):
            return redirect(request.url)
        else: 
            Trees.update_tree(tree_info)
            return redirect('/dashboard')

@app.route("/tree/show/<int:reported_trees_id>", methods = ['GET'])
def show_reported_tree_info(reported_trees_id):
    if session['user_id'] == None:
        flash('Please Log in first!')
        return redirect('/')
    else:
        tree_id = {
        'id' : reported_trees_id,
        }
    user_id = {
        'id' : session['user_id']
        }
    user_info = Users.get_one_user(user_id)
    tree_info = Trees.get_one_tree(tree_id)
    return render_template("show_tree.html", tree_info = tree_info, user_info = user_info)

@app.route('/user/account', methods = ['GET'])
def user_trees():
    if session['user_id'] == None:
        flash('Please Log in first!')
        return redirect('/')
    data = {
        'id' : session['user_id']
    } 
    user_info = Users.get_one_user(data)
    users_trees = Trees.get_user_trees(data)
    return render_template("manage_trees.html", user_info = user_info, users_trees = users_trees)


@app.route('/delete_tree/<int:reported_tree_id>')
def delete_tree(reported_tree_id):
    if session['user_id'] == None:
        flash('Please Log in first!')
        return redirect('/')
    else:
        data = {
        "id": reported_tree_id
        }
        Trees.delete_tree(data)
        return redirect("/dashboard")