class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2
    
    def execute(self):
        num1 = self.num1
        op = self.op
        num2 = self.num2
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        else:
            result = "그런거 없음"
        print(f"{num1} {op} {num2} = {result}")


    @staticmethod
    def new_number():
        num1 = int(input("숫자1: "))
        op = input("+,-,*,/,%: ")
        num2 = int(input("숫자2: "))
        return Calculator(num1,op,num2)

    @staticmethod
    def print_menu():
        print("###성적표어플###\n1.성적표 등록\n2.성적표 출력\n3.성적표 삭제\n4.종료")
        return int(input(f"\n메뉴 선택: "))
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Calculator.print_menu()
            if menu == 1:
                print("등록")
            elif menu == 2:
                print("목록")
            elif menu == 3:
                print("삭제")
            else:print("그런거 없음")

Calculator.main()