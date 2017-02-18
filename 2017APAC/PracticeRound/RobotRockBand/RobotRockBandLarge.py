#/*************************************************************************
# *  --------->    FILE: RobotRockBandLarge.py
# *  --------->    AUTHOR: Max Xu
# *  --------->    MAIL: xuhuan@live.cn
# *  --------->    DATE: 02/17/2017    TIME:17:30:40
# ************************************************************************/


import os

result = []

with open("B-large-practice.in") as fp:
    caseCount = int(fp.readline().strip())

    for i in range(1, caseCount+1):
        meta = fp.readline().split()
        N = int(meta[0])
        K = int(meta[1])

        a = [int(ai) for ai in fp.readline().strip().split()]
        b = [int(bi) for bi in fp.readline().strip().split()]
        c = [int(ci) for ci in fp.readline().strip().split()]
        d = [int(di) for di in fp.readline().strip().split()]

        ans = 0
        r = {}

        for ai in a:
            for bi in b:
                if not r.has_key(ai^bi):
                    r.setdefault(ai^bi, 1)
                else:
                    r[ai^bi] += 1

        for ci in c:
            for di in d:
                if r.has_key(ci^di^K):
                    ans += r[ci^di^K]

        result.append("Case #" + str(i) + ": " + str(ans))

with open("B-large-practice.out", "w") as fp:
    fp.writelines("%s\n" % r for r in result)
