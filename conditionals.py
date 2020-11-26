# set up a  variable, check its value, and then go down some different paths depending on the outcome.

#cast our user input - which bu default will be text - to a number using int()
temparature = int(input("input a value between 0 and 100: "))

#compare user input with the following conditions
if (temparature <= 4 ):
	#water will be frozen
	print("water's state is solid (ice)")

elif (temparature <100 ):
	#water is liquid
	print("water's state is liquid")
else:
	#water is boiling, so it's steam
	print("water is vapor")