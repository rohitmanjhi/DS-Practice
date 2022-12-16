def decimalToBinary(n):
    assert int(n) == n, "Parameter must be integer"    
    if n == 0:
        return 0
    else:
        print("----",n%2 + 10 * decimalToBinary(int(n/2)))
        return n%2 + 10 * decimalToBinary(int(n/2)) #1 + 10*0 + 10*1 + 10*1 + 10*0 = 1+0+10+10+0
        
print(decimalToBinary(13))     
