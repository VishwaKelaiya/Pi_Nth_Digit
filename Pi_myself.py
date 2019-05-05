"""Python script to print Pi with nth possible decimal digit using Ramanujan's series

1/pi = 2root 2 / 9801  = sum fro o to infinity of numerator = (4*k)! * (1103 + 26390*k),
denominator = (k!)**4 * (396)**(4*k)

"""

from decimal import *
import math

def pi_digit(n):

    n = n+1
    getcontext().prec = n  # to get n-1 decimal digits in calculation

    sum = 0
    for i in range(n):
        nume = math.factorial(4*i) * (1103 + 26390*i)
        denum = (math.factorial(i)**4) * 396**(4*i)

        sum += nume/denum

    c = 9801/2/math.sqrt(2)

    result = Decimal(c)/Decimal(sum)

    return result



if __name__ == '__main__':
    num = int(input('Enter a number\n'))
    print(pi_digit(num))

    print(format(math.pi,'.10f')) # you can change value of 10 according to num specified