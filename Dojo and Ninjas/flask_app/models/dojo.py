from flask_app.config.mysqlconnection import MySQLConnection

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data ['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = MySQLConnection('dojos_and_ninjas').query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one_dojo(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = MySQLConnection('dojos_and_ninjas').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def delete_dojo(cls,data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        results = MySQLConnection('dojos_and_ninjas').query_db(query,data)
        return results

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        return MySQLConnection('dojos_and_ninjas').query_db( query, data )

    @classmethod
    def edit_dojo(cls, data):
        query = "UPDATE dojos SET name = %(name)s, WHERE id = %(id)s"
        return MySQLConnection('dojos_and_ninjas').query_db(query, data)

