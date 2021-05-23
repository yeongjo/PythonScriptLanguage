def gcd(m, n):
    if m%n == 0:
        return n
    else:
        return gcd(n,m%n)

a = input("A b를 입력하세요: ").split()
a = [float(a[i]) for i in range(len(a))]

print(gcd(a[0], a[1]))