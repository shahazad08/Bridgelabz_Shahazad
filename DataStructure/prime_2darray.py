import numpy as np
import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

a = np.arange(2, 1000)
foo = np.vectorize(is_prime)
pbools = foo(a)
primes = np.extract(pbools, a)
print(primes)
