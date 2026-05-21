members = {}
# 회원가입 기능
def signUp():
    global members
    print('\n[회원가입]')
# ID 입력 및 중복 체크
def userid():

   while True:
    userid = input('회원 ID 입력: ')

    if userid in members:
        print("이미 사용중인 ID입니다. 다시 입력하세요.")
    else:
        break 
# 비밀번호 지정 함수
def SetPassword():
    
    while True:
        
        Pw = input('회원 비밀번호 입력: ')   

# 이메일 형식 검사
def useremail():

  while True:
    useremail = input('회원 Email 입력: ')
    
    if "@" in useremail and "." in useremail:
        break
    else:
        print("올바른 이메일 형식이 아닙니다. 다시 입력하세요.")

# 전화번호 '-' 자동 제거
def userphone():
    userphone = input("전화번호를 입력하세요: ")
    return userphone('-', "")

userphone = input('회원 phone 입력: ')
userphone = userphone.replace('-', "")


 


