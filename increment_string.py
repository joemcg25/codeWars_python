#https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
def increment_string(strng):
    digits="" # numbers
    vals = "" # letters
    numLength=0
    val=0
    lastLetter=0
    for i,j in enumerate(strng):
        if not j.isdigit():
            lastLetter=i
    cnter=0
    for i in strng:
        if i.isdigit() and cnter>=lastLetter:
            numLength+=1
            digits+=i
        else:
            vals+=i
        cnter += 1
    if 0==len(digits):
        digits="0"
    val=1+int(digits)
    val = str(val)
    for i in range((numLength-len(val))):
        vals+="0"
    return vals+val

print(increment_string(""))
print(increment_string("foo1"))
print(increment_string("foo001"))
#print(increment_string("foo0012"))
#print(increment_string("foo0999"))

print(increment_string('#92325250lR$o54990000000000093620'))
#'#lR$o9232525054990000000000093620' should equal
#'#92325250lR$o54990000000000093620'