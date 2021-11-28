'''get email && password both or just one (input)
check if input is in checking pwned websites, if so return the list where they
were found & a tip what to do, how to react
libs: selenium, time, os
make a gui? '''
import console_utilities
from console_utilities import colors
import input_processor


# ----------PRE-REQUISITS-----------#


# choice cleaning function


def choice_clean(_input):
    clean_choice = _input.split()
    return clean_choice


# getting input & cleaning it
console_utilities.clear()
print(
    f"Please input the {colors['cyan']}email{colors['reset']} you would like to check\n(multiple emails supported,"
    f" separated by ',' spaces will be ignored!)")
while True:
    choices = choice_clean(input(f"{colors['cyan']}-_0{colors['reset']} ->  "))
    command = choices[0]
    if command == "exit" or command == "quit" or command == "q":
        console_utilities.exit_animation()
        break
    elif command == "email":
        input_processor.process_email(choices[1:])

    else:
        pass
