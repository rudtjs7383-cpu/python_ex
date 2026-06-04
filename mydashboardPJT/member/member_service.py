import os
import json
import member.config as root_config
import member.config as config  # 💡 안전하게 패키지 경로 명시
import session
from util import util_time  


class MemberService:
    def __init__(self):
        self.members = {}
        self.init_database()

    # 회원 가입 기능
    def sign_up(self):
        mId = input('Input new member ID: ')

        # ID 중복 체크
        if mId in self.members:
            print('이미 사용중인 id 입니다.')
            return

        mPw = input('Input new member PW: ')
        mMail = input('Input new member MAIL: ')
        mPhone = input('Input new member PHONE: ')

        newMember = {
            'mId': mId,
            'mPw': mPw,
            'mMail': mMail,
            'mPhone': mPhone,
            'mRegDate': util_time.getCurrentDateTime(),
            'mModDate': util_time.getCurrentDateTime(),
        }

        self.members[mId] = newMember

        # DB(members.json)에 새 회원 정보 저장
        self.save_members(self.members)
        print('MEMBER SIGN-UP SUCCESS!!')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')

    # 회원 로그인 기능
    def sign_in(self):
        mId = input('Input member ID: ')
        mPw = input('Input member PW: ')

        self.members = self.load_members()
        if mId in self.members and self.members[mId]['mPw'] == mPw:
            print('로그인에 성공하였습니다.')
            session.setSignInedMemberId(mId)

            if root_config.DEV_MOD:
                # 💡 [수정] 직접 변수 접근 대신 Getter 함수 사용
                print(f'session.signInedMemberId: {session.getSignInedMemberId()}')
        else:
            print('ID 또는 PW 가 일치하지않습니다.')

    # 회원 로그아웃 기능
    def sign_out(self):
        session.setSignInedMemberId('')
        print('로그아웃이 성공적으로 되었습니다.')

    # 회원 정보수정 기능
    def modify(self):
        current_user = session.getSignInedMemberId()
        if current_user == '':
            print('로그인이 필요한 서비스입니다.')
            return

        mPw = input('Input new member PW: ')
        mMail = input('Input new member MAIL: ')
        mPhone = input('Input new member PHONE: ')

        self.members = self.load_members()
        memberForModify = self.members[current_user]
        memberForModify['mPw'] = mPw
        memberForModify['mMail'] = mMail
        memberForModify['mPhone'] = mPhone
        memberForModify['mModDate'] = util_time.getCurrentDateTime()

        self.save_members(self.members)
        print('회원 정보가 성공적으로 수정되었습니다.')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')

    # 회원 탈퇴 기능
    def delete(self):
        current_user = session.getSignInedMemberId()
        if current_user == '':
            print('로그인이 필요한 서비스입니다.')
            return

        confirm = input('정말 탈퇴하시겠습니까? [Y] or [N]: ')
        
        # 💡 [수정] != 'Y'에서 == 'Y'로 수정 (대소문자 무관하게 처리)
        if confirm.upper() == 'Y':
            self.members = self.load_members()
            if current_user in self.members:
                del self.members[current_user]
                self.save_members(self.members)
                session.setSignInedMemberId('')  # 탈퇴 후 세션 비우기
                print('회원 탈퇴가 성공적으로 되었습니다.')
            else:
                print('회원 정보를 찾을 수 없습니다.')
        else:
            print('회원 탈퇴가 취소되었습니다.')

        if root_config.DEV_MOD:
            print(f'self.load_members(): {self.load_members()}')

    def run(self):
        flag = True
        while flag:
            # 💡 [수정] 직접 변수 접근 대신 Getter 함수 사용
            if session.getSignInedMemberId() == '':
                try:
                    menuNum = int(input('\n1.SIGN-UP    2.SIGN-IN    99.SERVICE-OUT: '))
                except ValueError:
                    print('숫자를 입력해주세요.')
                    continue
            else:
                try:
                    menuNum = int(input('\n3.SIGN-OUT    4.MODIFY    5.DELETE    99.SERVICE-OUT: '))
                except ValueError:
                    print('숫자를 입력해주세요.')
                    continue

            if menuNum == config.SIGN_UP:
                self.sign_up()
            elif menuNum == config.SIGN_IN:
                self.sign_in()
            elif menuNum == config.SIGN_OUT:
                self.sign_out()
            elif menuNum == config.MODIFY:
                self.modify()
            elif menuNum == config.DELETE:
                self.delete()
            elif menuNum == config.SERVICE_OUT:
                flag = False
                print('MEMBER SERVICE CLOSED.')

    def init_database(self):
        BASE_PATH = os.path.dirname(os.path.abspath(__file__))
        print(f'BASE_PATH: {BASE_PATH}')

        ROOT_DIR = os.path.dirname(BASE_PATH)
        print(f'ROOT_DIR: {ROOT_DIR}')

        # db 폴더 자동 생성 장치 추가 (안전망)
        db_dir = os.path.join(ROOT_DIR, 'db')
        if not os.path.exists(db_dir):
            os.makedirs(db_dir)

        self.dbFile = os.path.join(db_dir, 'members.json')
        print(f'self.dbFile: {self.dbFile}')

        if not os.path.exists(self.dbFile):
            self.save_members(self.members)
        else:
            self.members = self.load_members()

    # JSON 파일 저장
    def save_members(self, members):
        with open(self.dbFile, 'w', encoding='utf-8') as f:
            json.dump(members, f, ensure_ascii=False, indent=4)

    def load_members(self):
        with open(self.dbFile, 'r', encoding='utf-8') as f:
            return json.load(f)


if __name__ == '__main__':
    memberService = MemberService()
    memberService.run()