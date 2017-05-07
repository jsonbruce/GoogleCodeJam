#/*************************************************************************
# *  --------->    FILE: CountryLeaderSmall.py
# *  --------->    AUTHOR: Max Xu
# *  --------->    MAIL: xuhuan@live.cn
# *  --------->    DATE: 02/19/2017    TIME:13:05:24
# ************************************************************************/
#

import os

result = []

with open("A-small-practice.in") as fp:
    caseCount = int(fp.readline().strip())

    for case in range(1, caseCount+1):
        N = int(fp.readline().strip())

        names = []
        for n in range(N):
            names.append(fp.readline().strip())

        namesLons = [""]
        for n in names:
            if len(set(n)) > len(set(namesLons[0])):
                namesLons = [""] 
                namesLons[0] = n
            elif len(set(n)) == len(set(namesLons[0])):
                namesLons.append(n)

        #namesMap = {}
        #for name in names:
        #    namesMap[name] = len(set(name))

        #print("len=%d" %len(namesMap))
        #print(namesMap)

        #namesMap = sorted(namesMap.items(), key=lambda d: d[1], reverse=True)
        #print("\nlen=%d \n" % len(namesMap))
        #print(namesMap)
        #break

        #names = []
        #for (k,v) in namesMap:
        #    if v >= namesMap[0][1]:
        #        print("v=%d" % v)
        #        names.append(k)
        #
        #names.sort()

        namesLons.sort()
        print("After:")
        print(namesLons)
        result.append("Case #" + str(case) + ": " + namesLons[0] + "\n")

with open("A-small-practice.out", "w") as fp:
    fp.writelines("%s" % r for r in result)
