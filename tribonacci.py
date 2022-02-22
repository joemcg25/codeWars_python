#https://www.codewars.com/kata/556deca17c58da83c00002db/train/python
def tribonacci(signature, n):
    while len(signature)<n:
        signature.append(sum(signature[-3:]))
    return signature[0:n]
print(tribonacci([0,0,1],10))