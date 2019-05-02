#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add
    print("{:d} + {:d} = {:d}".format((a), (b), (a + b)))
    from calculator_1 import sub
    print("{:d} + {:d} = {:d}".format((a), (b), (a - b)))
    from calculator_1 import mul
    print("{:d} + {:d} = {:d}".format((a), (b), (a * b)))
    from calculator_1 import div
    print("{:d} + {:d} = {:.0f}".format((a), (b), (a / b)))
