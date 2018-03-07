class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        myHT = {}
        for num in nums:
            if num in myHT:
                myHT[num] +=1
            else:
                myHT[num] = 1

        count = 0
        val = None
        for item in myHT:
            if (myHT[item] > count):
                count = myHT[item]
                val = item
        return val


        
