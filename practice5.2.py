import random
print("Rock  Paper  Scissor")
c=["Rock" , "Paper" , "Scissor"]
for i in range(3):
    User=input("please enter your choice: ")
    Computer=random.choice(c)
    
    if User==Computer:
        print("try again")
    
    elif User=="Paper" and Computer=="Rock":
        print("User win")

    elif User=="Scissor" and Computer=="Rock":
        print("Computer win")

    elif User=="Rock" and Computer=="Paper":
        print("Computer win")

    elif User=="Rock" and Computer=="Scissor":
        print("User win")

    elif User=="Scissor" and Computer=="Paper":
        print("User win")

    elif User=="Paper" and Computer=="Scissor":
        print("Computer win")

