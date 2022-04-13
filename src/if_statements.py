#############################
# Collaborators: (enter people or resources who/that helped you)
# If none, write none
#
#
#############################
play = input("Do you want to play? ")
if play == "No" or play == "no" or play == "NO":
    print("I'm offended, GO AWAYYYYY. ")
elif play == "Yes" or play == "yes" or play == "YES":   #elif = Else if
    print("Great, lets go! ")
else:
    print("Say yes or no, plz!")

num = int(input("Enter your favorite number: "))
if num % 2 == 0:
    print("even!")
else:
    print("Odd!")