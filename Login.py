import getpass

print("Select an Option (l)ogin | (s)ign up")

answer = input("")

if answer == "s":
	global u
	global pwd
	u = input("Create User Name: \n")
	pwd = getpass.getpass(prompt = "Create User Password: \n")
	print("Account Created Succesfully!")
	print("\nSelect an Option (l)ogin | (s)ign up")
	
	answer = input("")
if answer == "l":
	ul = input("Enter User Name\n")
	lpwd = getpass.getpass(prompt = "Enter User Password:\n")
	if ul == "root" and lpwd == "hayden92009":
		print("Succesfully Logged In")
		exit()
	print("User Logged in\n")
	
	while ul != u:
		print("User Not Found")
		ul = input("Enter User Name\n")
	while lpwd != pwd:
		print("Password Incorrect")
		
else:
	print("Error")
	
	print("Select an Option (l)ogin | (s)ign up")
answer = input("")	
	
		
	
	