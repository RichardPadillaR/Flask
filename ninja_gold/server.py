from flask import Flask, render_template, session, request, redirect
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key = "archon"   

@app.route('/')          
def index():
    if "gold" not in session:
        session['gold'] = 0
    if "activities" not in session:
        session['activities'] = []
    activities = session["activities"]
    reversed_activities = []
    for activity in activities:
        reversed_activities.insert(0, activity)
    return render_template('gold.html', activities = reversed_activities)

@app.route('/process_money', methods=["POST"])          
def process_money():
    location = request.form["location"]
    activities = session["activities"]
    if location == "Farm":
        earnedGold = random.randint(10,20)
    elif location == "Cave":
        earnedGold = random.randint(5,10)
    elif location == "House":
        earnedGold = random.randint(2,5)
    elif location == "Casino":
        earnedGold = random.randint(-50,50)
    activities.append({
        "activity_name": location,
        "gold": earnedGold,
        "date": datetime.now()
        })
    session["gold"] += earnedGold
    session["activities"] = activities
    return redirect("/")

@app.route('/reset', methods = ["POST"])          
def reset_points():
    if "activities" in session:
        session["activities"] = []
    if "gold" in session:
        session["gold"] = 0
    return redirect("/")

if __name__=="__main__":   
    app.run(debug=True, port = 5100) 