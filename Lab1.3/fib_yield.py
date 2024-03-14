def fib(n):
    a, b = 1, 1

    step = 0
    while step < n:
        yield a
        b, a = a + b, b
        step += 1

def fibr(n):
    for i in fib(50):
        print(i)