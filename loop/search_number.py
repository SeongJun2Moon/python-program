"""
두자리 정수 랜덤숫자 10개를 뽑아서
사용자가 검색하는 숫자의 배수만 출력하는
프로그램을 개발하시오.
예) [12,23,48,...,], 입력값 : 12
출력값이 12의 배수만 되도록 한다.
"""

from random_list import RandomList

class SerchNumber(object):
    def __init__(self, num) -> None:
        self.num = num

    def getRandom(self):
        random = RandomList()
        li = random.get_random(1,100,10)
        li = sorted(li)
        return li

    def searchNumber(self):
        li = []
        li2 = self.getRandom()
        print(li2)
        for i in li2:
            if i % self.num == 0:
                li.append(i)
        return li
            
    def print(self):
        print(self.searchNumber())

    @staticmethod
    def main():
        num = int(input("숫자: "))
        serchNumber = SerchNumber(num)
        serchNumber.print()

SerchNumber.main()