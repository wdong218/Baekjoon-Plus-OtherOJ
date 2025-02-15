import sys
fact = [1] * (4000000 + 1)
mod_p = 1000000007
def facto():
    for i in range(1,4000000 + 1):
        fact[i] = fact[i-1] * i % mod_p
facto()
def combi(n,k):
    global fact
    result = fact[n] * pow(fact[n - k] * fact[k] % mod_p, mod_p - 2, mod_p) % mod_p
    return result
m = int(sys.stdin.readline())
for _ in range(m):
    n,k = map(int,sys.stdin.readline().split())
    print(combi(n,k))

