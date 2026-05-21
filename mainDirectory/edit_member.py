# 수정 메뉴 번호
CHANGE_PASSWORD = '1'
CHANGE_EMAIL    = '2'
CHANGE_PHONE    = '3'


# 더미 데이터 (테스트용)
def inject_dummy_data(members):

    members['kyle01'] = {
        'pw': '1234',
        'email': 'kyle@test.com',
        'phone': '01012345678'
    }

    members['hong02'] = {
        'pw': 'abcd',
        'email': 'hong@test.com',
        'phone': '01098765432'
    }

    members['lee03'] = {
        'pw': 'pass',
        'email': 'lee@test.com',
        'phone': '01055556666'
    }

# 본인 확인 (ID + PW)
def verify_member(members):
    while True:
        user_id = input('회원 ID: ')
        if user_id in members:
            break
        print('없는 ID입니다.')

    user_pw = input('비밀번호: ')
    if members[user_id]['pw'] != user_pw:
        print('비밀번호가 틀렸습니다.')
        return None

    return user_id


# 수정 기능 3가지
def change_password(members, user_id):
    members[user_id]['pw'] = input('새 비밀번호: ')
    print('변경 완료')

def change_email(members, user_id):
    members[user_id]['email'] = input('새 이메일: ')
    print('변경 완료')

def change_phone(members, user_id):
    members[user_id]['phone'] = input('새 전화번호: ').replace('-', '')
    print('변경 완료')


# 메인 수정 함수
def editInfo(members):
    print('\n[회원 정보 수정]')

    user_id = verify_member(members)
    if user_id is None:
        return

    print('1.비밀번호  2.이메일  3.전화번호')
    choice = input('선택: ')

    actions = {
        CHANGE_PASSWORD: change_password,
        CHANGE_EMAIL:    change_email,
        CHANGE_PHONE:    change_phone,
    }

    if choice in actions:
        actions[choice](members, user_id)
    else:
        print('잘못된 선택입니다.')