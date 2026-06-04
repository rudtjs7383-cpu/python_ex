import config
import session
from member import member_service
from bank import bank_service
from memo import memo_service
from todo import todo_service

def main():
    while True:
        current_user = session.getSignInedMemberId()
        status = f"[{current_user}]" if current_user else "[로그인 필요]"
        
        print(f"\n현재 접속: {status}")
        try:
            menuNum = int(input('1. MEMBER    2. BANK    3. MEMO    4. TODO    99. SYSTEM OUT : '))
        except ValueError:
            continue

        if menuNum == config.MEMBER_SERVICE:
            member_service.MemberService().run()

        elif menuNum in [config.BANK_SERVICE, config.MEMO_SERVICE, config.TODO_SERVICE]:
            if not session.getSignInedMemberId():
                print("로그인이 필요한 서비스입니다.")
                continue
            
            if menuNum == config.BANK_SERVICE:
                bank_service.BankService().run()
            elif menuNum == config.MEMO_SERVICE:
                memo_service.MemoService().run()
            elif menuNum == config.TODO_SERVICE:
                todo_service.TodoService().run()

        elif menuNum == config.SYSTEM_OUT:
            break

if __name__ == "__main__":
    main()



































