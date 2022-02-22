#Grouping script for kata_6 level problems
#https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
#a except b
def array_diff(a, b):
    empty=[]
    for i in a:
        if b.__contains__(i):
            pass
        else:
            empty.append(i)
    return empty
#print(array_diff([1,2],[1]) == [2])
#print(array_diff([1,2,2,2,3],[2]) == [1,3])

#https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python
#value to the left and right are lower
#[1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]}
def pick_peaks(arr):
    default={"pos": [], "peaks": []}
    empty=[]
    for i,j in enumerate(arr):
        if i==0 or i==len(arr)-1:
            pass
        elif arr[i-1]<j and arr[i+1]<=j:
            for k in arr[i+1:]:
                if j<k:
                    break
                elif j>k:
                    default["pos"].append(i)
                    default["peaks"].append(j)
                    break
    return default

def assert_equals(x,y):
    print(x==y)

print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))
assert_equals(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
print("Running tests")


assert_equals(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})
assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})

assert_equals(pick_peaks([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})
assert_equals(pick_peaks([2,1,3,2,2,2,2,5,6]), {"pos":[2], "peaks":[3]})
assert_equals(pick_peaks([2,1,3,2,2,2,2,1]), {"pos":[2], "peaks":[3]})
assert_equals(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
assert_equals(pick_peaks([18, 18, 10, -3, -4, 15, 15, -1, 13, 17, 11, 4, 18, -4, 19, 4, 18, 10, -4, 8, 13, 9, 16, 18, 6, 7]),{'pos': [5, 9, 12, 14, 16, 20, 23], 'peaks': [15, 17, 18, 19, 18, 13, 18]})
assert_equals(pick_peaks([]),{"pos":[],"peaks":[]})
assert_equals(pick_peaks([1,1,1,1]),{"pos":[],"peaks":[]})





