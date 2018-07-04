import sys
from primes import prime_sieve

def truncate(num, direction="left"):
    string = str(num)
    if len(string) > 1:
        if direction == "left":
            return int(string[1:])
        else:
            return int(string[0:len(string)-1])
    else:
        return int(string)

def enumerate_truncate(num):
    list_trun = [num]
    curr = str(num)
    for _ in range(len(str(num))-1):
        new_number = truncate(curr, "right")
        list_trun.append(new_number)
        curr = new_number

    curr = str(num)
    for _ in range(len(str(num))-1):
        new_number = truncate(curr, "left")
        list_trun.append(new_number)
        curr = new_number

    return list_trun

if __name__ == '__main__':
    prime_set = set([])
    for line in sys.stdin:
        prime_set.add(int(line))

    result = 0
    count = 0
    for p in prime_sieve(10000000):
        is_trun_prime = True
        for new_p in enumerate_truncate(p):
            if not new_p in prime_set:
                is_trun_prime = False
                break
        if is_trun_prime and not p in [2, 3, 5, 7]:
            print p, enumerate_truncate(p)
            count += 1
            result += p

    print count, result
