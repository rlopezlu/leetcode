class Solution(object):
    def isValid(self, s):
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if(char in "([{"):
                print('open bracket ' + char)
                stack.append(char)

            if(char in ")]}"):
                print('closing bracket ' + char)
                if len(stack) != 0 and mapping[char] == stack[len(stack) -1]:
                    stack.pop()
                else:
                    print ("invalid")
                    return False

        return len(stack) == 0
        
