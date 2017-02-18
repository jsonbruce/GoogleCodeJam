#/*************************************************************************
# *  --------->    FILE: SumsOfSumsSLarge.py
# *  --------->    AUTHOR: Max Xu
# *  --------->    MAIL: xuhuan@live.cn
# *  --------->    DATE: 02/18/2017    TIME:16:36:45
# ************************************************************************/

import os

result = []

with open("D-large-practice.in") as fp:
    caseCount = int(fp.readline().strip())

    for case in range(1, caseCount+1):

        meta = fp.readline().split()
        N = int(meta[0])
        Q = int(meta[1])

        result.append("Case #" + str(case) + ":" + "\n")

        data = [int(d) for d in fp.readline().split()]
        subData = []

        print("Case #%d" %case)

        for i in range(len(data)):
            for j in range(i, len(data)):
                print(len(subData))
                subData.append(sum(data[i:j+1]))

        print("1 [Unsorted]Case %d \n" %(case))
        print(subData)
        print("2 [Unsorted]Case %d \n" %(case))

        #subData = sorted(subData)
        subData.sort()

        print("3 [Sorted]Case %d \n" %(case))
        print(subData)
        print("4 [Sorted]Case %d \n" %(case))

        for q in range(Q):
            meta = fp.readline().split()
            L = int(meta[0])
            R = int(meta[1])

            print("Q=%d q=%d" %(Q,q))
            print("L=%d R=%d" %(L,R))
            #print(subData[L-1:R])
            print("len(subData[])=%d" % (len(subData[L-1:R])))
            print("[Q]Case %d" %(case))
            print("len(result)=%d" %(len(result)))

            s = sum(subData[L-1:R])
            print("sum=%d" % s)

            result.append(str(sum(subData[L-1:R])) + "\n")

            print("len(result)=%d \n" %(len(result)))


with open("D-large-practice.out1", "w") as fp:
    fp.writelines("%s" % r for r in result)
