def is_prime(num):
    if num in (0, 1):
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True


def prime_list(obj):
    return [val for i, val in enumerate(obj) if is_prime(i)]


obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5}
print(prime_list(obj))
