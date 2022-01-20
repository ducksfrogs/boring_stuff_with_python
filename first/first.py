#!/bin/python


def spam(divide_by):
    return 42 / divide_by


print(spam(2))
print(spam(5))


def spam2(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print("Invalid number")


print(spam2(3))
print(spam2(0))
