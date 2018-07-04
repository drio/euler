import sys
from collections import deque

def shift(num):
    if num:
        a_number = map(str, str(num))
        items = deque(a_number)
        items.rotate(1)
        return int(''.join(items))

def enum_circular(num):
    a_cir = [num]
    curr_num = num
    for _ in range(len(str(num))-1):
        a_cir.append(shift(curr_num))
        curr_num = a_cir[-1]
    return a_cir

def is_circular_prime(num, primes):
    for c_value in enum_circular(num):
        if not c_value in primes:
            return False
    return True

if __name__ == '__main__':
    prime_set = set([])
    found_set = set([])

    for line in sys.stdin:
        prime_set.add(int(line))

    for idx, pnum in enumerate(prime_set):
        if idx % 100000 == 0 and idx != 0:
            print >> sys.stderr, idx, len(found_set)

        if not pnum in found_set and is_circular_prime(pnum, prime_set):
            for c_num in enum_circular(pnum):
                found_set.add(c_num)

    print(len(found_set))
