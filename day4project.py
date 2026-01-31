import random
user_choice=int(input("What do you choose?Type 0 for Rock,Type 1 for Paper,Type 2 for scissor::"))
rock='''
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor='''

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
first_list=["Rock","Paper","Scissor"]
list1=[rock,paper,scissor]

if user_choice < 0 or user_choice > 2:
    print("Invalid input. You lose!")
else:
    first_userchoice=first_list[user_choice]
    user_choice2=list1[user_choice]
    print(f"You chose {first_userchoice} {user_choice2}")
    comp_choice=random.randint(0,2)
    firstcomp_choice=first_list[comp_choice]
    comp_choice2=list1[comp_choice]
    print(f"Computer choose {firstcomp_choice} {comp_choice2}")
    
       
    if(comp_choice==user_choice):
        print("Draw match")
    elif(user_choice==0 and comp_choice==2):
        print("You win")
    elif(user_choice==2 and comp_choice==0):
        print("Computer wins")
    elif(comp_choice>user_choice):
        print("Computer wins")
    elif(user_choice>comp_choice):
        print("You win")