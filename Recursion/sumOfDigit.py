def sumOfDigit(num):
    assert num>=0 and int(num) == num, "The number has to be positive integer" 
    if num==0:
        return 0
    return int(num%10) + sumOfDigit(num/10)

print(sumOfDigit(0))



