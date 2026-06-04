import session
import os
import json
from memo import config as memo_config
import config as root_config

class MemoService:
    def __init__(self):
        self.memos = {}
        self.init_database()

    def init_database(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        ROOT_DIR = os.path.dirname(BASE_PATH)
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'memos.json')

        if not os.path.exists(self.dbFile):
            self.save_memos(self.memos)
        else:
            self.memos = self.load_memos()

    def save_memos(self, memos):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(memos, f, ensure_ascii=False, indent=4)

    def load_memos(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    def isMyMemos(self):
        allMemos = self.load_memos()
        return session.getSignInedMemberId() in allMemos
    
    def run(self):
        current_user = session.getSignInedMemberId()
        
        if current_user == '':
            print('Please SIGN-IN!!')
            return
        
        self.memos = self.load_memos()
        if current_user not in self.memos:
            self.memos[current_user] = []
            self.save_memos(self.memos)
        
        flag = True
        while flag:
            print("\n" + "="*40)
            menuNum = int(input('1.WRITE    2.READ    3.UPDATE    4.DELETE    99.SERVICE-OUT : '))
            print("="*40)
            
            if menuNum == memo_config.WRITE:
                newMemo = input('Write new memo: ')

                self.memos = self.load_memos()
                myMemos = self.memos[current_user]
                myMemos.insert(0, newMemo)

                self.save_memos(self.memos)
                print('WRITE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'-> [DEV] current db: {self.load_memos()}')
                    
            elif menuNum == memo_config.READ:
                self.memos = self.load_memos()
                myMemos = self.memos[current_user]
                
                if not myMemos:
                    print("No memos found.")
                else:
                    for idx, memo in enumerate(myMemos):
                        print(f'[{idx+1}] {memo}')
                
            elif menuNum == memo_config.UPDATE:
                self.memos = self.load_memos()
                myMemos = self.memos[current_user]
                
                if not myMemos:
                    print("No memos to update.")
                    continue
                    
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx+1}] {memo}')

                selectedNumber = int(input('PLEASE SELECT THE NUMBER TO MODIFY: '))
                
                if 1 <= selectedNumber <= len(myMemos):
                    memo = input('Edit Memo: ')
                    myMemos[selectedNumber-1] = memo
                    self.save_memos(self.memos)
                    print('MODIFY SUCCESS!!')
                else:
                    print('Invalid number!')

                if root_config.DEV_MOD:
                    print(f'-> [DEV] current db: {self.load_memos()}')

            elif menuNum == memo_config.DELETE:
                self.memos = self.load_memos()
                myMemos = self.memos[current_user]
                
                if not myMemos:
                    print("No memos to delete.")
                    continue
                    
                for idx, memo in enumerate(myMemos):
                    print(f'[{idx+1}] {memo}')
                    
                selectedNumber = int(input('PLEASE SELECT THE NUMBER TO DELETE : '))
                
                if 1 <= selectedNumber <= len(myMemos):
                    myMemos.pop(selectedNumber - 1) 
                    self.save_memos(self.memos)
                    print('DELETE SUCCESS!!')
                else:
                    print('Invalid number!')
                    
                if root_config.DEV_MOD:
                    print(f'-> [DEV] current db: {self.load_memos()}')

            elif menuNum == memo_config.SERVICE_OUT:
                print("Exit Memo Service.")
                flag = False

if __name__ == '__main__':
    memoService = MemoService()
    memoService.run()