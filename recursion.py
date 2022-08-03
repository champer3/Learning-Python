def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer"
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def sumOfDigits(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(n//10)


def power(l, n):
    assert n >= 0 and int(n) == n, "The exponent must be a positive integer"
    if n == 0:
        return 1
    else:
        return l * power(l, n-1)


def gcd(a, b):
    assert int(a) == a and int(b) == b, "The numbers must be integer"
    if b < 0:
        -1 * b
    if a < 0:
        -1 * a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def convert(num):
    assert int(num) == num, "The number must be an integer"
    if num == 0:
        return 0
    else:
        return (num % 2) + (10 * convert(int(num/2)))


print(convert(10))
