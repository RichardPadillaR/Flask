from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)   
app.secret_key = "archon" 
@app.route('/dojo-survey')          
def dojo_survey_input():
    return render_template("show.html") 

@app.route('/result', methods=['POST', 'GET'])
def dojo_survey_result():
    if request.method == 'POST':
        session['your_name'] = request.form['your_name']
        session['dojo_location'] = request.form['dojo_location']
        session['favorite_language'] = request.form['favorite_language']
        session['comment'] = request.form['comment']
        return redirect('/show')

@app.route('/show')
def show_user_input():
    return render_template('user_info.html', your_name= session['your_name'], dojo_location= session['dojo_location'], favorite_language= session['favorite_language'], comment= session['comment'])

if __name__=="__main__":   
    app.run(debug=True, port = 5100) 