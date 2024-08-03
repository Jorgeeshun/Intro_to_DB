import mysql.connector
from mysql.connector import errorcode


def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="jorgeeshun"
        )
        cursor = connection.cursor()

        # Create database if it doesn't exist
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    

if __name__ == "__main__":
    create_database()


def create_tables():
    connection = mysql.connector.connect(
            db = "task_2",
            host="localhost",
            user="root",
            password="jorgeeshun"
    )

    myCursor = connection.Cursot()
    myCursor.execute("ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'jorgeeshun';FLUSH PRIVILEGES;")

    try:
        myCursor.execute("CREATE DATABASE IF NOT EXISTS task_2")
        print("Database 'alx_book_store' created successfully!")
       
        myCursor.execute("CREATE TABLE IF NOT EXISTS Authors (author_id INT AUTO INCREMENT PRIMARY KEY, author_name VARCHAR(215) NOT NULL); ")

    except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")

           

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

        
    myCursor.close()

    connection.close()

if __name__ == "__main__":
    create_database()

