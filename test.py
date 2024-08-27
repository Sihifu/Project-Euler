
# Python3 program to find the Nth Fibonacci
# number using Fast Doubling Method iteratively
 
 

def fastfib(n):

    """computes fib(n) iteratively using fast doubling method"""

    bin_of_n = bin(n)[2:]  # binary string of n
    f = [0, 1]  # [F(i), F(i+1)] => i=0
 

    for b in bin_of_n:

        f2i1 = f[1]**2 + f[0]**2  # F(2i+1)

        f2i = f[0]*(2*f[1]-f[0])  # F(2i)
 

        if b == '0':

            f[0], f[1] = f2i, f2i1  # [F(2i), F(2i+1)]

        else:

            f[0], f[1] = f2i1, f2i1+f2i  # [F(2i+1), F(2i+2)]

    return f[0]
 
 

fib_121 = fastfib(121)
fib_120 = fastfib(120)

A=[]
for i in range(1,1_000_000_000):
    if fib_120%i==0 and (fib_121)%i==1:
        A.append(i)

print(A)