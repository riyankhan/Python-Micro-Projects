#This program is optimized for Python 3
#It should work on Python 2 as well but with some modifications
#You can use this program to generate a random number or you can also use this program as a dice.
#For more such interesting Python programs, visit: https://github.com/bytesandcode

from random import randint
user_answer = input("Want to generate a random number? Enter y for yes and n for no.: ").lower().strip()

if user_answer == "y":
    print(randint(1, 7))
elif user_answer == "n":
    print("No??...It's okay :(")
else:
    print("Error: Enter Y or N silly!")
