class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nList = []


        for number in range(left, right + 1):
            flag = True
            for digit in map(int, str(number)):
                if digit == 0 or number % digit != 0 :
                    flag = False
                    break
            if(flag == True):
                nList.append(number)
        return nList
