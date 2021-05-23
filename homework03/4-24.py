import random
a = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
b = ["크로바","다이아몬드","하트","스페이스"]

print("당신이 뽑은 카드는 ",b[random.randint(0,len(b))],a[random.randint(0,len(a))],"입니다.")