 # import packages to extend python (just like we extend sublime, or Atom, or VScode)
from random import randint
# [] =>This is an array. an array is a special type of container that can hold mulitipe items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices =["rock","paper","scissors"]

#THIS IS the player choice
player = input("choose rock,paper or scissors:  ")

#this is will be the AI choice -> a random pick from the choices array
computer = choices[randint(0, 2)]

 #check to see what the user input

#print outputs whatever is in the tound brackets -> in this case it outputs palyer to the command prompt window. 

print("user choose: " + player)

#validate taht the ranndom choice worked for the AI

print("AI choose: " + computer)

if (computer == player): 
	print("tie")
elif (computer == "rock"):
	if (player == "scissors"):
		print("you lose!!!")
	else:
		print("you win!!!")

elif (computer == "paper"):
	if (player == "scissors"):
		print("you win!!!")
	else:
		print("you lose!!!")

elif (computer == "scissors"):
	if (player == "rock"):
		print("you win!!!")
	else:
		print("you lose!!!")
