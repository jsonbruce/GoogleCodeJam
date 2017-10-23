#!/usr/bin/env python
# coding=utf-8

# Created by max on 17-10-22

import sys
import math


def quick_pow(x, n):
    result = 1
    while n:
        if (n & 1):
            result *= x
        x *= x
        n >>= 1
    return result


def main(args):
    result = []

    with open("A-large.in") as fp:
        casesCount = int(fp.readline().strip())

        for case in range(1, casesCount + 1):
            A, N, P = [int(s) for s in fp.readline().strip().split()]

            # ans = (A ** math.factorial(N)) % P
            ans = quick_pow(A, math.factorial(N)) % P

            result.append("Case #" + str(case) + ": " + str(ans))

    with open("A-large.out", "w") as fp:
        fp.writelines("%s\n" % r for r in result)


if __name__ == "__main__":
    main(sys.argv)
