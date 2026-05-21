from auth import login, logout


def show_menu():

    print("\n===== 메뉴 =====")
    print("1. 로그인")
    print("2. 로그아웃")
    print("3. 종료")


def main(members):

    while True:

        show_menu()

        menu = input("메뉴 선택: ")

        if menu == "1":

            result = login(members)

            if result == False:
                break

        elif menu == "2":
            logout()

        elif menu == "3":
            print("프로그램 종료")
            break

        else:
            print("잘못된 입력")
