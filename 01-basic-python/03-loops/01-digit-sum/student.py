# Write your code here

def digit_sum(n):
    sum = 0
    for i in str(n):
        sum += last_digit(i)
        n = remove_last_digit(n)
    return sum

def last_digit(n):
    n = str(n)
    return int(n[-1])

def remove_last_digit(n):
    return n // 10