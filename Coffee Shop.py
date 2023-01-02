#lets start a coffee shop!

#lets build a robot barista!

#whats Your name?
print("Hello! Welcome To Haydens Coffee Shop")

name = input("What Is Your Name? \n")
#lets build a robot bouncer!
#is Ben OR Patricia OR Loki evil?
if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("are you evil?\n")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "yes" and good_deeds < 4: 
        print("Your Not Welcome Here " + name + ". Get Out Of Here!!")
        exit()
    else:
        print("oh so your one of those good " + name + "s?")
else:
    print("Hello " + name + ",Thank You For Coming In Today! \n\n\n")


beard_length = int(input("how long is your beard?\n"))

if beard_length >= 1:
    print("oh, hello good sir, nice beard. you may go to the front of the line")

#ask the customer what they would want and store it in the variable quantity
menu = "Black Coffee, Espresso, Latte, Cappucino, Frappucino"

print(name + ", What Would You Like From Our Menu Today? Here Is What We Are Serving.\n" + menu)

order = input()
#set Price for coffee

if order == "Frappucino":
    price = 8
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 4
elif order == "Latte":
    price = 2
elif order == "Cappucino":
    price = 5
else:
    print("Sorry, we dont have that here")
    exit()


quantity = input("How Many Coffees Would You Like?\n")

total = price * int(quantity)

print("Thank You. Your Total Is: $" + str(total))

print("Sounds Good " + name + ", We'll Have Your " + quantity + " " + order + " Ready For You In A Moment\n")

print("Order Ready For " + name +",Have A Nice Day")