from randomlist import RandomList

class OddEven(object):
    def __init__(self) -> None:
        pass

    def print(self):
        random = RandomList()
        for i in random.get_random(1,101,10):
            print(i)

    @staticmethod
    def main():
        oddEven = OddEven()
        oddEven.print()

OddEven.main()
