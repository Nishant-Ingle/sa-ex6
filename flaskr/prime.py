

def get_primes(y):
    prime_list = []
    current_number = 2

    while len(prime_list) < y:
        for i in range(2, int(current_number/2)+1):
            if current_number % i == 0:
                break
        else:
            prime_list.append(current_number)

        current_number += 1

    return prime_list


def get_nth_prime(n):
    prime_counter = 1
    current_number = 2

    while prime_counter < n:
        for i in range(2, int(current_number/2)+1):
            if current_number % i == 0:
                break
        else:
            prime_counter += 1

        current_number += 1

    return current_number
