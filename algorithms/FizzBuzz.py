class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        for i in range (1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print ('FizzBuzz')
                list.append('FizzBuzz')
            elif i % 3 == 0:
                print('fizz')
                list.append('Fizz')
            elif i % 5 == 0:
                list.append('Buzz')
                print ('Buzz')
            else:
                print (i)
                list.append(str(i))
        return list
