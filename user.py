print("What is the user's name?")
user_name = input()
print("What is the user's age?")
user_age = input()
print("What is the user's country of birth?")
user_country = input()
print("What is the user known for?")
user_known = input()

user_information = {"name": user_name, 
                    "age": user_age, 
                    "country": user_country, 
                    "known for": user_known}

print(user_information)