class Born(object):
    
    def __init__(self) -> None:
        pass

    def print(self):
        print("hi")

    @staticmethod
    def main():
        born = Born()
        born.print()

Born.main()