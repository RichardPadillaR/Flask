from flask_app import app
import flask_app.controllers.cookies_controller

if __name__=="__main__":   
    app.run(debug=True, port = 5100) 