# J = "aA"
# S = "aAAbbbb"

J = "z"
S = "ZZ"


countingTable = {}

for jewel in J:
    countingTable[jewel] = 0

for stone in S:
    if stone in J:
        countingTable[stone] += 1

for key in countingTable:
    print (key + " " + str(countingTable[key]))
