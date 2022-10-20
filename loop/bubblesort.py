class Bubble(object):
    def __init__(self) -> None:
        pass

    def print(self):
        print("하이")

    @staticmethod
    def main():
        bb = Bubble()
        bb.print()

Bubble.main()