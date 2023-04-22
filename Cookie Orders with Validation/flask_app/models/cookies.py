from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash

class Cookies:
    def __init__(self,data):
            self.id = data["id"]
            self.customer_name = data["customer_name"]
            self.number_of_boxes = data["number_of_boxes"]
            self.cookie_type = data["cookie_type"]
            self.created_at = data["created_at"]
            self.updated_at = data["updated_at"]

    @classmethod
    def get_all_cookies(cls):
        query = "SELECT * FROM cookie_orders"
        results = MySQLConnection('cookie_orders').query_db(query)
        cookies = []
        for cookie in results:
            cookies.append(cls(cookie))
        return cookies

    @classmethod
    def get_one_cookie(cls,data):
        query = "SELECT * FROM cookie_orders WHERE id = %(id)s;"
        results = MySQLConnection('cookie_orders').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def update_cookie(cls,data):
        query = "UPDATE cookie_orders SET customer_name = %(customer_name)s, number_of_boxes = %(number_of_boxes)s, cookie_type = %(cookie_type)s, updated_at = NOW() WHERE id = %(id)s"
        return  MySQLConnection('cookie_orders').query_db(query,data)


    @classmethod
    def create_new_order(cls,data):
        query = "INSERT INTO cookie_orders ( customer_name, number_of_boxes, cookie_type, created_at, updated_at ) VALUES (%(customer_name)s, %(number_of_boxes)s, %(cookie_type)s, NOW(), NOW())"
        return MySQLConnection('cookie_orders').query_db(query,data)

    @staticmethod
    def validate_order(data):
        is_valid = True 
        if len(data['customer_name']) < 3:
                flash("Customer Name must be at least 3 characters.")
                is_valid = False
        if int(data['number_of_boxes']) <= 0:
                flash("Please order atleast 1 box")
                is_valid = False
        if len(data ['cookie_type']) < 2:
                flash("Cookie Type must be 2 characters or greater.")
                is_valid = False
        return is_valid