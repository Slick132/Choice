import time
import random
import time



pc_opsies = ['1','2','3','4','5','6','7','8','9']
Gues = 0





def die_hele_program():
    user_getal_keuse = str(input('''Choose a number between 1 and 9
'''))
    pc_keuse = random.choice(pc_opsies)
    if user_getal_keuse == pc_keuse:
        print('You got the awnser right. The awnser is indeed ' + pc_keuse )
        
        
        
            
    else:
        print('Wrong the awnser was ' + pc_keuse + ' and yours was '+ user_getal_keuse )
    time.sleep(0.8)




for i in range(1000):
    die_hele_program()
    Gues +=1

    print('Do you want to exit? (1. Yes / 2. No)')
    user_verlaat = int(input())
    if user_verlaat == 1:
        if Gues == 1:
            print('You took '+ str(Gues)+ ' guess  ')
        else:
            print('You took '+ str(Gues)+ ' guesses  ')
        time.sleep(2)              
        break
        exit
    elif user_verlaat== 2:
        print('Ok cool so lets do it again.')
    else:
        print('I did not understand?')
        print('''So do you want to exit or not?
Do not waste my time I got things to do(1. Yes / 2. No)''')
        user_verlaat_2 = int(input())
        if user_verlaat_2 == 1:
            if Gues == 1:
                print('You took '+ str(Gues)+ ' guess  ')
            else:
                print('You took '+ str(Gues)+ ' guesses  ')
            time.sleep(2)
            break
            exit
        
    




        
    

