def gcd(a,b):
    assert int(a) == a and int(b) == b, "This number must be integer only"
    if a<0:
        a = -1 * a
    if b<0:
        b = -1 * b 
    if b==0:
        return a
    else:
        return gcd(b, a%b)
    
print(gcd(6,12))           
