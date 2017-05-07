#/*************************************************************************
# *  --------->    FILE: VoteSmall.py
# *  --------->    AUTHOR: Max Xu
# *  --------->    MAIL: xuhuan@live.cn
# *  --------->    DATE: 02/19/2017    TIME:15:46:35
# ************************************************************************/
#

import os
import math

result = []

with open("B-small-practice.in") as fp:
    caseCount = int(fp.readline().strip())

    for case in range(1, caseCount+1):
        meta = fp.readline().strip().split()
        N = int(meta[0])
        M = int(meta[1])

        ans = float(math.factorial(N)) / math.factorial(N+M)

        result.append("Case #" + str(case) + ": " + str(ans))

with open("B-small-practice.out", "w") as fp:
    fp.writelines("%s\n" % r for r in result)
