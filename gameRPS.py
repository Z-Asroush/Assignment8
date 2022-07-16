import random

options=['Rock','Paper','Scissor']
scores={'computer':0 , 'user':0}

for i in range(10):
    computer_choice=random.choice(options)
    print(computer_choice)
    user_choice=input('what is your choice?')

    if user_choice=='Rock' and computer_choice=='Paper' or user_choice=='Paper' and computer_choice=='Scissor' or user_choice=='Scissor' and computer_choice=='Rock' :
        print('computer wins')
        scores['computer']+=1
    elif  user_choice=='Rock' and computer_choice=='Scissor' or user_choice=='Paper' and computer_choice=='Rock' or user_choice=='Scissor' and computer_choice=='Paper':
        print('user wins')  
        scores['user']+=1
    elif  user_choice=='Paper' and computer_choice=='Paper' or user_choice=='Rock' and computer_choice=='Rock' or user_choice=='Scissor' and computer_choice=='Scissor':
        print('draw')
    # elif  user_choice=='Rock' and computer_choice=='Rock':
    #     print('draw')
    # elif  user_choice=='Paper' and computer_choice=='Rock':
    #     print('user wins')  
    #     scores['user']+=1 
    # elif  user_choice=='Paper' and computer_choice=='Scissor':  
    #     print('computer wins')
    #     scores['computer']+=1  
    # elif  user_choice=='Scissor' and computer_choice=='Rock':  
    #     print('computer wins')
    #     scores['computer']+=1
    # elif  user_choice=='Scissor' and computer_choice=='Paper':
    #     print('user wins')  
    #     scores['user']+=1 
    # elif  user_choice=='Scissor' and computer_choice=='Scissor':
    #     print('draw')        
                 
if scores['computer']>scores['user']:
    print('hoooora...computer wins')
elif scores['computer']<scores['user']:
    print('hoooora...user wins') 
elif scores['computer']==scores['user']:
    print('draw')        