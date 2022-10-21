# ...
# 이름, 전화번호, 이메일, 주소를 받아서
# 연락처 입력, 출력, 삭제하는 프로그램을 개발하시오
# 단, 인명은 여러명 저장 가능합니다.
# ...

from typing import Container

class Contract(object):
    def __init__(self, name, pnum, mail, adrr)->None:
        self.name = name
        self.pnum = pnum
        self.mail = mail
        self.adrr = adrr

    def print_user(self):
        print(self.name, self.pnum, self.mail, self.adrr)

    @staticmethod
    def new_user():
        name = input("이름: ")
        pnum = input("전화번호: ")
        mail = input("이메일: ")
        adrr = input("주소: ")
        return Contract(name,pnum,mail,adrr)

    @staticmethod
    def get_user(ls):
        [_.print_user() for _ in ls]

    @staticmethod
    def print_menu():
        print("\n메뉴 선택 (1.등록 2.보기 3.삭제 4.종료)")
        return int(input("메뉴: "))

    @staticmethod
    def delete_user(ls, name):
        del ls[[i for i,j in enumerate(ls) if j.name == name][0]]

    @staticmethod
    def main():
        ls = []
        while True:
            ct = Contract.print_menu()
            if ct == 1:
                print("연락처 등록")
                nc = Contract.new_user()
                ls.append(nc)
            elif ct == 2:
                Contract.get_user(ls)
            elif ct == 3:
                Contract.delete_user(ls,input("삭제할 이름: "))
            elif ct == 4:
                print("어플 종료")
                break
            else:print("그런거 없음")


Contract.main()