from module.menu_dir_jjh import menuList
from module.menu_dir_jjh import exitMenu

while True:

    choice = menuList.showMenu()

    if choice == 0:
        if exitMenu.exitProgram():
            break

        else:
            continue