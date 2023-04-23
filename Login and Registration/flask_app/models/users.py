from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash

class Users:
    def __init__(self,data):
            self.id = data["id"]
            self.first_name = data["first_name"]
            self.last_name = data["last_name"]
            self.email = data["email"]
            self.password = data["password"]
            self.created_at = data["created_at"]
            self.updated_at = data["updated_at"]

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM login_registration"
        results = MySQLConnection('login_registration').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM login_registration WHERE id = %(id)s;"
        results = MySQLConnection('login_registration').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_user_email(cls,data):
        query = "SELECT * FROM login_registration WHERE email = %(email)s;"
        result = MySQLConnection('login_registration').query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def create_new_user(cls,data):
        query = "INSERT INTO login_registration ( first_name, last_name, email, password, created_at, updated_at ) VALUES (%(first_name)s, %(last_name)s, %(email)s , %(password)s, NOW(), NOW())"
        return MySQLConnection('login_registration').query_db(query,data)

    @staticmethod
    def validate_order(data):
        is_valid = True 
        if len(data['first_name']) < 3:
                flash("First Name must be at least 3 characters.")
                is_valid = False
        if len(data['last_name']) < 3:
                flash("Last Name must be at least 3 characters.")
                is_valid = False
        if len(data['email']) <= 4:
                flash("Please enter a valid email.")
                is_valid = False
        if len(data['password']) < 8:
                flash("Password needs to be at least 8 characters.")
                is_valid = False
        return is_valid