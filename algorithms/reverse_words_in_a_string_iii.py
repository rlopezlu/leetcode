class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        stringList = s.split(' ')
        def myReverse(aString):
            return aString[::-1]

        return ' '.join(map(myReverse, stringList))
