# ...
# 이름, 전화번호, 이메일, 주소를 받아서
# 연락처 입력, 출력, 삭제하는 프로그램을 개발하시오
# 단, 인명은 여러명 저장 가능합니다.
# ...

from typing import Container


class Contract(object):
    
    def __init__(self, name, pnum, mail, adrr) -> None:
        self.name = name
        self.pnum = pnum
        self.mail = mail
        self.adrr = adrr
        

    @staticmethod
    def new_contact():
        name = input("이름:")
        pnum = input("전화번호:")
        mail = input("이메일:")
        adrr = input("주소:")
        return Contract(name, pnum, mail, adrr)

    def print_info(self):
        print(f"{self.name} {self.pnum} {self.mail} {self.adrr}\n")

    @staticmethod
    def get_contacts(ls):
        for i in ls:
            i.print_info()

    @staticmethod
    def print_menu():
        print("1.연락처 등록")
        print("2.연락처 출력")
        print("3.연락처 삭제")
        print("4.종료")
        menu = int(input(f"\n메뉴 선택: "))
        return menu

    @staticmethod    
    def main():
        ls = []
        while True:
            menu = Contract.print_menu()
            if menu == 1:
                print("1.연락처 등록\n")
                contact = Contract.new_contact()
                ls.append(contact)
                print()
            elif menu == 2:
                print("2.연락처 출력\n")
                Contract.get_contacts(ls)
            elif menu == 3:
                print("3.연락처 삭제\n")
            elif menu == 4:
                print("4.종료")
                break
            else:
                print("그런거 없음.\n")
                
        

Contract.main()