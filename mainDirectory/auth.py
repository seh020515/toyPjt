from database import users

failCount = 0
currentUser = False


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

            print("비밀번호 틀림")
            print(f"실패 횟수: {failCount}")

            return True

    else:
        print("존재하지 않는 아이디")
        return True


def logout():

    global currentUser

    if currentUser == False:
        print("로그인 상태가 아닙니다.")

    else:
        print(f"{currentUser}님 로그아웃")
        currentUser = False