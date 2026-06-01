import os
import json
from member import member_service
from bank import bank_service
from bank import bank_config

def main():
    flag = True
    while flag:
        menuNum = int(input('1. MEMBER    2. BANK    3. MEMO    4. TODO    99. SYSTEM OUT : '))
        
        if menuNum == bank_config.MEMBER_SERVICE:
            memberService = member_service.MemberService()
            memberService.run()

        elif menuNum == bank_config.BANK_SERVICE:
            bankService = bank_service.BankService()
            bankService.run()

        elif menuNum == bank_config.MEMO_SERVICE:
            pass

        elif menuNum == bank_config.TODO_SERVICE:
            pass
            
        elif menuNum == bank_config.SYSTEM_OUT:
            flag = False

if __name__ == "__main__":
    main()

















