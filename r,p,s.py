import random

user_wins = 0
com_wins = 0

options = ["R","P","S"]

while True:
    user_input = input("Type R/P/S or Q :  ").lower()
    if user_input == "q":
        break

    if user_input not in options :
        continue

    random_num = random.randint(0, 2)

    com_pick = options[random_num]
    print("Com picked",com_pick + ".")

    if user_input == "R" and com_pick == "S":
        print("You Won!")
        user_wins += 1    

    elif user_input == "P" and com_pick == "R":
        print("You Won!")
        user_wins += 1   

    elif user_input == "S" and com_pick == "P":
        print("You Won!")
        user_wins += 1   

    else : 
        print("You Lost!")
        com_wins += 1

print("BYE!!!")
