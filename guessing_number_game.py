import random #used to generate inputs
random_number = random.randint(1,15) #generate a random number between 1 to 100


def number_game(win_number): #function that does the game
    for i in range(1,7):    #iterating from 1 to 5
        if i == 6:          #when you exhuast 5 chances
            print("sorry you lost your chance")
        else:
            Guessed_number=int(input("please enter a new number  "))
            if Guessed_number == win_number:        
                #if you guess the right number
                print("you won and you guessed the number correctly  ")
                break
            elif Guessed_number < win_number: 
                #when you guessed a lower number than required
                print("choose a higher number  ")
                continue             
            else:
                print("choose a lower number  ")       
                #when you guessed a higher
                continue

number_game(random_number)
