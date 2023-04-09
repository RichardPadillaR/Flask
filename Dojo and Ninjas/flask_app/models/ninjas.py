from flask_app.config.mysqlconnection import MySQLConnection
from flask_app.models import dojo

class Ninjas:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
        
        self.dojo = None


    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"
        results = MySQLConnection('dojos_and_ninjas').query_db(query)
        ninjas = []
        for dojo in results:
            ninjas.append(cls(dojo))
        return ninjas

    @classmethod
    def get_one_ninjas(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        results = MySQLConnection('dojos_and_ninjas').query_db(query,data)
        return cls(results[0])

    @classmethod
    def delete_ninjas(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        results = MySQLConnection('dojos_and_ninjas').query_db(query,data)
        return results

    @classmethod
    def save_ninjas(cls, data):
        query = query = "INSERT INTO ninjas ( dojo_id, first_name , last_name , age , created_at, updated_at ) VALUES ( %(dojo_id)s, %(first_name)s , %(last_name)s , %(age)s , NOW() , NOW() );"
        return MySQLConnection('dojos_and_ninjas').query_db( query, data )

    @classmethod
    def edit_ninjas(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s"
        return MySQLConnection('dojos_and_ninjas').query_db(query, data)

    @classmethod
    def get_ninjas_in_dojo( cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id=%(id)s"
        results = MySQLConnection('dojos_and_ninjas').query_db(query, data)
        if len(results) < 1:
            return False

        dojo_object = dojo.Dojos(results[0])
        for row_from_db in results:
            ninjas_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "dojo_id": row_from_db["dojo_id"],
                "created_at": row_from_db["created_at"],
                "updated_at": row_from_db["updated_at"],
            }
            ninja =cls(ninjas_data)
            dojo_object.ninjas.append(ninja)
        return dojo_object

