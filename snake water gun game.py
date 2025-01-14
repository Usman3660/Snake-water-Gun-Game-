import random

def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == 0 and user ==1):
    return -1
    
  if(comp == 1 and user ==2):
    return -1
    
  if(comp == 2 and user == 0):
    return -1

  return 1
    
  
comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun 3 to Exit the Game: \n"))

score = check(comp, user)


while(1):
    if(score == 0):
        print("user: ", user)
        print("Computer: ", comp)
        print("Its a draw")
    elif (score == -1):
        print("user Lose")
        print("user: ", user)
        print("Computer: ", comp)
    elif(user==3):
       print("Game Ended")
       quit()
    else:
        print("user: ", user)
        print("Computer: ", comp)
        print("User Won")
  

