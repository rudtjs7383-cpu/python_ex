import bank as bank_config
import session
import os
import json
import uuid


class BankService:
    def __init__(self):
        self.accounts = {}
        self.init_database()

    def init_database(self):
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH:{BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR:{ROOT_DIR}')

        self.dbFile = os.path.join(ROOT_DIR, 'db', 'accounts.json')

        if not os.path.exists(self.dbFile):
            self.save_accounts(self.accounts)
        else:
            self.accounts = self.load_accounts()

    # json 에 저장
    def save_accounts(self, accounts):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(accounts, f, ensure_ascii=False, indent=4)

    def load_accounts(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
            
    def isMyAccount(self):
        allAccount = self.load_accounts()
        current_user = session.getSignInedMemberId()
        # 로그인한 회원의 계좌 딕셔너리가 존재하고, 그 내부에 계좌가 1개 이상 있을 때 True
        if current_user in allAccount and len(allAccount[current_user]) > 0:
            return True
        return False

    def run(self):
        if session.getSignInedMemberId() == '':
            print('로그인 후 이용 부탁드립니다.')
            return

        flag = True
        while flag:
            current_user = session.getSignInedMemberId()
            
            if self.isMyAccount():
                try:
                    menNum = int(input('\n1.계좌목록   2.신규개설   3.입금   4.출금   0.메인메뉴로: '))
                except ValueError:
                    print('숫자를 입력해주세요.')
                    continue
            else:
                print('\n계좌가 없습니다. 신규 개설 후 이용 부탁드립니다.')
                try:
                    menNum = int(input('2.신규개설   0.메인메뉴로: '))
                except ValueError:
                    print('숫자를 입력해주세요.')
                    continue

            if menNum == bank_config.ACCOUNT_LIST:
                pass

            elif menNum == bank_config.NEW_ACCOUNT:
                self.accounts = self.load_accounts()
                
                # 대소문자 오타 수정 (getsignInedMemberId -> getSignInedMemberId)
                if current_user not in self.accounts:
                    self.accounts[current_user] = {}

                myAccounts = self.accounts[current_user]
                
                # 💡 [잔액 기능 반영] 신규 계좌 개설 시 balance: 0 필드 추가
                new_account_number = str(uuid.uuid4())
                myAccounts[new_account_number] = {
                    "balance": 0
                }
                
                # 변경된 계좌 정보를 파일에 즉시 반영
                self.save_accounts(self.accounts)
                print(f'\n계좌가 신규 개설되었습니다!')
                print(f'개설된 계좌번호: {new_account_number}')

            elif menNum == bank_config.DEPOSIT:
                pass

            elif menNum == bank_config.WITHDRAWAL:
                pass

            elif menNum == 0 or menNum == bank_config.SERVICE_OUT:
                print('은행 서비스를 종료합니다.')
                flag = False


if __name__ == "__main__":
    bankService = BankService()
    bankService.run()