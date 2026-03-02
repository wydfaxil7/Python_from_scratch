####### STONE PAPER SCISSOR GAME ########

import random

comp = random.randint(1,3)
Stone = "1. Stone"
Paper = "2. Paper"
Scissor = "3. Scissor"
print(Stone.center(20))
print(Paper.center(20))
print(Scissor.center(22))

user = int(input("\nEnter your choice: "))

print(f"\nComputer chose: {comp}")
print(f"You chose: {user}")

if comp == user: 
    print("\nIts a tie")
elif(comp == 1 and user == 2) or(comp == 2 and user == 3) or (comp == 3 and user == 1):
    print("\nYOU WON")
else:    
    print("\nYOU LOST")

