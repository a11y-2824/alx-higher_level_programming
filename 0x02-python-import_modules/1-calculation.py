#!usr/bin/python3
if __name__ == "__main__":
    from calculator_1.py import add
    a = 10
    b = 5
    print("() + () = ()".format(a, b, add(a, b)))

    from calculator_1.py import sub
    a = 10
    b = 5
    print("{} - {} = {}".format(a, b, subtract(a, b)))

    from calculator_1.py import mul
    a = 10
    b = 5
    print("{} * {} = {}".format(a, b, multiply(a, b)))

    from calculator_1.py import div
    a = 10
    b = 5
    print("{} / {} = {}".format(a, b, divide(a, b)))
