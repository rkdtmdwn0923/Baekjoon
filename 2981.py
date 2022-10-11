import sys
import math
input = sys.stdin.readline

# 루트값을 int()해주면 버림으로 처리한다
# A = M * a + R
# B = M * b + R
# C = M * c + R

def gcd(a,b):
    result = 0
    while b:
        a,b = b, a%b
        result = a
    return result


n = int(input())
arr=[]
arr2=[]
for i in range(n):
    arr.append(int(input()))
arr = sorted(arr,reverse=False)

for i in range(1,n):
    arr2.append(arr[i] - arr[i-1])

GCD = arr2[0]
for i in range(1,len(arr2)):
    GCD = gcd(arr2[i],GCD)

## GCD**0.5일때 두개 추가할 수도있음
result = set()
for i in range(2,int(GCD**0.5)+1):
    if GCD % i ==0:
        result.add(i)
        result.add(GCD//i)
result.add(GCD)
result = sorted(list(result))
print(' '.join(map(str,result)))


