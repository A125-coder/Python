import shelve
if __name__ == "__name__":
    Users

INFO = list()


class Users:

    def __init__(self, first_name, last_name, user_name, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_name = user_name
        self.__email = email
        self.__password = password

    def show_user_info(self):
        # print("First name: ", self.__first_name, "\nLast name: ", self.__last_name,
        #       "\nUser name: ", self.__user_name, "\nEmail: ", self.__email,
        #       "\nPassword: ", self.__password)
        INFO.append(self.__first_name + " # " + self.__last_name + " # " +
                    self.__user_name + " # " + self.__email + " # " + self.__password + "\n")

    def save_user(self):
        # doc = open('db.txt', 'a')
        # doc.write(self.__first_name + " # " + self.__last_name + " # " +
        #           self.__user_name + " # " + self.__email + " # " + self.__password + "\n")
        # doc.close()
        with open("db.txt", "a") as doc:
            doc.write(self.__first_name + " # " + self.__last_name + " # " +
                      self.__user_name + " # " + self.__email + " # " + self.__password + "\n")
        doc.close()

    def show_all_users(self):
        users = []
        with open("db.txt", "r") as doc:
            for lines in doc:
                if len(lines.strip()) > 0:
                    user = lines.strip()
                    user_info = user.split("#")
                    users.append(user_info)
            return users

    def register(self):
        """1. Реєстрація нового користувача з перевіркою (перевірити чи користувач вже є в файлі)
        """
        users_register = self.__dict__.values()
        # all_users = self.show_all_users()
        # with shelve.open("db.txt", "n") as doc:
        for item in users_register:
            if item[2] == self.__user_name:
                print("Username '" + item[2] + "' is already present")
            return users_register

    def check_passw(self):
        """2. Логін користувача (логін по username з перевіркою паролю.)
        """

    def delete_user(self):
        """3. Видалення користувача (по username)
        """
