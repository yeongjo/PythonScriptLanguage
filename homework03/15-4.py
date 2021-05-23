def gcd(n):
    if n == 1:
        return 1
    else:
        return gcd(n-1) + 1/n

print(gcd(10))