#/*************************************************************************
# *  --------->    FILE: LazySpellingBeeLarge.py
# *  --------->    AUTHOR: Max Xu
# *  --------->    MAIL: xuhuan@live.cn
# *  --------->    DATE: 02/17/2017    TIME:09:21:13
# ************************************************************************/
#

import os

md = 1000000007
result = []

with open('A-large-practice.in') as fp:
    caseCount = fp.readline()

    for i in range(1, int(caseCount)+1):
        s = fp.readline().strip()

        if len(s) == 1:
            result.append("Case #" + str(i) + ": " + str(1))
            continue

        if len(s) == 2:
            if s[0] == s[1]:
                result.append("Case #" + str(i) + ": " + str(1))
            else:
                result.append("Case #" + str(i) + ": " + str(4))
            continue
        
        ans = 1
        for j in range(len(s)):
            if j == 0:
                ss = set({s[j], s[j+1]})
            elif j == len(s) - 1:
                ss = set({s[j], s[j-1]})
            else:
                ss = set({s[j-1], s[j], s[j+1]})
            ans *= len(ss)


        ans %= md
        result.append("Case #" + str(i) + ": " + str(ans))

with open("A-large-practice.out", "w") as fp:
    fp.writelines("%s\n" % r for r in result)
    #for r in result:
    #    fp.write(r)
