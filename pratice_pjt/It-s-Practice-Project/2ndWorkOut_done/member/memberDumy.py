from db import memberDB
from db import diaryDB


dummyMembers = {

    'gildong': {

        'uPw': '1234',
        'uMail': 'gildong@gmail.com',
        'uPhone': '010-1234-5678'

    },

    'minsu': {

        'uPw': '5678',
        'uMail': 'minsu@gmail.com',
        'uPhone': '010-9999-8888'

    },

    'chanho': {

        'uPw': '5678',
        'uMail': 'chanho@gmail.com',
        'uPhone': '010-3333-4448'

    },

    'saeri': {

        'uPw': '9999',
        'uMail': 'saeri@gmail.com',
        'uPhone': '010-2233-4998'

    }

}


def dummyInit():

    for uId, uInfo in dummyMembers.items():

        memberDB.memberDB[uId] = {

            'uId': uId,
            'uPw': uInfo['uPw'],
            'uMail': uInfo['uMail'],
            'uPhone': uInfo['uPhone']

        }

        diaryDB.diaryDB[uId] = []