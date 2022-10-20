"""
이름, 주민번호, 주소를 입력받아서
회원명부를 관리하는 어플을 제작하고자 한다.

출력되는 결과는 다음과 같다

### 자기소개어플 ###
********************************
이름: 홍길동
나이: 25세 (만나이)
성별: 남성
주소: 서울
*******************************
"""

class Intro(object):
    def __init__(self, name, ssn, adr) -> None:
        self.name = name
        self.ssn = ssn
        self.adr = adr
    
    def execute(self):
        self.print_intro()

    def set_age(self):
        num = self.ssn.split('-')[0][0:2]
        if int(num[0]) > 2 and int(num[0]) < 10:
            age = 122 - int(num)
        else:
            age = 22 - int(num)

        return f"{age}세 (만나이)"

    def set_gen(self):
        who = self.ssn.split('-')[1][0]
        if who == "1" or who == "3":
            gen = "남자"
        else:
            gen = "여자"
        return gen

    def set_answer(self):
        return f"이름: {self.name}\n나이: {self.set_age()}\n성별: {self.set_gen()}\n주소: {self.adr}"

    def print_intro(self):
        title = "### 자기소개어플 ###"
        astar = "********************************"
        answer = self.set_answer()
        print(f"{title}\n{astar}\n{answer}\n{astar}")

    @staticmethod
    def main():
        name = input("이름: ")
        ssn = input("주민번호: ")
        adr = input("주소: ")
        intro = Intro(name, ssn, adr)
        intro.execute()

Intro.main()