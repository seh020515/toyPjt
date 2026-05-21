members = {}
# 회원가입 기능
def signUp():
    global members
    print('\n[회원가입]')
# ID 입력 및 중복 체크
def user_id():

   while True:
    user_id = input('회원 ID 입력: ')

    if user_id in members:
        print("이미 사용중인 ID입니다. 다시 입력하세요.")
    else:
        break 
# 비밀번호 지정 함수
def SetPassword():
    
    while True:
        
        Pw = input('회원 비밀번호 입력: ')   

# 이메일 형식 검사
def user_email():

  while True:
    user_email = input('회원 Email 입력: ')
    
    if "@" in user_email and "." in user_email:
        break
    else:
        print("올바른 이메일 형식이 아닙니다. 다시 입력하세요.")

# 전화번호 '-' 자동 제거
def user_phone():
    return user_phone('-', "")

user_phone = input('회원 phone 입력: ')
user_phone = user_phone.replace('-', "")


 


