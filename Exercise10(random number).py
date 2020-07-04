import random
number = random.randint(1,5)
k=0
game_over=False
gussing_number = int(input("enter a number between 1 to 100 : "))
while not game_over:
    if number==gussing_number:
        print(f"you win the game! and you gussed the number in {k+1} times")
        game_over=True
    else:
        if number>gussing_number:
            print("your number is too low")
            k +=1
            gussing_number= int(input("guss again "))
        else:
            print("Your number is too high")
            k +=1
            gussing_number= int(input("guss again "))

        
        
