nums = [2, 7, 11, 15]
target = 9
found = 0
myHT = {}

# TODO: can be optimized to be done in a single loop
for index, num in enumerate(nums):
    myHT[num] = index

for key in myHT:
    currentIndex = myHT[key]
    del myHT[key]
    if(target - key) in myHT:
        print (target - key)
        print (key)
        break
