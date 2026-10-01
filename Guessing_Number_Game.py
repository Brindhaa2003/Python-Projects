import random
print("------Welcome to Guessing Number Game------")
num=random.randint(1,50)
for i in range(5):
    guess_num=int(input("Enter a Guessing Number:"))
    if num==guess_num:
        print("You Won the Game...")
        break
    elif num>guess_num:
        print("The Guessing Number is Bigger than Your Number")
    elif num<guess_num:
        print("The Guessing Number is Smaller than Your Number")
    print("You have only",4-i,"choices")
    print("-------------------------------------")
else:
    print("The Correct Number is:",num)
    print("You Loss the Game")
print("Game Over")