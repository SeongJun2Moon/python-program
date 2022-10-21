from random_list import RandomList

class OddEven(object):
    def __init__(self) -> None:
        pass

    def print(self):
        rl = RandomList().get_random(1,100,10)
        print([f"짝수:{i}" if i%2==0 else f"홀수:{i}" for i in rl])

    @staticmethod
    def main():
        oddEven = OddEven()
        oddEven.print()

OddEven.main()
