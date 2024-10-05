import math

base = 10

results = []

def karprekar(start):
    diffs = []
    results = []

    lastDiff = start
    while(not(lastDiff in diffs)):

        
        diffs.append(lastDiff)
        
        digits = [int(d) for d in str(lastDiff)]
        print(digits)
        
        downSrt = digits.copy()
        downSrt.sort(reverse=True)
        upSrt = downSrt.copy()
        upSrt.reverse()
        print(downSrt, upSrt)
        downNum= int("".join([str(d) for d in downSrt]))
        upNum = int("".join([str(d) for d in upSrt]))
        print(downNum, upNum)
        lastDiff = downNum - upNum

        results.append({"upNum": upNum, "downNum": downNum, "diff": lastDiff})

    print(results)



karprekar(12542)