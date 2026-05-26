from practice import showMenu
from practice2 import exitMenu

while True:

    choice = showMenu()

    if choice == 0:
        if exitMenu():
            break

        else:
            continue