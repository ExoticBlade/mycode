import random

Choices = ["Rock", "Paper", "Scissors"]

R = random.choice(Choices)

Person = input(" Rock, Paper or Scissors? ")

if Person == "Rock" and R == "Paper":
  print("You Lose!")
  exit()
  
if Person == "Rock" and R == "Scissors":
  print("You Win!")
  exit()
  
if Person == "Rock" and R == "Rock":
  print("Tie")
  exit()
  
if Person == "Paper" and R == "Rock":
  print("You Win!")
  exit()
  
if Person == "Paper" and R == "Paper":
  print("Tie")
  exit()
  
if Person == "Paper" and R == "Scissors":
  print("You Lose!")
  exit()
  
if Person == "Scissors" and R == "Scissors":
  print("Tie")
  exit()
  
if Person == "Scissors" and R == "Paper":
  print("You Win!")
  exit()
  
if Person == "Scissors" and R == "Rock":
  print("You Lose!")
  exit()