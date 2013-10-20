import random
import time
import sys
choise = {'spock-scissors':['w','smashes'],'spock-rock':['w','vaporizes'],'scissors-paper':['w','cuts'],'scissors-lizard':['w','decapitates'],
          'paper-rock':['w','covers'],'paper-spock':['w','disproves'],'rock-lizard':['w','crushes'],'rock-scissors':['w','crushes'],
          'lizard-paper':['w','eats'],'lizard-spock':['w','poisons']}
elements={1:'rock',2:'paper',3:'scissors',4:'lizard',5:'spock'}

def get_randomval():
          ch = random.randint(1,5)
          comp_ch=elements[ch]
          return comp_ch

def get_usr_ch():
    for i in range(5):
        sys.stdout.write(elements[i+1]+"\t\t")
        time.sleep(0.5)
        sys.stdout.flush()
    print()
    cho = int(sys.stdin.readline())
    usr_ch = elements[cho]
    sys.stdout.flush()
    return usr_ch

def rules():
    print("HOW TO PLAY:::==>")
    print("1. Each entity (Rock,Paper,Scissors,Lizard,Spock) are represented by numbers (1,2,3,4,5) respectively.")
    print("2.When you press <Return> key all the 5 entities are displayed one after the other, The end of which you need to enter the number of your choise.")
    print("3.Then the system will tell you if u won or not.")

def game():
    print("ROCK-PAPER-SCISSORS-LIZARD-SPOCK")
    while(True):
        print("1.play  2.how to play")
        print("Seclect an option")
        ch = input()
        if ch=='2':
            rules()
        elif ch=='1':
            print("1.ROCK  2.PAPER  3.SCISSORS  4.LIZARD  5.SPOCK")
            print()
            user_choice = get_usr_ch()
            comp_choice = get_randomval()
            if user_choice == comp_choice:
                print("result tied.. both options are "+user_choice)
            else:
                if comp_choice+"-"+user_choice in choise:
                    list_val = choise[comp_choice+"-"+user_choice]
                    print("YOU: "+ user_choice +  ",\t COMPUTER: " + comp_choice)
                    print(comp_choice + " " + list_val[1] +" " + user_choice )
                    print("YOU LOSE!!!!")
                elif user_choice+"-"+comp_choice in choise:
                    list_val = choise[user_choice+"-"+comp_choice]
                    print("YOU: "+ user_choice +  "\t COMPUTER: " + comp_choice)
                    print(user_choice+ " " + list_val[1]+ " " + comp_choice)
                    print("YOU WIN!!!")
        print("Wanna Play ?? (y/n)")
        ch01 = input()
        if ch01 == 'n' or ch01 == 'N':
            sys.exit(0)

game()








        
