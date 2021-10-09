import random

def rock_paper_scissors():
     player=input('enter r or p or s= ')
     choices=['r','s','p']
     opp=random.choice(choices)
     print('opp=',opp)

     if player==opp:
        return print('same')
     if check_win(player,opp):
        return print('user_win')
               
     if check_win(player,opp) !=True:
        return print('computer_win')

def check_win(user,computer):
    if(user=='r' and computer=='s') or (user=='s' and computer=='p') or (user=='p' and computer=='r'):
        return True
i=0
while(i<5):
    rock_paper_scissors()
    i+=1
    



 




