# clearing screen function
import time
import os

colors = {"cyan": "\033[1;36;40m", "reset": "\033[1;32;m"}

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def exit_animation():
    loading_animation('[-_0] - Exiting Program ')
    clear()


def loading_animation(output):
    print(f'{output}', end='', flush=True)
    time.sleep(0.25)
    print('.', end='', flush=True)
    time.sleep(0.5)
    print('.', end='', flush=True)
    time.sleep(0.5)
    print('.', flush=True)
    time.sleep(1)
