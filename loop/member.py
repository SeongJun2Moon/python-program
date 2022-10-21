# '''
# 아이디, 비밀번호, 이름을 받아서
# 회원가입, 목록, 삭제하는 프로그램을 개발하시오.
# '''

class Member(object):
    def __init__(self, id, pw, name)->None:
        self.id = id
        self.pw = pw
        self.name = name

    def print(self):
        print(self.id, self.pw, self.name)

    @staticmethod
    def new_regist():
        id = input("아이디: ")
        pw = input("비밀 번호: ")
        name = input("이름: ")
        print("등록 완료!")
        return Member(id, pw, name)

    @staticmethod
    def print_regist(ls):
        for i in ls:
            i.print()

    @staticmethod
    def print_menu():
        return int(input("메뉴: "))

    @staticmethod
    def main():
        while True:
            ls = []
            menu = Member.print_menu()
            if menu == 1:
                print("회원 가입")
                mb = Member.new_regist()
                ls.append(mb)
            elif menu == 2:
                print("목록")
                Member.print_regist(ls)
            elif menu == 3:
                print("삭제")
            elif menu == 4:
                print("종료")
                break
            else:print("그런거 없음")


Member.main()