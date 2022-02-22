#https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
#For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
def square_sum(numbers):
    return sum([i**2 for i in numbers])

print(square_sum([1,2]))
print(square_sum([0, 3, 4, 5]))
print(square_sum([]))
print(square_sum([-1,-2]))
print(square_sum([-1,0,1]))