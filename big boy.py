print("Welcome to my fun little quiz")
answer = input("Do you wanna play? ")

score = 0

if answer.lower() != ("yes" and "y") :
    print("It was nice knowing you :( ")
    
    quit()

else:
    print("Okay let's paly :)")

answer = input("What is full form of CPU? ")

if answer.lower() == ("central processing unit"):
    print("Correct!")
    score += 1
else: print("Incorrect")

answer = input("What is full form of GPU? ")

if answer.lower() == ("graphics processing unit"):
    print("Correct!")
    score += 1
else: print("Incorrect")

answer = input("What is full form of RAM? ")

if answer.lower() == ("random access memory"):
    print("Correct!")
    score += 1
else: print("Incorrect")

answer = input("What is full form of PSU? ")

if answer.lower() == ("power supply unit"):
    print("Correct!")
    score += 1
else: print("Incorrect")

print("You got " + str(score) + "  questions correct!")
print("and " + str(4-score) + " incorrect")
print("And you got " + str((score/4)*100) + " %")

print("Have a nice day ~_~ bye!")

input("")
quit()



