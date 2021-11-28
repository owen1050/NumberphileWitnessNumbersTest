def runTest(n, a):
    #n is num we want to be prime
    #a is the witness

    #solve for d n = 2^m * d + 1
    newN = n - 1
    count = 2
    ms = [1]
    ds = [int(newN / 2)]
    newN = newN / 2
    while((newN / 2) % 2 == 0):
        ms.append(count)
        count = count + 1

        ds.append(int(newN / 2))
        newN = newN / 2

    #ds is all possible D's and ms is is all possible ms
    #now take a^d and if its mod n == 1 or -1 then this witness thinks its prime
    testN = pow(a, ds[0]) % n
    #print(testN, ds, ms)
    if(testN == 1 or testN == n - 1):
        return True
    return False

#run through a bunch of numbers to test
liarCount = {}
startN = 131
endN = 30000
tests = int((endN-startN) / 2)
for n in range(startN, endN, 2):
    #test each a up to n, ovbiously 1 lies every time so we dont even test it
    trues = []
    falses = []
    #this range sets the A's to test. 
    for a in range(2, 130):
        if(runTest(n, a)):
            trues.append(a)
        else:
            falses.append(a)    
    if(len(trues) < len(falses)):
        for liar in trues:
            if liar in liarCount:
                liarCount[liar] = liarCount[liar] + 1
            else:  
                liarCount[liar] = 1
    else:
        for liar in falses:
            if liar in liarCount:
                liarCount[liar] = liarCount[liar] + 1
            else:  
                liarCount[liar] = 1
    print("tested n=" + str(n))


for l in dict(sorted(liarCount.items(), key=lambda item: item[1])):
    print("a: " + str(l) + "\tlies:"+ str(round(liarCount[l]*100/tests, 1)) + "% of the time, or " + str(liarCount[l]) + " out of " + str(tests) + " tests")