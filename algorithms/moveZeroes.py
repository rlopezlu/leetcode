class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                count +=1
            else:
                nums[i - count] = nums[i]
                if(count):
                    nums[i] = 0




        
