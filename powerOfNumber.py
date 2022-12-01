def power(base, exp):
    assert int(exp) == exp, "The exponent must be integer only"
    if exp == 0:
        return 1
    elif exp < 0:
        a = 1/base * power(base, exp+1)
        # print(a) 1/4*
        return a
    return base * power(base, exp-1)
    
print(power(4,-1))    
