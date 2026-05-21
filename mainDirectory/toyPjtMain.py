from edit_member import inject_dummy_data, editInfo
from sighIn import main

flag = True

SIGN_UP                 = 1
SIGN_IN                 = 2
PRINT_INFO              = 3
EDIT_INFO               = 4
SYSTEM_SHUTDOWN         = 99

#더미 데이터 넣을 공간------------
DEV_MOD = True
members = {}
if DEV_MOD:
    inject_dummy_data(members)
#------------------------------

def logIn():
    main()

def getMenu():
    menu = int(input('1.회원가입 2.로그인 3.회원 조회 4.회원정보 수정 99.종료 : '))
    return menu

while flag:
    userSelectedMenuNum = getMenu()
    
    if userSelectedMenuNum == SIGN_UP:
        pass
    
    elif userSelectedMenuNum == SIGN_IN:
        logIn()
    
    elif userSelectedMenuNum == PRINT_INFO:
        pass
    
    elif userSelectedMenuNum == EDIT_INFO:
        editInfo(members)
    
    elif userSelectedMenuNum == SYSTEM_SHUTDOWN:
        flag = False
        print('안녕히가십시오.')  #프로그램 종료 시에 출력 멘트