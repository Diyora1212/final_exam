def one_plus(digits):
    n = len(digits)
    digits[n - 1] += 1
    carry = 0
    for i in range(n - 1, -1, -1):
        digits[i] += carry
        carry = digits[i] // 10
        digits[i] %= 10

    if carry:
        digits.insert(0, 1)
    return digits


print(one_plus([1, 2, 3]))
print(one_plus([4, 3, 2, 1]))
print(one_plus([9]))
