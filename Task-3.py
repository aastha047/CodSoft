import string
import random

length = int(input("Enter password length: "))
print("Choose character sets for password: \n1.Letters\n2.Digits\n3.Special characters\n4.Exit")
characterList = ""

while(True):
	choice = int(input("Pick a number "))
	if(choice == 1):
		characterList += string.ascii_letters
	elif(choice == 2):
		characterList += string.digits
	elif(choice == 3):
		characterList += string.punctuation
	elif(choice == 4):
		break
	else:
		print("Invalid choice")
		break

password =""
for i in range(length):
    password += random.choice(characterList)
print("The generated password is:", password)

