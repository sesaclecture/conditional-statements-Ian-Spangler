from datetime import datetime as dt
import json

users = {
    "ian411": {
        "name": "ian",
        "date of birth": "2004-01-01",
        "password": "1q2w3e4r",
        "role": "admin"
    },
    "kevin1717": {
        "name": "kevin",
        "date of birth": "1992-05-10",
        "password": "kdb123",
        "role": "viewer"
    },
    "elice0617": {
        "name": "elice",
        "date of birth": "2000-06-17",
        "password": "abc123",
        "role": "viewer"
    },
}

logged_in = True

status = input("SignUp:1, Login:2 ")
match status:
        case "1":
            new_id = input("ID: ")
            if new_id not in users:
                new_password = input("Password (10 or more characters): ")
                if len(new_password) >= 10:
                    new_date_of_birth = input("Date of birth: ")
                    try:
                        dt.strptime(new_date_of_birth, "%Y-%m-%d")
                        new_name = input('Name: ')
                        users[new_id] = {}
                        users[new_id]["name"] = new_name
                        users[new_id]["date of birth"] = new_date_of_birth
                        users[new_id]["password"] = new_password
                        users[new_id]["role"] = "viewer"
                        print(json.dumps(users, indent=2))
                    except ValueError:
                        print("Invalid date!")
                else:
                    print("Your password is too short!")
            else:
                print("This ID already exists!")
        case "2":
            id = input("ID: ")
            if id in users:
                password = input("Password: ")
                if users[id]["password"] == password:
                    print("Login success")
                    while logged_in:
                        tool = input("Edit:1, Delete:2, Log Out:3 ")
                        match tool:
                            case "1":
                                if users[id]["role"] == "admin":
                                    edit_user = input("Which user's data would you like to edit? ")
                                    edit_password = input("Password (10 or more characters): ")
                                    edit_date_of_birth = input("Date of birth: ")
                                    edit_name = input('Name: ')
                                    users[edit_user]["date of birth"] = edit_date_of_birth
                                    users[edit_user]["password"] = edit_password
                                    users[edit_user]["name"] = edit_name
                                else:
                                    edit_password = input("Password (10 or more characters): ")
                                    edit_date_of_birth = input("Date of birth: ")
                                    edit_name = input('Name: ')
                                    users[id]["date of birth"] = edit_date_of_birth
                                    users[id]["password"] = edit_password
                                    users[id]["name"] = edit_name
                                print(json.dumps(users, indent=2))
                            case "2":
                                if users[id]["role"] == "admin":
                                    delete_user = input("Which user's data would you like to delete? ")
                                    users.pop(delete_user)
                                else:
                                    users.pop(id)
                                    logged_in = False
                                print(json.dumps(users, indent=2))
                            case "3":
                                logged_in = False
                                print("You are Logged Out")
                else:
                    print("Wrong password!")
            else:
                print("User not exists")
        case _:
          print("Invalid")

