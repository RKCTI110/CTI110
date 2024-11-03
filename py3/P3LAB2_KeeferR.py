# CTI 110
# P3LAB2 - Grades and Games
# KeeferR
# 11/3/24

import random

def main ():
    
    print("Craps game")
    print("Roll from 1 to 6")
    
    #die1 = int(input("First Die:"))
    #die2 = int(input("Second Die:"))

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    total = die1 + die2
    print("Roll:", die1, "+", die2, "is", total)

    if total == 7:
        print("You win!")
    elif total == 11:
        print("You win!")
    elif total == 2:
        print("You lose!")
    elif total == 12:
        print("You lose!")
    else:
        print("Point was", total)
        print("To be continued...")

if __name__ == "__main__":
    main()
