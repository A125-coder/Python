import mysql.connector
if __name__ == "__main__":
    db_manager


class db_manager:

    def __init__(self, host, user, passwd):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS pythonlogin")
        self.__cursor.execute("USE pythonlogin")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Register\n 2. Login\n 3. Edit\n 4. Delete\n 5. Show all users\n 6. Search by user name\n 7. Search by user email\n 0. Exit ===>> "))
            if choice == 1:
                answer = self.__register()
                print(answer)
            elif choice == 2:
                print("Login")
            elif choice == 3:
                print("Edit")
            elif choice == 4:
                delete = self.__delete()
                print(delete)
            elif choice == 5:
                print("Show all users")
            elif choice == 6:
                print("Search by user name")
            elif choice == 7:
                print("Search by user email")
            elif choice == 0:
                exit = True
                print("Goodbye!")
            else:
                print("Wrong choise")

    def __register(self):
        username = input("Enter user name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        re_password = input("Confirm password: ")
        if password != re_password:
            return "Please check your password"

        self.__cursor.execute(
            "SELECT * FROM users WHERE username='"+username+"'")
        result = self.__cursor.fetchone()
        if result != None:
            return "User exists"
        else:
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s,%s)"
            val = (username, email, password)
            self.__cursor.execute(sql, val)
            self.__db.commit()
            return "User has been created"

    def __delete(self):
        username = input("Enter username to delete: ")
        self.__cursor.execute(
            "SELECT * FROM users WHERE username='"+username+"'")
        user_delete = self.__cursor.fetchone()
        if user_delete != None:
            sql = "DELETE FROM users WHERE username = '" + username + "'"
            self.__cursor.execute(sql)
            self.__db.commit()
            return "User is deleted"
        else:
            return "This User do not exist!"
