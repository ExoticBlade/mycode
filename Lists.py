#Lists

List = input("Do you want to create a list? \n")

if List == "No" or List == "no":
    exit()
Custom_List = []

while True:
  Add = input("Do you want to add to the list? \n")
  if Add == "No" or Add == "no":
        exit()
  else:
   Add == "Yes" or Add == "yes"
  List_Add = (input("What do you want do add? \n"))
  Custom_List.append(List_Add)
  print(Custom_List)