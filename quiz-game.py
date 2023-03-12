print("Welcome to the simple computer quiz. \nThere are 4 questions and each questions has 2 attempts. \nAll the best!")

playing = input("Do you want to start? (yes/no) ")

if playing.lower() != "yes":
    print("Bye!")
    quit()
print("Lets play!")

score = 0
trial = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
while answer.lower()!= "central processing unit":
    print("Incorrect")
    print("trial 1/2")
    trial += 1
    answer = input("What does CPU stand for? ")
    print("Incorrect")
    print("trial 2/2")
    if trial == 1:
        break

    
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score+=1
while answer.lower()!= "graphics processing unit":
    print("Incorrect")
    print("trial 1/2")
    trial += 1
    answer = input("What does GPU stand for? ")
    print("Incorrect")
    print("trial 2/2")
    if trial == 1:
        break

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
while answer.lower()!= "random access memory":
    print("Incorrect")
    print("trial 1/2")
    trial += 1
    answer = input("What does RAM stand for? ")
    print("Incorrect")
    print("trial 2/2")
    if trial == 1:
        break

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score+=1
while answer.lower()!= "read only memory":
    print("Incorrect")
    print("trial 1/2")
    trial += 1
    answer = input("What does ROM stand for? ")
    print("Incorrect")
    print("trial 2/2")
    if trial == 1:
        break 

print("Your got " +str(score) +" questions correct! ")
print("Percentage: " +str((score/4) * 100) +"%")