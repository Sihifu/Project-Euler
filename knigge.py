import numpy as np


def fib(mx):
    nums = [0, 1, 1]
    for i in range(mx-3):
        nums.append(nums[len(nums)-1]+nums[len(nums)-2])
    return nums


fibs = fib(122)


def mods(n):
    arr = [fib % n for fib in fibs]
    return arr


def pi(n):
    ar = mods(n)
    for i in range(1, len(ar)-1):
        if ar[i] == 0 and ar[i+1] == 1:
            return i


def n():
    nums = []
    for i in range(1, 1_000_000_000):
        if fibs[120] % i == 0 and fibs[121] % i == 1:
            nums.append(i)
    return nums
print(n())