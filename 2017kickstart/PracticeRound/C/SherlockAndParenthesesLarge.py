#/*************************************************************************
# *  --------->    FILE: SherlockAndParenthesesLarge.py
# *  --------->    AUTHOR: Max Xu
# *  --------->    MAIL: xuhuan@live.cn
# *  --------->    DATE: 02/19/2017    TIME:15:21:06
# ************************************************************************/
#

import os

result = []

with open("C-large-practice.in") as fp:
    caseCount = int(fp.readline().strip())

    for case in range(1, caseCount+1):
        meta = fp.readline().strip().split()
        L = int(meta[0])
        R = int(meta[1])

        m = min(L,R)
        ans = m * (m+1) / 2

        result.append("Case #" + str(case) + ": " + str(ans))

with open("C-large-practice.out", "w") as fp:
    fp.writelines("%s\n" % r for r in result)
