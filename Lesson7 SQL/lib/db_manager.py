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
                login = self.__login()
                print(login)
            elif choice == 3:
                edit = self.__edit()
                print(edit)
            elif choice == 4:
                delete = self.__delete()
                print(delete)
            elif choice == 5:
                all_users = self.__all_users()
                print(all_users)
            elif choice == 6:
                search_by_Username = self.__searchByUsername()
                print(search_by_Username)
            elif choice == 7:
                search_by_Email = self.__searchByEmail()
                print(search_by_Email)
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
            sql = "DELETE FROM users WHERE username='" + username + "'"
            self.__cursor.execute(sql)
            self.__db.commit()
            return "User is deleted"
        else:
            return "This User do not exist!"

    def __login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        self.__cursor.execute(
            "SELECT * FROM users WHERE username='"+username+"' AND password='"+password+"'")
        user_login = self.__cursor.fetchone()
        if user_login != None:
            return "Login was successful"
        else:
            return "Check your registration information"

    def __edit(self):
        exit = False
        while not exit:
            edit = int(input(
                "Enter what you want to edit:\n1. Username\n2. Email\n3. Password\n0. OUT => "))
            if edit == 1:
                username = input("Edit username: ")
                self.__cursor.execute(
                    "SELECT * FROM users WHERE username='"+username+"'")
                user_edit = self.__cursor.fetchone()
                if user_edit != None:
                    new_username = input("New username: ")
                    sql = "UPDATE users SET username='"+new_username + \
                        "' WHERE username= '" + username + "'"
                    self.__cursor.execute(sql)
                    self.__db.commit()
                    return "Username is edited"
                else:
                    return "This User do not exist!"
            elif edit == 2:
                username = input("Enter username: ")
                email = input("Edit email: ")
                self.__cursor.execute(
                    "SELECT * FROM users WHERE email='"+email+"' AND username='" + username + "'")
                email_edit = self.__cursor.fetchone()
                if email_edit != None:
                    new_email = input("New email: ")
                    sql = "UPDATE users SET email='"+new_email+"' WHERE email= '" + \
                        email + "' AND username='" + username + "'"
                    self.__cursor.execute(sql)
                    self.__db.commit()
                    return "Email is edited"
                else:
                    return "This User do not exist!"
            elif edit == 3:
                username = input("Enter username: ")
                password = input("Edit password: ")
                self.__cursor.execute(
                    "SELECT * FROM users WHERE password='"+password+"' AND username='" + username + "'")
                password_edit = self.__cursor.fetchone()
                if password_edit != None:
                    new_password = input("New password: ")
                    sql = "UPDATE users SET password='"+new_password + \
                        "' WHERE password= '" + password + "' AND username='" + username + "'"
                    self.__cursor.execute(sql)
                    self.__db.commit()
                    return "Password is edited"
                else:
                    return "This User do not exist!"
            elif edit == 0:
                exit = True
                print("Edit complete")
            else:
                print("Wrong choise")

    def __all_users(self):
        self.__cursor.execute("SELECT * FROM users")
        all_users = self.__cursor.fetchall()
        return all_users

    def __searchByUsername(self):
        username = input("Enter name to search: ")
        self.__cursor.execute(
            "SELECT * FROM users WHERE username='" + username + "'")
        search_user = self.__cursor.fetchone()
        return search_user

    def __searchByEmail(self):
        email = input("Enter email to search: ")
        self.__cursor.execute(
            "SELECT * FROM users WHERE email='" + email + "'")
        search_user = self.__cursor.fetchone()
        return search_user
def __searchByEmail(self):
        email = input("Enter email to search: ")
        self.__cursor.execute(
            "SELECT * FROM users WHERE email='" + email + "'")
        search_user = self.__cursor.fetchone()
        return search_user