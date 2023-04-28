'''Calculates PI'''
ACCURACY = float(10**5)


def divide(a, b):
    quotient = 0.0
    while True:
        (a, addition) = divide_helper(a, b, 1)
        quotient += addition
        if addition <= 10**-30:
            break
        if addition == 0.0:
            break
    return quotient


def divide_helper(a, b, addition):
    if a - (b * addition) >= 0:
        a -= b * addition
        return (a, addition)
    if addition <= 10**-30:
        return (a, addition)
    return divide_helper(a, b, addition/10)


i = 1
TOTAL = float(0)
ADD = True
while i < ACCURACY:
    if ADD:
        TOTAL += divide(4.0, i)
        ADD = False
    else:
        TOTAL -= divide(4.0, i)
        ADD = True
    i += 2

print(TOTAL)
