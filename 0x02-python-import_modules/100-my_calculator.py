#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = int()
    b = int()

if op == '+':
    print("{} + {} = {}".format(a, b, add(a, b)))
elif op == '-':
    print("{} - {} = {}".format(a, b, sub(a, b)))
elif op == '*':
    print("{} * {} = {}".format(a, b, mul(a, b)))
elif op == '/':
    print("{} / {} = {}".format(a, b, div(a, b)))
