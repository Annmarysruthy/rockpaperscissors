import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

mychoice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if mychoice>=0 and mychoice<=2:
  game = [rock,paper,scissors]
  print(game[mychoice])
  compchoice = random.randint(0,1)
  comp = game[compchoice]
  print("Computer chose: ")
  print(comp)
  if compchoice==mychoice:
    print("it a raw")
  elif mychoice==0 and compchoice==1:
    print("You lose")
  elif mychoice==0 and compchoice==2:
    print("You win")
  elif mychoice==1 and compchoice==0:
    print("You win")
  elif mychoice==1 and compchoice==2:
    print("You lose")
  elif mychoice==2 and compchoice==0:
    print("You lose")
  elif mychoice==2 and compchoice==1:
    print("You win")
else:
  print("Invalid input")
