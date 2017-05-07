#/*************************************************************************
# *  --------->    FILE: SquareCountingSmall.py
# *  --------->    AUTHOR: Max Xu
# *  --------->    MAIL: xuhuan@live.cn
# *  --------->    DATE: 03/05/2017    TIME:14:26:37
# ************************************************************************/
#

import os

result = []

with open("A-small1.in") as fp:
    casesCount = int(fp.readline().strip())

    for case in range(1, casesCount+1):
        meta = fp.readline().strip().split()
        R = int(meta[0])
        C = int(meta[1])

        ans = 0
        data = [[0 for c in range(C)] for r in range(R)]

        for r in range(R-1):
            for c in range(C-1):
                for rl in range(max(R, C)):
                    for cl in range(1, max(R, C)):
                        #print("#" + str(case) + " " + str((rl,cl)) + ": " + str((r,c)) + ", " + str((r-rl,c+cl)) + ", " + str((r-rl+cl, c+cl+rl)) + ", " + str((r-rl+cl+rl, c+cl+rl-cl)))
                        if 0 <= r-rl <= R-1 and 0 <= c+cl <= C-1 and 0 <= r-rl+cl <= R-1 and 0 <= c+cl+rl <= C-1 and 0 <= r-rl+cl+rl <= R-1 and 0 <= c+cl+rl-cl <= C-1:
                            #print("***#" + str(case) + " " + str((rl,cl)) + ": " + str((r,c)) + ", " + str((r-rl,c+cl)) + ", " + str((r-rl+cl, c+cl+rl)) + ", " + str((r-rl+cl+rl, c+cl+rl-cl)))
                            ans = ans + 1

        result.append("Case #" + str(case) + ": " + str(ans))

with open("A-small.out1", "w") as fp:
    fp.writelines("%s\n" % r for r in result)
