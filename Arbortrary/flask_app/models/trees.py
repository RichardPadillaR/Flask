from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app.models import users

class Trees:
    def __init__(self,data):
        self.id = data["id"]
        self.species = data["species"]
        self.location = data["location"]
        self.reason = data["reason"]
        self.date_planted = data["date_planted"]
        self.users_id = data["users_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.users = []

    @classmethod
    def all_trees(cls):
        query = "SELECT * FROM trees"
        results = MySQLConnection('arbortrary').query_db(query)
        trees = []
        for tree in results:
            trees.append(cls(tree))
        return trees

    @classmethod
    def get_one_tree(cls,data):
        query = "SELECT * FROM trees WHERE id = %(id)s;"
        results = MySQLConnection('arbortrary').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update_tree(cls,data):
        query = "UPDATE trees SET species = %(species)s, location = %(location)s, reason = %(reason)s, date_planted = %(date_planted)s, Users_id = %(Users_id)s, updated_at = NOW() WHERE id = %(id)s"
        return  MySQLConnection('arbortrary').query_db(query,data)

    @classmethod
    def create_new_tree(cls,data):
        query = "INSERT INTO trees ( species, location, reason, date_planted, Users_id, created_at, updated_at ) VALUES (%(species)s, %(location)s, %(reason)s, %(date_planted)s, %(users_id)s, NOW(), NOW())"
        return MySQLConnection('arbortrary').query_db(query,data)

    @classmethod
    def delete_tree(cls,data):
        query = "DELETE FROM trees WHERE id = %(id)s;"
        results = MySQLConnection('arbortrary').query_db(query,data)
        return results

    @classmethod
    def get_user_trees(cls, users_id):
        query = "SELECT * FROM users LEFT JOIN trees ON trees.users_id = users.id WHERE users.id = %(id)s"
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
            #tree_object = users.Users.trees(trees_data)
            #tree_result = cls(tree_object[0])
            #tree_result.append(tree_object)
        return trees_data

    @staticmethod
    def validate_tree(data):
        is_valid = True 
        if len(data['species']) <= 5:
                flash("At least 5 characters for species!")
                is_valid = False
        if len(data['reason']) <= 0:
                flash("What was the reason?")
                is_valid = False
        if len(data['reason']) > 50:
                flash("50 characters or less please!")
                is_valid = False
        if len(data ['location']) <= 2:
                flash("Please tell us the location!")
                is_valid = False
        return is_valid