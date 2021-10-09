import random
i=0

def chek_win1(user,computer1,computer2):
    if(user=='backhand' and computer1=='underhand' and computer2=='underhand') or (user=='underhand' and computer1=='backhand' and computer2=='backhand'):
        return True
def chek_win2(user,computer1,computer2):
    if(computer1=='underhand' and computer2=='backhand' and user=='backhand') or (computer1=='backhand' and computer2=='underhand' and computer2=='underhand'):
        return True
def chek_win3(user,computer1,computer2):
    if(computer2=='backhand' and computer1=='underhand' and user=='underhand') or (computer2=='underhand' and computer1=='backhand' and user=='backhand'):
        return True
def palam_pulum_pilish():
    player=input('Enter user (backhand or underhand)= ')
    choices=['backhand','underhand']
    op1=random.choice(choices) 
    print('computer1= ',op1)       
    op2=random.choice(choices)
    print('computer2= ',op2)

    if(player==op1 and player==op2):
        return print('same')
    if chek_win1(player,op1,op2):
        return print('user_win')
    if chek_win2(player,op1,op2):
        return print('computer1_win')
    if chek_win3(player,op1,op2):
        return print('computer2_win')

while(i<5):
    palam_pulum_pilish()
    i+=1



