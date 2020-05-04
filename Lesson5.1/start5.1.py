from lib.person import Users

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
user_name = input("Enter your user name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
user = Users(first_name, last_name, user_name, email, password)
# user.show_user_info()
print(
    "===================================================================")
user.register()
user.save_user()
# users = user.show_all_users()
# print(users)




# user2 = Users("Bran", "Stark", "b_stark", "bs@gmail.com", "bskingofnorth")
# user2.show_user_info()
# user2.save_user()