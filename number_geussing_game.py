import random

user=input("Guess any number between 1 to 50=") 
game_over=False
geuss=1
win_num=random.randint(1,50)

while not game_over:
	user=int(user)
	if user==win_num:
		print(f"You win {geuss}")
		geuss=1
		user=input("Geuss number and q for quit=")
		if user.lower()=="q":
	 	     game_over=True
	 
	else:
	       if user>win_num:
	       	print("To high")
	       	geuss+=1
	       	user=input("Guess again=")
	       else:
	           print("To Low")
	           geuss+=1
	           user=input("Guess again=")	 
