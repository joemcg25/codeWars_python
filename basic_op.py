#https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python
def basic_op(operator, value1, value2):
    items="+-*/"
    if not operator in items:
        return 0
    inx=items.index(operator)
    if inx==0:
        return value1+value2
    elif inx==1:
        return value1-value2
    elif inx==2:
        return value1*value2
    else:
        return value1/value2
def basic_op(operator, value1, value2):
    return eval(str(value1) + operator + str(value2))


def assert_equals(x,y):
    if x==y:
        print(True)
    print(False)

assert_equals(basic_op('+', 4, 7), 11)
assert_equals(basic_op('-', 15, 18), -3)
assert_equals(basic_op('*', 5, 5), 25)
assert_equals(basic_op('/', 49, 7), 7)

