import math
a,b = map(int,input().split())
c,d = map(int,input().split())
son = b * c + a * d
mother = b * d

gcd = math.gcd(son, mother)
son //= gcd
mother //= gcd
print(son,mother)