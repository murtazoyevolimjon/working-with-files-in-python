from os import system
from colorama import Fore, Style
system('clear')
count = int(input(f"{Style.DIM} {Style.BRIGHT}talaba sonini kiriting  "))
s = 0
total = 0
while s != count:
   
    r = range(1, count+1)
    with open("grades.txt", "w") as file:
        name = input(f"{Style.BRIGHT} {Fore.BLUE}talabaning ismini kiriting   ")
        file.write(name + ": ") 
        ball = int(input(f"{Style.BRIGHT} {Fore.BLUE}talaba toplagan ballni kiriting  "))
        file.write(str(ball) + "\n") 
        total += ball
        
    with open("grades.txt", "r") as f:
        
        print(f.read())
    
    average = float(total / count)

    print(f"O'rtacha ball {average}")
    print()
    
    s += 1
    
print(f"{Style.BRIGHT} {Fore.GREEN}exiting   ")