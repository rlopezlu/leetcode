class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        HT = {}
        for item in nums:
            if(item in HT):
                HT[item] = 2
            else:
                HT[item] = 1

        for item in HT:
            if(HT[item]  == 1):
                return item


        
