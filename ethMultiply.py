
def ethiopian_multiply(a, b):
    result = 0
    while a > 0:
        if a % 2 != 0:
            result += b
        a = a // 2      # GANZZAHLIGE Division
        b = b * 2
    return result
