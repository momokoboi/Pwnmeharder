'''get email && password both or just one (input)
check if input is in checking pwned websites, if so return the list where they
were found & a tip what to do, how to react
libs: selenium, time, os
make a gui? '''
from os import system, name
from time import sleep
#----------PRE-REQUISITS-----------#
colors = {"cyan":"\033[1;36;40m", "reset":"\033[1;32;m" }
# clearing screen function
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# getting input & cleaning it
clear()
print(f"Please input the {colors['cyan']}email{colors['reset']} you would like to check\n(multiple emails supported, separeted by ',' spaces will be ignored!)")
while True:
    choices = input(f"{colors['cyan']}-_0{colors['reset']} ->  ")
    if choices == "exit" or choices == "quit" or choices =="q":
        break
    elif choices == "HY":
        print("printing hy: ")
        sleep(1)
        print("hy")
    else:
        pass