import os
import json
import time
import subprocess


def initial_message():
	subprocess.call("clear", shell=True)
	print("Hi, I am LinkedIN bot.\n")
	time.sleep(2)
	print("I am here to help you to automate your messaages and make your life hassle free and easy.")
	print("\n\n\n")
	time.sleep(3)
	return

def save_credentials():
	
	def username_entry():
		username = input("Enter your LinkedIN USERNAME: ").strip()
		re_username = input("Re-enter your LinkedIN USERNAME: ").strip()
		if(username != re_username):
			print("\n\n")
			print("USERNAME was not same. Please re-enter your USERNAME.")
			username_entry()
		return username

	def password_entry():
		password = input("Enter your LinkedIN PASSWORD: ").strip()
		re_password = input("Re-enter your LinkedIN PASSWORD: ").strip()
		if(password != re_password):
			print("\n\n")
			print("PASSWORD was not same. Please re-enter your PASSWORD.")
			password_entry()
		return password

	def store_credentials(username, password):
		subprocess.call("clear", shell=True)
		print("Storing your credentials safely.")
		with open("./metadata/credentials.json", "w") as f:
			json.dump({"username": username, "password": password}, f)
		time.sleep(1)
		print("\n\n\n\n")
		print("YAYYYYYYYYYYYYYY!!!!!!!!!!!!!")
		print("LinkedIN bot is successfully installed.")
		return


	subprocess.call("clear", shell=True)
	print("Now we will be taking your credentials. So I can talk to your profile and do work for you.")
	print("\n")
	time.sleep(3)
	print("Don't worry. Your credentials will only be in your system and in your system only.")
	print("\n")
	time.sleep(3)
	print("I will be open source FOREVER so chill.")
	print("\n")
	time.sleep(2)
	print("So if you believe in the power of open source then be a part of it.")
	print("\n")
	time.sleep(3)
	print("\n\n")

	username = username_entry()

	print("\n\n")

	password = password_entry()

	store_credentials(username, password)


initial_message()

save_credentials()