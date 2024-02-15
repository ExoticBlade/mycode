import getpass
import sys
import time

def typewriter_effect(text):
    typing_speed = 2 / len(text)  # Calculate typing speed dynamically
    start_time = time.time()
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        while (time.time() - start_time) < typing_speed:
            pass
        start_time = time.time()  # Reset start time for the next character
    print()

typewriter_effect("Booting System...[+]\n")

def typewriter_effect2(text):
    typing_speed = 2 / len(text)  # Calculate typing speed dynamically
    start_time = time.time()
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        while (time.time() - start_time) < typing_speed:
            pass
        start_time = time.time()  # Reset start time for the next character
    print()

typewriter_effect2("Starting Services... [+]\n")

def typewriter_effect3(text):               
    typing_speed = 1 / len(text)  # Calculat
    start_time = time.time()                
    for char in text:                       
        sys.stdout.write(char)              
        sys.stdout.flush()                  
        while (time.time() - start_time) < typing_speed:
            pass                            
        start_time = time.time()  # Reset st
    print()                                 
                                            
typewriter_effect3("Booting Login Terminal...[+]\n")

import sys
import time

def typewriter_effect4(text):
    typing_speed = 2 / len(text)  # Calculate typing speed dynamically
    start_time = time.time()
    for idx, char in enumerate(text):
        if idx == 9:  # Check if the character is the 's' in 'services'
            char = char.upper()  # Convert 's' to uppercase
        sys.stdout.write(char)
        sys.stdout.flush()
        while (time.time() - start_time) < typing_speed:
            pass
        start_time = time.time()  # Reset start time for the next character
    print()

typewriter_effect4("Initializing Hardware...[+]\n")

import sys
import time

def typewriter_effect5(text):
    typing_speed = 2 / len(text)  # Calculate typing speed dynamically
    start_time = time.time()
    for idx, char in enumerate(text):
        if idx == 9:  # Check if the character is the 's' in 'services'
            char = char.upper()  # Convert 's' to uppercase
        sys.stdout.write(char)
        sys.stdout.flush()
        while (time.time() - start_time) < typing_speed:
            pass
        start_time = time.time()  # Reset start time for the next character
    print()

typewriter_effect5("BIOS/UEFI initializing...[+]\n")

import sys
import time

def typewriter_effect6(text):
    typing_speed = 2 / len(text)  # Calculate typing speed dynamically
    start_time = time.time()
    for idx, char in enumerate(text):
        if idx == 9:  # Check if the character is the 's' in 'services'
            char = char.upper()  # Convert 's' to uppercase
        sys.stdout.write(char)
        sys.stdout.flush()
        while (time.time() - start_time) < typing_speed:
            pass
        start_time = time.time()  # Reset start time for the next character
    print()

typewriter_effect6("Loading Kernel...[+]\n")

import sys
import time

def typewriter_effect7(text):
    typing_speed = 2 / len(text)  # Calculate typing speed dynamically
    start_time = time.time()
    for idx, char in enumerate(text):
        if idx == 9:  # Check if the character is the 's' in 'services'
            char = char.upper()  # Convert 's' to uppercase
        sys.stdout.write(char)
        sys.stdout.flush()
        while (time.time() - start_time) < typing_speed:
            pass
        start_time = time.time()  # Reset start time for the next character
    print()

typewriter_effect7("Mounting Filesystems...[+]\n")

import sys
import time

def typewriter_effect8(text):
    typing_speed = 2 / len(text)  # Calculate typing speed dynamically
    start_time = time.time()
    for idx, char in enumerate(text):
        if idx == 9:  # Check if the character is the 's' in 'services'
            char = char.upper()  # Convert 's' to uppercase
        sys.stdout.write(char)
        sys.stdout.flush()
        while (time.time() - start_time) < typing_speed:
            pass
        start_time = time.time()  # Reset start time for the next character
    print()

typewriter_effect8("Starting System...[+]\n")

def typewriter_effect9(text):
    typing_speed = 2 / len(text)  # Calculate typing speed dynamically
    start_time = time.time()
    for idx, char in enumerate(text):
        if idx == 9:  # Check if the character is the 's' in 'services'
            char = char.upper()  # Convert 's' to uppercase
        sys.stdout.write(char)
        sys.stdout.flush()
        while (time.time() - start_time) < typing_speed:
            pass
        start_time = time.time()  # Reset start time for the next ")
    print()

typewriter_effect9("Loading Drivers...[+]\n\n\n\n")

print("Welcome To Nyx Linux! \n")

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
	exit()
	
	while ul != u:
		print("User Not Found")
		ul = input("Enter User Name\n")
	while lpwd != pwd:
		print("Password Incorrect")
		
else:
	print("Error")
	
	print("Select an Option (l)ogin | (s)ign up")
answer = input("")	
