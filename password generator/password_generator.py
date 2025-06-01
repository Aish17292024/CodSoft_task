import string
import random

if __name__ == "__main__":
	str1 = string.ascii_lowercase
	str2 = string.hexdigits
	str3 = string.ascii_uppercase
	# takes the length of the password
	pass_len = int(input("Enter the length of the password: "))

	password = []

	password.extend(str1)
	password.extend(str2)
	password.extend(str3)
	# shuffles the generated string for the password
	random.shuffle(password)
	# joins the generated string to form a password
	print("".join(password[:pass_len]))
