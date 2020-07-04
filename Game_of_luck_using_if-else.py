name = input("enter your name : ")
num = int(input("enter a number between 1 to 100 : "))
random_num = (len(name) * num) + 2
gussing_num = int(input("enter your gussed number between 1 to 1000 \n your number is : "))
if random_num == gussing_num:
    print("congatulation , You win the game")
elif random_num<gussing_num:
    print("Sorry,number is too high , try next time")
else:
    print("Sorry,number is too low , try next time")
                  
