# Fibonacci_sequence:f(0)=0, f(1)=1, f(n)=f(n-1)+f(n-2)
def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)
print(f(10))