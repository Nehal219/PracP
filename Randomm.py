import random

computer = random.randint(0,100)
i = 1

while(True):
    you = int(input("Enter your number:"))
    if (you < computer):
        print("Enter a larger number!!!")
        i += 1
    elif (you > computer):
        print("Enter a smaller number!!!")
        i += 1
    elif (you == computer):
        print("YOU WIN...")
        print("Number of Guesses you took:",i)
        break
