from colorama import init
from colorama import Fore, Back, Style

from time import sleep

from random import randint

import os
 
def clearConsole():
    os.system('cls')

def clearConsole():
    print("\033c\033[3J")

def treePage1():
    print(Fore.RED + '     X')
    print(Fore.GREEN + '     ^')
    print(Fore.GREEN + '    ^' + Fore.YELLOW + 'O' + Fore.GREEN + '^')
    print(Fore.GREEN + '   ^^^^^')
    print(Fore.GREEN + '  ^' + Fore.RED + '0' + Fore.GREEN + '^^' + Fore.BLUE + 'o' + Fore.GREEN + '^^')
    print(Fore.GREEN + '    ^^^')
    print(Fore.GREEN + '   ^^^^^')
    print(Fore.GREEN + '  ^^' + Fore.CYAN + 'O' + Fore.GREEN +  '^^' + Fore.RED + 'o' + Fore.GREEN + '^')
    print(Fore.GREEN + ' ^^^^^^^^^')
    print(Fore.MAGENTA + '    |||')
    print(Fore.WHITE + 'Merry X-Mas from A-ST-RA :3')


def treePage2():
    print(Fore.YELLOW + '     X')
    print(Fore.GREEN + '     ^')
    print(Fore.GREEN + '    ^' + Fore.RED + 'O' + Fore.GREEN + '^')
    print(Fore.GREEN + '   ^^^^^')
    print(Fore.GREEN + '  ^' + Fore.YELLOW + '0' + Fore.GREEN + '^^' + Fore.CYAN + 'o' + Fore.GREEN + '^^')
    print(Fore.GREEN + '    ^^^')
    print(Fore.GREEN + '   ^^^^^')
    print(Fore.GREEN + '  ^^' + Fore.WHITE + 'O' + Fore.GREEN +  '^^' + Fore.MAGENTA + 'o' + Fore.GREEN + '^')
    print(Fore.GREEN + ' ^^^^^^^^^')
    print(Fore.MAGENTA + '    |||')
    print(Fore.WHITE + 'Merry X-Mas from A-ST-RA :3')


def treePage3():
    print(Fore.BLUE + '     X')
    print(Fore.GREEN + '     ^')
    print(Fore.GREEN + '    ^' + Fore.BLACK + 'O' + Fore.GREEN + '^')
    print(Fore.GREEN + '   ^^^^^')
    print(Fore.GREEN + '  ^' + Fore.RED + '0' + Fore.GREEN + '^^' + Fore.WHITE + 'o' + Fore.GREEN + '^^')
    print(Fore.GREEN + '    ^^^')
    print(Fore.GREEN + '   ^^^^^')
    print(Fore.GREEN + '  ^^' + Fore.CYAN + 'O' + Fore.GREEN +  '^^' + Fore.BLACK + 'o' + Fore.GREEN + '^')
    print(Fore.GREEN + ' ^^^^^^^^^')
    print(Fore.MAGENTA + '    |||')
    print(Fore.WHITE + 'Merry X-Mas from A-ST-RA :3')


init()
clearConsole()
while (True):
    treePage1()
    sleep(randint(1, 3))
    clearConsole()
    treePage2()
    sleep(randint(1, 3))
    clearConsole()
    treePage3()
    sleep(randint(1, 3))
    clearConsole()