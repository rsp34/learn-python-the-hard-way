from sys import exit

#def new_court():
#	print "You are now in new court. Do you go up D staircase, head to library court, go \
#	go to Old Court

def porters():
	dead("You've entered the Porter's lodge. Kay starts talking to you and you are \
	stuck for all eternity.")

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	name = raw_input("Please enter your name > ")
	print "Hello " + name + "."
	print "Imagine you're an ASNAC student at Corpus Christi College, Cambridge."
	print "You've been tasked with finding the College's Auroch horn."
	print "You're at the entrance to the College. Which way do you go straight or left?"
	
	choice = raw_input("> ")
	
	if choice == "straight":
		new_court()
	elif choice == "left":
		porters()
	else:
		dead("You went the wrong way!")
		
start()