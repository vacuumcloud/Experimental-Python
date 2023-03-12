import random

top_of_range = input("Type a positive number = ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=0:
        quit()
else:
    print("Type a number next time")        
    quit()

random_number = random.randint(0 , top_of_range)
guesses = 0
while True:
    guesses+=1
    user_guess = input("Make a guess ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type a number next time") 
        continue   

    if user_guess == random_number:
        print("Correct guess")
        break    
    elif user_guess > random_number:
        print("Your guess is above the number")
    else:
        print("Your guess is below the number")    

print("Number of guesses = " ,guesses)