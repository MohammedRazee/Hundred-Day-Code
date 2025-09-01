# Code is Optimized for non Prime Numbers, I guess

def is_prime(num):
    '''Checks if number is Prime or Not'''
    if num < 2:
        return False
    
    for n in range(2, num):
        if num % n == 0:
            return False

    return True

print(is_prime(2))
