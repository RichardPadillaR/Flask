from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.models import trees

class Users:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
        self.trees = []

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users"
        results = MySQLConnection('arbortrary').query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = MySQLConnection('arbortrary').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_user_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = MySQLConnection('arbortrary').query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def create_new_user(cls,data):
        query = "INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at ) VALUES (%(first_name)s, %(last_name)s, %(email)s , %(password)s, NOW(), NOW())"
        return MySQLConnection('arbortrary').query_db(query,data)

    @classmethod
    def get_user_trees(cls, users_id):
        query = "SELECT * FROM users JOIN trees ON trees.users_id = users.id WHERE users.id = %(id)s"
        result = MySQLConnection('arbortrary').query_db(query,users_id)
        if len(result) < 1:
            return False
        for row_from_db in result:
            trees_data = {
                "id": row_from_db["trees.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email" : row_from_db["email"],
                "password" : row_from_db["password"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"],
                "species" : row_from_db["species"],
                "location" : row_from_db["location"],
                "reason" : row_from_db["reason"],
                "date_planted" : row_from_db["date_planted"],
                "users_id" : row_from_db["users_id"],
                }
            tree_object = trees.Trees(trees_data)
            tree_result = cls(result[0])
            # results = Users.trees.append(tree_object) <--- keeps giving me error AttributeError: type object 'Users' has no attribute 'trees' and I know the atribute is up there, i've been at this for 3-4 hours just on this, watch videos and looked up on googled, used learner platform etc. If not would have been under 5 hours im sure, this was only thing TA couldn't go over before she left....couldn't figure it out sorry.
        return tree_result

    @staticmethod
    def validate_user(data):
        is_valid = True 
        if len(data['first_name']) < 2:
                flash("First Name must be at least 2 characters.")
                is_valid = False
        if len(data['last_name']) < 2:
                flash("Last Name must be at least 2 characters.")
                is_valid = False
        if len(data['email']) <= 4:
                flash("Please enter a valid email.")
                is_valid = False
        if len(data['password']) < 8:
                flash("Password needs to be at least 8 characters.")
                is_valid = False
        return is_valid