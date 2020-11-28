 # import packages to extend python (just like we extend sublime, or Atom, or VScode)
from random import randint
from gameComponents import gameVars, buyorlose

 
print("==================*/ Welcome to RPS GAME /*=======================")
print("======*/ This is a battle simulation game requires logic and fortune. /*=====")
print("======*/You have only one intention - beat the AI to win more gold coins. *=====")
	
answer = input("Are you ready(Y / N)? ")

if answer == "Y" or answer == "y":
	gold_coins = 200
	print("Congrats! You get 200 gold coins as a BOUNS!")

elif answer == "N" or answer == "n":
	print("What? So surprised you're not ready, See you next time!")
	exit()
	
else:
	print("Make a valid choice  - Y OR N")
	choice = input("Y / N: ")

while gameVars.player == False: 

	#print("Now you have gold coins:", gold_coins)
	print("Computer lives" ,gameVars.ai_lives, "/", gameVars.total_lives)
	print("player lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("=======================================================")
 
	print("Choose your weapon! or type quit to exit\n") # \n means "new line"
	#THIS IS the player choice
	gameVars.player = input("choose rock ,paper or scissors:  \n")

	# if the player chose to quit, then exit the game
	if gameVars.player == "quit":
			print("you chose to quit")
			exit()

	#player = True -> it has a valuse (rock, paper, or scissors)

	#this is will be the AI choice -> a random pick from the choices array
	computer = gameVars.choices[randint(0,2)]

	#check to see what the user input

	#print outputs whatever is in the tound brackets -> in this case it outputs palyer to the command prompt window. 
	print("user choose: " + gameVars.player)

	#validate taht the ranndom choice worked for the AI
	print("AI choose: " + computer)

	if (computer == gameVars.player): 
		print("tie")

	elif (computer == "rock"):
		if (gameVars.player == "scissors"):
			print("you lose!!!")
			gameVars.player_lives -= 1
		else:
			print("you win!!!")
			gameVars.ai_lives -= 1
			gold_coins +=100
			print("Your Balance up to:" , str(gold_coins))
			
			

	elif (computer == "paper"):
		if (gameVars.player == "rock"):
			print("you lose!!!")
			gameVars.player_lives -= 1
		else: 
			print("you win!!!")
			gameVars.ai_lives -= 1
			gold_coins +=100
			print("Your Balance up to:" , str(gold_coins))
			
			

	elif (computer == "scissors"):
		if (gameVars.player == "paper"):
			print("you lose!!!")
			gameVars.player_lives -= 1
		else:
			print("you win!!!")
			gameVars.ai_lives -= 1
			gold_coins +=100
			print("Your Balance up to:" , str(gold_coins))

		 

#/-------------------------MOVE THIS CHUNK OF CODE TO A PACKAGE - START HERE-------------------/
	# if (computer == gameVars.player): 
	# 	print("tie")

	# always check for negative conditions first(the losing case)
	# elif (computer == "rock"):
	# 	if (gameVars.player == "scissors"):
	# 		print("you lose!!!")
	# 		gameVars.player_lives -= 1
	# 	else:
	# 		print("you win!!!")
	# 		gameVars.ai_lives -= 1

	# elif (computer == "paper"):
	# 	if (gameVars.player == "rock"):
	# 		print("you lose!!!")
	# 		gameVars.player_lives -= 1
	# 	else: 
	# 		print("you win!!!")
	# 		gameVars.ai_lives -= 1

	# elif (computer == "scissors"):
	# 	if (gameVars.player == "paper"):
	# 		print("you lose!!!")
	# 		gameVars.player_lives -= 1
	# 	else:
	# 		print("you win!!!")
	# 		gameVars.ai_lives -= 1

# /------------------STOP HERE - ALL OF THE ABOVE NEEDS TO MOVE ---------------/

	# if gameVars.player_lives == 0:
	# 	chooseWinner.winlorlose("lost")

	# if gameVars.ai_lives == 0:
	# 	chooseWinner.winlorlose("won")

	print("player_lives:", gameVars.player_lives, "lives left")
	print("ai_lives:", gameVars.ai_lives," lives left")


	if gameVars.player_lives == 0:
		buyorlose.buyorlose("lost")

	if gameVars.ai_lives == 0:
		buyorlose.buyorlose("win")




	#make the loop keep running by setting player bback to False
	# unset, so that our loop condition above will evauate to Ture
	gameVars.player = False











