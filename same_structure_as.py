#Same nesting structures and same corresponding length of nested arrays as the first array.
#https://www.codewars.com/kata/520446778469526ec0000001/train/python
def same_structure_as(original,other):
    originalList = isinstance(original, list)
    otherList = isinstance(other, list)
    if originalList:
        original=getLists([],original)
    if otherList:
        other=getLists([],other)
    return original == other

def getLists(empty,listArg):
    empty.append(len(listArg))
    for i in listArg:
        if isinstance(i, list):
            empty.append(len(i))
            getLists(empty,i)
        else:
            empty.append(1)
    return empty


# should return True
print(same_structure_as([1, 1, 1], [2, 2, 2]))

# FALSE
original = [1, 6, 6, [-13, -2], 4, [13, -17, [-2, -14], -1], -10, 1, -15, -16]
other = [18, [8, 16], -20, [-5, [9, 6]], [-8, -15], [[2, -7], -19], -3, 15, 2, [8, 3], 17, -7, 3, 6]
print(same_structure_as(original,other))
print(same_structure_as([1,[1,1]], [[2,2],2]))


#test.assert_equals(same_structure_as([],1), False, "[] not same as 1")
print(same_structure_as([],1))