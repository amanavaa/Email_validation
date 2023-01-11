# checking email validation using regix module
import re

email_condition = "^[a-zA-Z]+[\_.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
# ^ -> check the first position
# + -> all conditoins
# \ ->check any charcter in the email\string
# ? -> work with 0 or 1 only if any charcter in prestent 2 time it return false
# $ -> indexing start from last

email = input("Enter the email:")
if re.search(email_condition , email):
    print("you entered the right email")
else:
    print("This is an invalid email")    