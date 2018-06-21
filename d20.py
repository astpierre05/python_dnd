#dungeons and dragons skill checks and attacks
import random

while True:
    input("Press enter to roll a D20")
    d20 = random.randint (1,20)
    print(d20)
    if d20 == 1:
        print("You have critically failed. Good job stabbing your party member")
    elif d20 == 20:
        print("Critical Success! You did the hell out of that thing!")
