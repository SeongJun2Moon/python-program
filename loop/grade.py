"""
국어. 영어, 수학점수를 입력받아서 학점을 출력하는 프로그램을 완성하시오.
각 과목 점수는 0 ~ 100 사이이다.
평균에 따라 다음과 같이 학점이 결정된다
90이상은 A학점
80이상은 B학점
70이상은 C학점
60이상은 D학점
50이상은 E학점
그 이하는 F학점
출력되는 결과는 다음과 같다.
### 성적표 ###
********************************
이름 국어 영어 수학 총점 평균 학점
*******************************
홍길동 90 90 92 272 90.6 A
********************************
"""

class Grade(object):
    def __init__(self, name, lan, eng, math) -> None:
        self.name = name
        self.lan = lan
        self.eng = eng
        self.math = math

    def print(self):
        ave = (self.lan+self.eng+self.math)/3
        if ave >= 90:
            grade = "A"
        elif ave >=80 and ave < 90:
            grade = "B"
        elif ave >=70 and ave < 80:
            grade = "C"
        elif ave >=60 and ave < 70:
            grade = "D"
        elif ave >=50 and ave < 40:
            grade = "E"
        else:
            grade = "F"
        answer = f"{self.name} {self.lan} {self.eng} {self.math} {self.lan+self.eng+self.math} {ave:.1f} {grade}" 
        print(f"{answer}")

    @staticmethod
    def new_grade():
        name = input("이름: ")
        lan = int(input("국어: "))
        eng = int(input("영어: "))
        math = int(input("수학: "))
        print()
        return Grade(name, lan, eng, math)

    @staticmethod
    def get_grades(ls):
        print("### 성적표 ###\n********************************\n이름 국어 영어 수학 총점 평균 학점\n********************************")
        for i in ls:
            i.print()
        print("********************************\n")

    @staticmethod
    def print_menu():      
        print("###성적표어플###\n1.성적표 등록\n2.성적표 출력\n3.성적표 삭제\n4.종료")
        menu = int(input(f"\n메뉴 선택: "))
        return menu

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Grade.print_menu()
            if menu == 1:
                gd = Grade.new_grade()
                ls.append(gd)
            elif menu == 2:
                Grade.get_grades(ls)
            elif menu == 3:
                print("3.성적표 삭제\n")
            elif menu == 4:
                print("ㅃ2")
                break
            else:
                print("그런거 없음.\n")

Grade.main()