import sys
a = []
for i in range(3):
    line = sys.stdin.readline().strip()
    try:
        num = int(line) + 3 - i
    except ValueError:
        pass

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)