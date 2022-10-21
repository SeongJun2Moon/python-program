class Contacts(object):
    def __init__(self)->None:
        pass

    def print(self):
        pass

    @staticmethod
    def print_menu():
        return int(input("메뉴: "))
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contacts.print_menu()
            if menu == 1:
                print("등록")
            elif menu == 2:
                print("목록")
            elif menu == 3:
                print("닫기")
                break
            else:print("그런거없음")

Contacts.main()