from gameComponents import gameVars
## Adding new function, and combine with choosewinner function : Ask player if want use gold coins to buy a chance to continue when lose. 

def buyorlose (status):
	print ("inside buyorlose function; status is ", status)

	if status == "lost":
		print("You", status, ",Would you like to use gold coins to buy a chance to revive? ")
		choice = input("Y / N ?")

		if choice =="N" or choice =="n":
			print ("Oh nooooooo you gonna die soon! Better luck next time!")
			exit()

		elif choice == "Y" or choice =="y":
			gold_coins = 200
		# show the player balance and give player the option to buy lives
			print("You now have:" , str(gold_coins),"bonus")
			print("It takes 100 coins for ONCE restart , Do you want purchase? ",)
			restart = input('Type the Yes here:   ')
			print("Now you revived!")
			gameVars.player_lives = 3
			gameVars.ai_lives = 3
			gameVars.player = False


	if status == "win":
		print("You", status, "! Would you like to play again?")
		choice = input("Y / N? ")

		if choice =="N" or choice =="n":
			print("You chose to quit! Better luck next time!")
			exit()
		elif choice == "Y" or choice =="y":
		
			gameVars.player_lives = 3
			gameVars.ai_lives = 3
			gameVars.player = False
			