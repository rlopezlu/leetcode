nums = [2, 7, 11, 15]
target = 9
found = 0


for i in range(0, len(nums)):
    if found:
        break
    for x in range( i +1, len(nums)):
        print (nums[i], end=' ')
        print(nums[x], )
        if( nums[i] + nums[x] == target):
            print ('found')
            found = 1
            break
