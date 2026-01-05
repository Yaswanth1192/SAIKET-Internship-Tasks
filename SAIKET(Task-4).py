import random

secret_number=random.randint(1,100)
guess_count=0
while True:
    guess=int(input("Enter random number between 1,100: "))
    guess_count += 1
    
    if guess >secret_number:
        print("Too high")
    
    elif guess <secret_number:
        print("Too Low")
    
    else:
        print("Congrulations You Guessed The Number")
        print("Total guesses:",guess_count)
        break
    
    