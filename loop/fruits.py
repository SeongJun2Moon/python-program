"""
과일판매상에서 메뉴를 진열하는 어플을 제작하고자 한다.
입력되는 값은 없다.
다만, 실행했을 때 출력되는 결과는 다음과 같다.
### 과일번호표 ###
********************************
1번과일: 바나나
2번과일: 사과
3번과일: 망고
********************************
구매할 과일: 바
바나나
"""
class Fruits(object):

    def __init__(self, search) -> None:
        self.menu = ["바나나", "사과나", "망고"]
        self.search = search
    
    def getAnswer(self):
        answer = ""
        num = 1
        for i in self.menu:
            fruit = f"{num}번과일: {i}\n"
            answer+=fruit
            num += 1
        return answer
        
    def searchFruits(self):
        li = []
        for i in self.menu:
            if self.search in i:
                li.append(i)
        return li

    def print_menu(self):
        print("### 과일번호표 ###")
        print("********************************")
        print(f"{self.getAnswer()}********************************")
        print(f"구매할과일: {self.search}")
        print(self.searchFruits())
    
    @staticmethod
    def main():
        search = input("검색: ")
        fruits = Fruits(search)
        fruits.print_menu()

Fruits.main()