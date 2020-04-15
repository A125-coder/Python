if __name__ == "__name__":
    Users


class Users:

    def __init__(self, first_name, last_name, user_name, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__user_name = user_name
        self.__email = email
        self.__password = password

    def show_user_info(self):
        print("First name: ", self.__first_name, "\nLast name: ", self.__last_name,
              "\nUser name: ", self.__user_name, "\nEmail: ", self.__email, "\nPassword: *************", self.__password)

    def save_user(self):

        f = open('db.txt', 'a')
        f.write(self.__first_name + "#" + self.__last_name + "#" +
                self.__user_name + "#" + self.__email + "#" + self.__password + "\n")
        f.close()

    def show_all_users(self):
        users = []
        with open("db.txt", "r") as show_user_db:
            item = show_user_db.readline()
            item = item.strip()
            item = item.split("#")
            users.append(item)
        return users
