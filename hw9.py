from datetime import datetime

############ Divide and conquer solution ############
def ConquerHowManyWays(numOfMatrices):
    output = 0
    if numOfMatrices == 1 or numOfMatrices == 2:
        output =  1
    else:
        for i in range(1, numOfMatrices):
            output += ConquerHowManyWays(i) * ConquerHowManyWays(numOfMatrices - i)
    return output

############ Dynamic programming solution ############
def DynamicHowManyWays(numOfMatrices):
    num = [1,1]
    if numOfMatrices == 1 or numOfMatrices == 2:
        return 1
    else:
        for i in range(2, numOfMatrices + 1):
            num.append(0)
            for j in range(1, i):
                num[i] += num[j] * num[i - j]
    return num[len(num) - 1]

############ Helper functions ############

def getTimeDict1(testcases):
    timeDict = {}
    for num in testcases:
        start = datetime.now()
        output = ConquerHowManyWays(num)
        end = datetime.now()
        timeDict[num] = [output, str(end - start)[5:]]
    return timeDict

def getTimeDict2(testcases):
    timeDict = {}
    for num in testcases:
        start = datetime.now()
        output = DynamicHowManyWays(num)
        end = datetime.now()
        timeDict[num] = [output, str(end - start)[5:]]
    return timeDict

def printResults(times):
    for key, value in times.items():
        print("n = {}   -> {} ways".format(key,value[0]))
        print("\t{} seconds".format(value[1]))

def timeComparison(dict1, dict2):
    values1 = dict1.values()
    values2 = dict2.values()
    time1 = []
    time2 = []
    for i in range(len(values1)):
        time1.append(float(values1[i][1]))
        time2.append(float(values2[i][1]))
    avg1 = sum(time1) / len(time1)
    avg2 = sum(time2) / len(time2)
    print("________________________________")
    print("Divide and Conquer time: {:.7f} seconds".format(avg1))
    print("Dynamic programming time: {:.7f} seconds".format(avg2))
    print("________________________________")

############ Execution ############

testcases = [2,3,4,5,6,7]

conquerTimes = getTimeDict1(testcases)
dynamicTimes = getTimeDict2(testcases)

printResults(conquerTimes)
print("________________________________")
printResults(dynamicTimes)


timeComparison(conquerTimes, dynamicTimes)