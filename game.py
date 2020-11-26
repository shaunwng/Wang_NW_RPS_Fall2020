 # import packages to extend python (just like we extend sublime, or Atom, or VScode)
from random import randint

# [] =>This is an array. an array is a special type of container that can hold mulitipe items
# arrays are indexed (their contents get assigned a number)
# the index always starts at 0
choices = ["rock","paper","scissors"]

player_lives = 5
ai_lives = 5

total_lives = 5


#True and False are Boolean data types -> they are the euuivalent of on or off, 1 and 0
player = False

while player == False: 
	print("==================*/ RPS GAME /*=======================")
	print("Computer lives:" ,ai_lives, "/", total_lives)
	print("player Lives:", player_lives, "/", total_lives)
	print("=======================================================")
 
	print("Choose your weapon! or type quit to exit\n") # \n means "new line"
	#THIS IS the player choice
	player = input("choose rock,paper or scissors:  \n")

	# if the player chose to quit, then exit the game
	if player == "quit":
			print("you chose to quit")
			exit()

	#player = True -> it has a valuse (rock, paper, or scissors)

	#this is will be the AI choice -> a random pick from the choices array
	computer = choices[randint(0,2)]

	#check to see what the user input

	#print outputs whatever is in the tound brackets -> in this case it outputs palyer to the command prompt window. 
	print("user choose: " + player)

	#validate taht the ranndom choice worked for the AI
	print("AI choose: " + computer)

	if (computer == player): 
		print("tie")

	# always check for negative conditions first(the losing case)
	elif (computer == "rock"):
		if (player == "scissors"):
			print("you lose!!!")
			player_lives -= 1
		else:
			print("you win!!!")
			ai_lives -= 1

	elif (computer == "paper"):
		if (player == "rock"):
			print("you lose!!!")
			player_lives -= 1
		else: 
			print("you win!!!")
			ai_lives -= 1

	elif (computer == "scissors"):
		if (player == "paper"):
			print("you lose!!!")
			player_lives -= 1
		else:
			print("you win!!!")
			ai_lives -= 1


	if player_lives == 0:
		print("You lose! Would you like to play again?")
		choice = input("Y/N")

		if choice =="N" or choice == "n":
			print("You chose to quit! Better luck next time!")
			exit()

		elif choice == "Y" or choice =="y":
			#reset the player lives and the AI lives
			# and set player to False so that our loop will restart
			player_lives = 5
			ai_lives = 5
			player = False

		else:
			print("Make a valid choice  - Y OR N")
			# this will generate a bug that we need to fix later
			choice = input("Y / N: ")

	if player_lives == 0:
		print("You WON! Would you like to play again?")
		choice = input("Y / N")

		if choice =="N" or choice == "n":
			print("You chose to quit! Better luck next time!")
			exit()

		elif choice == "Y" or choice =="y":
			#reset the player lives and the AI lives
			# and set player to False so that our loop will restart
			player_lives = 5
			ai_lives = 5
			player = False

		else:
			print("Make a valid choice  - Y OR N")
			# this will generate a bug that we need to fix later
			choice = input("Y / N: ")

	print("player_lives:", player_lives, "lives left")
	print("ai_lives:", ai_lives," lives left")


	#make the loop keep running by setting player bback to False
	# unset, so that our loop condition above will evauate to Ture
	player = False












