import random

#  Stone Paper Scissors
def gameWin(comp, you):
    # If two values are equal, declare a tie!
    if comp == you:
        return None

    # when computer chose stone
    elif comp == 's':
        if you=='sc':
            return False
        elif you=='p':
            return True
    
    #  when computer chose paper
    elif comp == 'p':
        if you=='s':
            return False
        elif you=='sc':
            return True
    
    # when computer chose scissor
    elif comp == 'sc':
        if you=='p':
            return False
        elif you=='s':
            return True

print("Comp Turn: Stone(s) paper(p) or scissor(sc)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 'sc'

you = input("Your Turn: Snake(s) paper(p) or scissor(sc)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")