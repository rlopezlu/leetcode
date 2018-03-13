# Output:
# [0, 6]

import collections
# s= "cbaebabacd" 
# p= "abc"

s= "abab"
p= "ab"


#count each char in p
anagramCounter = collections.Counter(p)
result = []

for i in range(0, 1 + len(s) - len(p)):
	windowCount = collections.Counter(s[i:i+len(p)])
	# print(s[i:i+len(p)])
	if windowCount == anagramCounter:
		print (anagramCounter)
		print(  s[i:i+len(p)])
		result.append(i)
		print(result)




