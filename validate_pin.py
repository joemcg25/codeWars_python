#https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
def validate_pin(pin):
    length=len(pin)
    nums="0123456789"
    if (length!=4) and (length!=6):
        return False
    for i in pin:
        if not nums.__contains__(i):
            return False
    return True

print(validate_pin("1234"))
print(validate_pin("123a"))
print(validate_pin("12345"))
print(validate_pin("123456"))
print(validate_pin("-12345"))
print(validate_pin("+111"))
print(validate_pin("+88888"))
print(validate_pin("09876"))
