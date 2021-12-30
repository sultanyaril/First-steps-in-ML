def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** (1/2)) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes():
    n = 1
    while True:
        if is_prime(n):
            yield n
        n += 1

if __name__ == "__main__":
    for i in primes():
        print(i)
        if i >= 20:
            break
