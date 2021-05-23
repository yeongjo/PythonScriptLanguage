def reverse(number):
    return int(''.join(reversed(str(number))))

def isPalindrome(number):
    t = str(reverse(number))
    count = len(t)/2
    idx = 0
    for i in str(number):
        if i == t[idx]:
            count -= 1
        else:
            break
        idx+=1
    return True if (count <= 0) else False

a = input("대칭수인지 판별할테니 아무거나 입력: ")
if isPalindrome(a):
    print("맞음")
else:
    print("no")