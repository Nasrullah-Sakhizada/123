# Implement a Custom Iterator for Prime Numbers
# Objective: Design a class `PrimeIterator` that generates an infinite sequence of prime numbers.
# Parameters:
# - None, but the iterator should handle internal state for generating primes.
# Returns:
# - Prime numbers, one at a time, indefinitely.
# Details:
# - Implement the iterator protocol methods `__iter__()` and `__next__()`.
# - Use a sophisticated method to check for primes to ensure efficiency as numbers grow large.

class PrimeIterator:
    def __init__(self):
        self.current = 2 

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
primes = PrimeIterator()
for _ in range(10):
    print(next(primes))

# Example:
# primes = PrimeIterator()
# for _ in range(10):
#     print(next(primes))  # Prints the first 10 prime numbers