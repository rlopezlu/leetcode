class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = 0
        myLen = len(s)
        for index, char in enumerate(s):
            val += 26 ** (myLen - index - 1) * (ord(char) - 64)
        return val
        
