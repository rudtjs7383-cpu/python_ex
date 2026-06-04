import os
import json
import session
from todo import config as todo_config
import config as root_config
from util import util_time

class TodoService:
    def __init__(self):
        self.todos = {}
        self.init_database()

    def init_database(self):
        # 현재 파일 위치
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        # 프로젝트 루트 경로
        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        # db/accounts.json
        self.dbFile = os.path.join(ROOT_DIR, 'db', 'todos.json')
        print(f'self.dbFile: {self.dbFile}')
        # C:\kmh\python\python_ex\myDashboradPjt\db\todos.json

        # 파일 존재 여부 확인
        if not os.path.exists(self.dbFile):
            self.save_todos(self.todos)
        else:
            self.todos = self.load_todos()

    # JSON 파일 저장
    def save_todos(self, todos):   # {}
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(todos, f, ensure_ascii=False, indent=4)

    def load_todos(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)
        
    def isMyTodos(self):
        allTodos = self.load_todos()
        if session.getSignInedMemberId() in allTodos:
            return True
        
        return False
    
    def run(self):
        
        if session.getSignInedMemberId() == '':
            print('Please Sign-in')
            return

        flag = True
        while flag:
            if not self.isMyTodos():
                self.todos[session.getSignInedMemberId()] = []
                self.save_todos(self.todos)

            menuNum = int(input('1.WRITE    2.READ    3.UPDATE    4.DELTE    5.COMPLETE-CHANGE    99.SERVICE-OUT '))
            if menuNum == todo_config.WRITE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]

                tText = input('Input new todo text: ')
                tExpDate = input('Input todo experation date(2026-08-05 06:09:09)')

                todo = {
                    'tTxt': tText,
                    'tExpDate': tExpDate,
                    'tRegDate': util_time.getCurrentDateTime(),
                    'tModDate': util_time.getCurrentDateTime(),
                    'tComplete': False
                }

                myTodos.insert(0, todo)
                self.save_todos(self.todos)
                print('WRITE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos(): {self.load_todos()}')

            elif menuNum == todo_config.READ:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx,myTodo in enumerate(myTodos):
                    print('-' * 50)
                    print(f"[{idx+1}]")
                    print(f"TEXT : {myTodo['tText']}")
                    print(f"EXPIRATIONDATE:{myTodo['tExpDate']}")
                    print(f"REGISTRY DATE : {myTodo['REGISTRYdate']}")
                    print(f"MODIFY DATE : {myTodo['MODIFYdate']}")
                    print(f"COMPLETE:{myTodo['COMPLETE']}")
                    print('-'*50)

            elif menuNum == todo_config.UPDATE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx , myTodo in enumerate(myTodos):
                    print('-'*100)
                    print(f"[{idx+1}]{myTodo['tTxt']}[{myTodo['tExpDate']}][{myTodo['MODIFYdate']}][{myTodo['COMPLETE']}]")
                    print('-'*100)

                todoNumber = int(input('Enter the todo number:')) 
                tText = input('Input todo Text')
                tExpDate = input('Input todo  experation date(YYYY-MM-DD HH:MM:SS)')
                todo = {
                'tTxt': tText,
                 'tExpDate': tExpDate,
                 'tRegDate': myTodos[todoNumber-1]['tRegDate'],
                 'tModDate': util_time.getCurrentDateTime(),
                 'tComplete': myTodos[todoNumber-1]['tComplete']
                }

                myTodos[todoNumber-1] = todo
                self.save_todos(self.todos)
                print('UPDATE SUCCESS!!!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos(): {self.load_todos()}')



                elif menuNum == todo_config.DELETE:
                 self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx , myTodo in enumerate(myTodos):
                    print('-'*100)
                    print(f"[{idx+1}]{myTodo['tTxt']}[{myTodo['tExpDate']}][{myTodo['MODIFYdate']}][{myTodo['COMPLETE']}]")
                todoNumber = int(input('Enter the todo number:'))
                del myTodos[todoNumber-1]
                self.save_todos(self.todos)
                print('DELETE SUCCESS!!')

                if root_config.DEV_MOD:
                    print(f'self.load_todos(): {self.load_todos()}')        


            elif menuNum == todo_config.COMPLETE_CHANGE:
                self.todos = self.load_todos()
                myTodos = self.todos[session.getSignInedMemberId()]
                for idx , myTodo in enumerate(myTodos):
                    print('-'*100)
                    print(f"[{idx+1}]{myTodo['tTxt']}[{myTodo['tExpDate']}][{myTodo['MODIFYdate']}][{myTodo['COMPLETE']}]")
                    
                    todoNumber = int(input('Enter the todo number:'))
               
                    myTodos[todoNumber-1]['tComplete'] = not myTodos[todoNumber-1]['tComplete']
                    self.save_todos(self.todos)
                    print('COMPLETE CHANGE SUCCESS!!')

                    if root_config.DEV_MOD:
                        print(f'self.load_todos(): {self.load_todos()}')
                        
            
               



            elif menuNum == todo_config.SERVICE_OUT:
                flag = False

if __name__ == '__main__':
    todoService = TodoService()
    todoService.run()