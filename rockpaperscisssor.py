import random
while True:
 choices=["rock","paper","scissors"]

 Bot=random.choice(choices)
 player=input("rock,paper or scissors:")
 while True:
    if player in choices:
        print('player :',player)
        print("Bot :",Bot)
    else:
       print("invalid")
       break
    if player==Bot:
      print("tie")
      break
    elif player=='rock' and Bot== "scissors":
      print("you win")
      break
    elif player=='paper' and Bot== "rock":
      print("you win")
      break
    elif player=='scissor' and Bot== "paper":
      print("you win")  
      break      
    else:
      print("you lose")
      break
 play_again=input("want to play again(yes/no): ")   
 if play_again=='no':
  break      
