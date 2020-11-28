# from gameComponents import gameVars

# # define a win or lose function
# def winlorlose (status): 
# 	#print("inside winlorlose function; status is: ", status)

# 	print("You", status, "! Would you like to play again?")
# 	choice = input("Y / N? ")

# 	if choice =="N" or choice == "n":
# 		print("You chose to quit! Better luck next time!")
# 		exit()

# 	elif choice == "Y" or choice =="y":
# 		#reset the player lives and the AI lives
# 		# and set player to False so that our loop will restart
	
# 		gameVars.player_lives = 3
# 		gameVars.ai_lives = 3
# 		gameVars.player = False
# 	#this still throws a bug - doesn't present the right choice
# 	else:
# 		print("Make a valid choice  - Y OR N")
# 		# this will generate a bug that we need to fix later
# 		choice = input("Y / N: ")