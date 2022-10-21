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
        print(f"아이디:{self.id} 비밀번호:{self.pw} 이름:{self.name}")
    @staticmethod
    def delete_member(ls,name):
        del ls[[i for i,j in enumerate(ls) if name == j.name][0]]

    @staticmethod
    def new_regist():
        id = input("아이디: ")
        pw = input("비밀 번호: ")
        name = input("이름: ")
        print("등록 완료!\n")
        return Member(id, pw, name)

    @staticmethod
    def print_regist(ls):
        [_.print() for _ in ls]

    @staticmethod
    def print_menu():
        print("메뉴를 선택하세요\n1. 회원가입  2. 목록  3. 삭제  4. 종료")
        return int(input("메뉴: "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == 1:
                print("회원 가입")
                mb = Member.new_regist()
                ls.append(mb)
            elif menu == 2:
                print("\n###회원목록###")
                Member.print_regist(ls)
                print()
            elif menu == 3:
                Member.delete_member(ls,input("삭제할 사람: "))
            elif menu == 4:
                print("종료")
                break
            else:print("그런거 없음\n")


Member.main()