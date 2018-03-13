

stairs = 4
stepCount = [None] * (stairs +1)
stepCount[0] = 0
stepCount[1] = 1
stepCount[2] = 2


for i in range (0, stairs + 1):
	if stepCount[i] == None:
		stepCount[i] = stepCount[i -1] + stepCount[i-2]

print (stepCount)