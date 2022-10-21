'''
키와 몸무게를 입력받아서 비만도를 측정하는 프로그램을 완성하시오.
BMI 지수를 구하는 공식은 다음과 같다.
BMI지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))
BMI 지수에 따른 결과는 다음과 같다.
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
이름, 키, 몸무게를 입력받으면 다음과 같이 출력되도록 하시오.
### 비만도 계산 ###
***************************
이름 키(cm) 몸무게(kg) 비만도
***************************
홍길동 170 79 정상
***************************
'''
class Bmi(object):
    def __init__(self, name, cm, kg) -> None:
        self.name = name
        self.cm = cm
        self.kg = kg

    def get_biman(self):
        kg = self.kg
        m = self.cm / 100
        bmi = kg / m ** 2
        if bmi >= 35:
            biman = "고도비만"
        elif bmi >= 30:
            biman = "중(重)도 비만 (2단계 비만)"  
        elif bmi >= 25:
            biman = "경도 비만 (1단계 비만)" 
        elif bmi >= 23:
            biman = "과체중" 
        elif bmi >= 18.5:
            biman = "정상" 
        else:
            biman = "저체중" 
        return biman

    def print_biman(self):
        name = self.name
        cm = self.cm
        kg = self.kg
        biman = self.get_biman()
        title = "### 비만도 계산 ###"
        aster = "*"*40
        schema = "이름 키(cm) 몸무게(kg) 비만도"
        result = f"{name} {cm} {kg} {biman}"
        print(f'{title} \n {aster} \n {schema} \n {aster} \n {result} \n {aster} ')

    @staticmethod
    def new_bmi():
        name = input("이름: ")
        cm = int(input("키: "))
        kg = int(input("몸무게: "))
        return Bmi(name, cm, kg)
    @staticmethod
    def get_bmi(ls):
        for i in ls:
            i.print_biman()
    @staticmethod
    def print_menu():
        print("###비만도 등록표###\n1.비만도 등록\n2.비만도 출력\n3.비만도 삭제\n4.종료")
        return int(input(f"\n메뉴 선택: "))
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Bmi.print_menu()
            if menu == 1:
                b = Bmi.new_bmi()
                ls.append(b)
                print('등록')
            elif menu == 2:
                Bmi.get_bmi(ls)
                print("목록")
            elif menu == 3:
                print("삭제")
            else: print("그런거없음")

Bmi.main()