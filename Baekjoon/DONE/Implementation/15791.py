import sys
n,k = map(int,sys.stdin.readline().split())
mod_p = 1000000007
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % mod_p
result = fact[n] * pow(fact[n - k] * fact[k] % mod_p, mod_p - 2, mod_p) % mod_p
print(result)