import random
r=int(input("gues a random number"))
n=random.randint(1,9)
if n == r:
    print("guessed the correct number the number was",n)
else:
    print("you guessed the wrong number the number was",n)