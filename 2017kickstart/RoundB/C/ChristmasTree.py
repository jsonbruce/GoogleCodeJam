#!/usr/bin/env python
# coding=utf-8

# Created by max on 17-5-7

import sys


def main(args):
    result = []

    with open("A-small-attempt0.in") as fp:
        casesCount = int(fp.readline().strip())

        for case in range(1, casesCount + 1):
            N = int(fp.readline().strip())


            ans = 0

            result.append("Case #" + str(case) + ": " + str(ans))

    with open("A-small.out", "w") as fp:
        fp.writelines("%s\n" % r for r in result)


if __name__ == "__main__":
    main(sys.argv)