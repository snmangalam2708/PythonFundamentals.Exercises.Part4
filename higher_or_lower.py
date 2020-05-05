from random import randrange
def randomize():
    num = int(input("Enter a number within 0 and 10 " + " "))
    t = randrange(10)
    if (num<t): 
        print("Number was low")
        print("Random number was: ", t)
        print("Your guess was:", num, "\n")
        randomize()
    elif (num>t): 
        print("Number was high")
        print("Random number was: ", t)
        print("Your guess was:", num, "\n")
        randomize()
    else:
        print("Number was spot-on")
        print("Random number was: ", t)
        print("Your guess was:", num, "\n")
randomize()