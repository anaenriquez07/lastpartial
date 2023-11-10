https://replit.com/join/gfuewuvgos-ana-lucialuc103

import secrets
import string

letters_and_numbers = string.ascii_uppercase + string.digits
random_let_number = [secrets.choice(letters_and_numbers) for i in range(8)]
final_password =''.join(random_let_number)

print("The first letter is: ",random_let_number[0])
print("The second letter is: ",random_let_number [1])
print("The third letter is: ",random_let_number [2])
print("The fourth letter is: ",random_let_number [3])
print("The fifth letter is: ",random_let_number [4])
print("The sixth letter is: ",random_let_number [5])
print("The seventh letter is: ",random_let_number [6])
print("The eight letter is: ",random_let_number [7])
print(f"Your password is: {final_password}")
