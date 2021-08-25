from art import logo
import random
print(logo)
def fun1():
 
  rand3 = random.choice(cards)
  user.append(rand3)
loopgame = True
while loopgame:

  tog = input("You want to play game 'y' yes or 'n' no: ").lower()
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  user = []
  comp = []
  ha = True
  result = 0
  cresult = 0
  if tog == 'y':
    
    rand1 = random.choice(cards)
    rand2 = random.choice(cards)
    result = rand1 + rand2
    user.append(rand1)
    user.append(rand2)
    print(f"user cards {user} , score is {result}")

    num = random.randint(2,3)
    
    for i in range(0,num):
      rand = random.choice(cards)
      comp.append(rand)
    for i in comp:
      cresult += i
    print("computer's first hand is:",comp[0])
    
    
    while ha:
      rtoggl = input("type 'y' to get another card or 'n to pass' ").lower()
      if rtoggl == 'y':
        fun1()
        for i in user:
          result += i
        print(f"user cards {user} , score is {result}")
      else:
        ha= False
        print(f"Your final hand is {user} , score is {result}")
        print(f"Computers final hand is {comp} , score is {cresult}")
  if result > 20:
    print("you went over, You lose 😥 ")
  elif cresult > 20:
    print("computer went over, You win 😁")
  elif cresult > result:
    print("You lose 😥")

  elif result > cresult:
    print("You win 😁")
  
  if tog == 'n':
    loopgame = False
  

  

