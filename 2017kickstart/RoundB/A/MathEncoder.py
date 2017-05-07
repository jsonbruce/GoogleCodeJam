#!/usr/bin/env python
# coding=utf-8

# Created by max on 17-5-7
# https://codejam.withgoogle.com/codejam/contest/11304486/dashboard#s=p0

import sys

from itertools import chain, combinations

def subsets(iterable):
    xs = list(iterable)
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

def main(args):
    result = []

    with open("A-small-attempt5.in") as fp:
        casesCount = int(fp.readline().strip())

        for case in range(1, casesCount + 1):
            N = int(fp.readline().strip())
            data = [int(s) for s in fp.readline().strip().split()]

            ans = 0

            # subs = subsets(data)
            # for s in subs:
            #     if len(s) > 0:
            #         ans += max(s) - min(s)

            for i in range(N-1):
                for j in range(i+1, N):
                    ans += (j - i) * (data[j] - data[i])
            ans += data[N-1] - data[0]

            ans %= 1000000007

            result.append("Case #" + str(case) + ": " + str(ans))


    with open("A-large.out1", "w") as fp:
        fp.writelines("%s\n" % r for r in result)

if __name__ == "__main__":
    main(sys.argv)
