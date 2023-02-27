from flask import Flask ,render_template, session, redirect
app = Flask(__name__)
app.secret_key = "arhcon"

@app.route('/')
def site_visits():
    if 'visits' not in session:
        session['visits'] = 0
    session['visits'] +=1
    return render_template("index.html", visits = session['visits'])

@app.route('/plus_2')
def plus_2():
    session['visits'] +=2
    return render_template("index.html", visits = session['visits'])

@app.route('/reset')
def reset():
    session['visits'] = 0
    return redirect('/')

if __name__=="__main__":  
    app.run(debug=True, port = 5100)  