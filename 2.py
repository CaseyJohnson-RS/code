from math import log10, ceil


def check(num):

    num = str(num)

    #flag = True

    for i in range(len(num) - 1):

        if int(num[i]) % 2 == int(num[i+1]) % 2:
            return False
    
    return True


def generator(n):

    counter = 1
    num = 10

    N = []

    while counter <= n:

        if (check(num)):
            N.append(num)
            counter += 1
        num += 1
        
    
    return N
        
n = int(input())

print(generator(n)[-1])