import datetime

# Divide and conquer solution
def HowManyWaysDC(numOfMatrices):
    divideStart = datetime.time
    if numOfMatrices <= 1:
        return 1
    output = 1
    for i in range(numOfMatrices):
        p1 = HowManyWaysDC(i)
        p2 = HowManyWaysDC(numOfMatrices - i - 1)
        output = output + p1 * p2
    
    divideEnd = datetime.time
    print("Divide and Conquer Algo took " +
            str(divideEnd - divideStart) +
            "\nFor " + str(numOfMatrices) +
            " numOfMatrices, output = " +
            str(output))
    return output

# Dynamic programming solution
def HowManyWaysDP(numOfMatrices):
    dynamicStart = datetime.time
    output = 0







    dynamicEnd = datetime.time
    print("Divide and Conquer Algo took " +
            (dynamicEnd - dynamicStart) +
            "\nFor " + str(numOfMatrices) + " numOfMatrices, output = " + str(output))




HowManyWaysDC(2)
#HowManyWaysDP(2)