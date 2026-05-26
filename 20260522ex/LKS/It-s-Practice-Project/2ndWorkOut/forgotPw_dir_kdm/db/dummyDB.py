from db import memberDB 


def dummyInit():

    memberDB.members['gildong'] = {

        'uPw': '1234',
        'uMail': 'gildong@gmail.com',
        'uPhone': '010-1234-5678'
    }

    memberDB.members['minsu'] = {

        'uPw': '5678',
        'uMail': 'minsu@gmail.com',
        'uPhone': '010-9999-8888'    
    }

    memberDB.members['chanho'] = {

        'uPw': '5678',
        'uMail': 'chanho@gmail.com',
        'uPhone': '010-3333-4448'    
    }

    memberDB.members['saeri'] = {

        'uPw': '9999',
        'uMail': 'saeri@gmail.com',
        'uPhone': '010-2233-4998'    
    }