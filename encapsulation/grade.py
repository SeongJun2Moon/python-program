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

    def execute(self):
        self.get_answer()
        self.print_grade()


    def get_answer(self):
        lan = self.lan
        eng = self.eng
        math = self.math
        sum = lan+eng+math
        ave = sum/3
        grade = ""
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
        answer = f"{self.name} {lan} {eng} {math} {sum} {ave:.1f} {grade}" 
        return answer

    def print_grade(self):
        title = "### 성적표 ###"
        astar = "********************************"
        cate = "이름 국어 영어 수학 총점 평균 학점"
        answer = self.get_answer()
        print(f"{title}\n{astar}\n{cate}\n{astar}\n{answer}\n{astar}")

    @staticmethod
    def main():
        name = input("이름: ")
        lan = int(input("국어: "))
        eng = int(input("영어: "))
        math = int(input("수학: "))
        grade = Grade(name, lan, eng, math)
        grade.execute()

Grade.main()