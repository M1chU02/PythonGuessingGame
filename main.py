import random
turns = 0
n = random.randint(1, 99)
guess = int(input("Enter an integer from 1 to 99: "))
while True:
    if guess < n:
        turns += 1
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        turns += 1
        print ("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        turns += 1
        turns = str(turns)
        print ("you guessed it right!")
        if turns == 1:
            print ("it took you only " + turns + " turn")
        else:
            print ("it took you only " + turns + " turns")
        break
