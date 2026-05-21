users = {
    "admin": "1111",
    "pw": "2222"
}

failCount = 0
currentUser = False



def showMenu():
    print("===== 메뉴 =====")
    print("1. 로그인")
    print("2. 로그아웃")
    print("3. 종료")



def login():

    global failCount
    global currentUser

   
    if failCount >= 3:
        print("비밀번호 3회 실패")
        print("프로그램 종료")
        return False

    userId = input("아이디 입력: ")
    userPw = input("비밀번호 입력: ")

   
    if userId in users:

        
        if users[userId] == userPw:

            currentUser = userId
            failCount = 0

            print(f"{currentUser}님 환영합니다!")
            return True

        else:
            failCount += 1

            print("비밀번호가 틀렸습니다.")
            print(f"실패 횟수: {failCount}")

            return True

    else:
        print("존재하지 않는 아이디입니다.")
        return True



def logout():

    global currentUser

    if currentUser == False:
        print("현재 로그인된 사용자가 없습니다.")

    else:
        print(f"{currentUser}님 로그아웃 되었습니다.")
        currentUser = False



def main():

    while True:

        showMenu()

        menu = input("메뉴 선택: ")

        if menu == "1":

            result = login()

            
            if result == False:
                break

        elif menu == "2":
            logout()

        elif menu == "3":
            print("프로그램 종료")
            break

        else:
            print("잘못된 입력입니다.")