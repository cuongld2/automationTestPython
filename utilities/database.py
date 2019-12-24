import mysql
from mysql.connector import Error


class MySQL:

    def connect(self, host_name, database_name, user_name, password):
        try:
            connection = mysql.connector.connect(host=host_name,
                                                 database=database_name,
                                                 user=user_name,
                                                 password=password)

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("Your connected to database: ", record)
                return connection

        except Error as e:
            print("Error while connecting to MySQL", e)

    def close(self, connection):
        if connection.is_connected():
            connection.cursor().close()
            connection.close()
            print("MySQL connection is closed")


class RestAPIDatabase:

    def get_user_info_by_username(self, connection, username):
        sql_query = 'SELECT * FROM user_info where username = %s'
        cursor = connection.cursor()
        cursor.execute(sql_query, (username,))
        row = cursor.fetchone()
        return row

    def delete_user_info_by_username(self, connection, username):
        sql_query = 'DELETE FROM user_info WHERE username = %s'
        cursor = connection.cursor()
        cursor.execute(sql_query, (username,))
        connection.commit()
