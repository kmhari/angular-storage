import string, random
#--------Random String generator-----
def id_generator(size):
	return ''.join(random.choice(string.ascii_uppercase) for _ in range(size))
#--------------

def guesses(wrd,lmt):
	no_of_guess=0
	found=0
	while True:
		while True:
			guess=input("\n Guess a string in CAPS and of the appropriate length: ")
			if len(guess)==len(wrd):
				break;
		no_of_guess= no_of_guess+1
		corr_pos=0
		wrg_pos=0
		#wrg_letter=0
		#------------Game Logic
		for x in guess:
			if x in wrd:
				if guess.index(x) == wrd.index(x):
					corr_pos= corr_pos +1
				else :
					wrg_pos=wrg_pos+1
		#--------------
		print("\n The number of characters that are correct but are in the wrong place is "+str(wrg_pos))
		print("\n The number of characters that are correct and are in the correct place is "+str(corr_pos))
		if corr_pos == len(wrd):
			print("\n You've guessed correctly :)")
			found = 1 
		else:
			print("\n Wrong Guess :(")
			
			
			
			
		if no_of_guess>= lmt or found==1:
			break
		if found == 1:
			print("\n Congrats! ")
		else:
			print("\n Guesses Exceeded! Hard Luck!")
	
	
#--------------------
def main():
	while True:
	
		while True:
			limit=int(input ("Enter the limit of guesses: "))
			if limit>=1:
				break
		x=random.randint(2,7)
		
		word= id_generator(x)
		print("\n The size of the string is "+ str(len(word)))
		guesses(word,limit)
		play=input("Wanna play again? (Y/N)")
		if play== 'N':
			break
#-------------------------
main()



