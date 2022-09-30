def Fibonacci_Loop(number):
    old = 1
    new = 1
    for itr in range(number - 1):
        tmpVal = new
        new = old
        old = old + tmpVal
    return new

def Fibonacci_Loop_pythonic(number):
    old, new = 1, 1
    for iter in range (number - 1):
        new, old = old, old + new
    return new


def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

print(Fibonacci_Loop(15))
print(Fibonacci_Loop_pythonic(15))
print(fib_recur(25))