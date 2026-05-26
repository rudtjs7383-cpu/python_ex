from config_dir.dir import config
from db import memberDB
from db import diaryDB
from member import memberDumy
from member import session
from module.menu_dir_jjh import menuList
from module.menu_dir_jjh import exitMenu
from module.sign_up_lks import signUp
from module.sign_in_ktk import signInModule2
from module.forgotPw_dir_kdm import forgotPW

if config.DEV_MOD:

    memberDumy.dummyInit()

    print(f'memberDB: {memberDB.memberDB}')
    print(f'diaryDB: {diaryDB.diaryDB}')


flag = True

while flag:

    selectedMenu = menuList.showMenu()


    if selectedMenu == config.SIGN_UP:

        signUp.signUp()


    elif selectedMenu == config.SIGN_IN:

        signInModule2.signIn()


    elif selectedMenu == config.PRINT_MY_INFO:

        print('나의 정보 출력 기능')


    elif selectedMenu == config.PRINT_ALL_MEMBER_INFO:

        print('모든 회원 정보 출력 기능')


    elif selectedMenu == config.FIND_ID:

        forgotPW.findID()


    elif selectedMenu == config.FIND_PASSWORD:

        forgotPW.findPassword()


    elif selectedMenu == config.SYSTEM_SHUTDOWN:

        flag = exitMenu.exitMenu()


    else:

        print('잘못된 메뉴 입력입니다.')

