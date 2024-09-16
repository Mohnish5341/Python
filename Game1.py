import random
from playsound import playsound

print("Comp Turn: Snakes(s) Water(w) or Gun(g)?")
randNo =random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
print("computer selected")
you=input("Your Turn: Snakes(s) Water(w) or Gun(g)?")
print("You selected")

def gamewin(comp,you):
    if comp=='s':
        if you=='w':
          return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
          return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
          return False
        elif you=='w':
            return True
    elif comp==you:
        return None
print(f"Computer chose {comp}")
print(f"You chose {you}")

a=gamewin(comp,you)
if a==None:
    print("The game is a tie!")
    playsound('drow.mp3')    
elif a==True:
    print("You Win!")  
    playsound('wins.mp3')  
elif a==False:
    print("You Lose!")
    if comp=='s':
        playsound('snake.mp3')  
    elif comp=='w':
        playsound('water.mp3')  
    elif comp=='g':
        playsound('pistol.mp3')   

  


  
  


