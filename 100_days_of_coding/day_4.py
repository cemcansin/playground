import random







rock = '''
    ____r___
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ___p____
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    ___s____
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = ["r", "p", "s"]
ai_pick = random.choice(options)
pick = input("Lets play 'Rock Paper Scissors'\nWhat is your pick:\nr for rock\np for paper\ns for scissors\n")
print(rock, paper, scissors)
if pick == ai_pick:
    print("we got a tie")
if pick == "r" and ai_pick == "p":
    print("You lost, paper beats rock")
if pick == "r" and ai_pick == "s":    
    print("You won, Rock beats scissors")
if pick == "p" and ai_pick == "r":
    print("You won, Paper beats Rock")
if pick == "p" and ai_pick == "s":
    print("You lost, Scissor beats Paper")
if pick == "s" and ai_pick == "p":
    print("You won, Scissor beats Paper")
if pick == "s" and ai_pick == "r":
    print("You lost, Rock beats scissors")