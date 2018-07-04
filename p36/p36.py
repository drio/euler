
def is_palin(num):
    string = str(num)
    size = len(string)
    left = str(num)[0:size/2]
    right = str(num)[size/2:]
    if size % 2 > 0:
        right = str(num)[(size/2)+1:]
    return left == right[::-1]

sum_nums = 0
if __name__ == '__main__':
    for num in range(1000000):
        if is_palin(num) and is_palin("{0:b}".format(num)):
            sum_nums += num

print(sum_nums)
