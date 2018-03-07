class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        p = 0
        q = 2
        lengthS = 0#length of arithmetic segment
        count = 0
        while q < len(A):
            currentCount = 0 #count in current segment
            diff1 = A[q] - A[p +1]
            diff2 = A[p+1] - A[p]
            prevQ = A[q-1]
            # print ('prevQ' + str(prevQ))
            # q+=1
            if diff2 == diff1 : #if arithmetic, find whole arithmetic segment
                print ("diff " + str(diff1) + " starts at index " + str(p))
                while(q < len(A) and diff1 == (A[q] - prevQ)):#while still arithmetic
                    # print ("increase q " + str(q))
                    prevQ = A[q]
                    q+=1
                lengthS = q - p
                # print (lengthS)
                for i in range(1, lengthS - 1):
                    # print (i)
                    currentCount += i
                    count += i
                p = q
            else:#segment of 3 was not arithmetic, check next segment of 3
                p+=1
            q = p + 2
            print (currentCount)
            print (count)
        return count



                    
