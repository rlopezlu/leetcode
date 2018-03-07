x = 1
y = 4

#XOR operator gives 1 for bits where they are different
asBin = bin(x ^ y)[2:]
print(asBin.count('1'))
return asBin.count('1')
