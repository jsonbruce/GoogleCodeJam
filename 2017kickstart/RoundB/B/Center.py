#!/usr/bin/env python
# coding=utf-8

# Created by max on 17-5-7
# https://codejam.withgoogle.com/codejam/contest/11304486/dashboard#s=p1

import sys


class Point():
    def __init__(self, p):
        if isinstance(p, list):
            self.x = p[0]
            self.y = p[1]
            self.w = p[2]

    def __str__(self):
        return "(%f, %f, %f)" % (self.x, self.y, self.w)

    def __repr__(self):
        return "(%f, %f, %f)" % (self.x, self.y, self.w)

    def diff(self, center):
        return max(abs(self.x - center.x), abs(self.y - center.y)) * self.w

    @staticmethod
    def center(data):
        if isinstance(data, list):
            N = len(data)
            x_sum = 0.0
            y_sum = 0.0
            for p in data:
                x_sum += p.x
                y_sum += p.y
            return Point([x_sum / N, y_sum / N, 0])


def main(args):
    result = []

    with open("B-small-attempt0.in") as fp:
        casesCount = int(fp.readline().strip())

        for case in range(1, casesCount + 1):
            data = []
            is_same_weight = True

            N = int(fp.readline().strip())
            for i in range(N):
                p = Point([float(s) for s in fp.readline().strip().split()])
                data.append(p)
                if len(data) > 1 and p.w != data[0].w:
                    is_same_weight = False

            # compute
            ans = 0.0
            center = Point.center(data)

            if not is_same_weight:
                # sorted by weight
                data.sort(key=lambda d: d.w, reverse=True)
                center = data[0]

            for i in range(0, N):
                ans += data[i].diff(center)

            result.append("Case #" + str(case) + ": " + str(ans))

    with open("B-small.out", "w") as fp:
        fp.writelines("%s\n" % r for r in result)


if __name__ == "__main__":
    main(sys.argv)
