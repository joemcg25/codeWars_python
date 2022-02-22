#https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python
def digitize(n):
    return [int(i) for i in reversed(str(n))]


print(digitize(35231))
print(digitize(0))
print(digitize(23582357))
print(digitize(984764738))
print(digitize(45762893920))
print(digitize(548702838394))