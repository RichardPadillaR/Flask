from flask_app.config.mysqlconnection import MySQLConnection

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = MySQLConnection('users').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = MySQLConnection('users').query_db(query,data)
        return cls(results[0])

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        results = MySQLConnection('users').query_db(query,data)
        return results

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email , created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );"
        return MySQLConnection('users').query_db( query, data )

    @classmethod
    def edit_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s"
        return MySQLConnection('users').query_db(query, data)