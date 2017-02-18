#/*************************************************************************
# *  --------->    FILE: SumsOfSumsSmall.py
# *  --------->    AUTHOR: Max Xu
# *  --------->    MAIL: xuhuan@live.cn
# *  --------->    DATE: 02/18/2017    TIME:16:36:45
# ************************************************************************/

import os

result = []

with open("D-small-practice.in") as fp:
    caseCount = int(fp.readline().strip())

    for case in range(1, caseCount+1):

        meta = fp.readline().split()
        N = int(meta[0])
        Q = int(meta[1])

        result.append("Case #" + str(case) + ":" + "\n")

        data = [int(d) for d in fp.readline().split()]
        subData = []

        for i in range(len(data)):
            for j in range(i, len(data)):
                subData.append(sum(data[i:j+1]))

        subData = sorted(subData)

        for q in range(Q):
            meta = fp.readline().split()
            L = int(meta[0])
            R = int(meta[1])

            result.append(str(sum(subData[L-1:R])) + "\n")


with open("D-small-practice.out", "w") as fp:
    fp.writelines("%s" % r for r in result)
