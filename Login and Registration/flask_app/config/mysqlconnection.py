import pymysql.cursors

class MySQLConnection:
    def __init__(self, database_name):
        connection = pymysql.connect(
            host = 'localhost',
            user = 'root', 
            password = 'Archon5614',
            db = database_name,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True)
        self.connection = connection
    def query_db(self, query:str, data:dict=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    result = cursor.fetchall()
                    return result
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                raise e
            finally:
                self.connection.close() 
def connectToMySQL():
    return MySQLConnection()