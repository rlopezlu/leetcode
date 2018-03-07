x = 1
y = 4

str1 = bin(x)[2:]
str2 = bin(y)[2:]

print(str1 + " " + str2)

len1 = len(str1)
len2 = len(str2)
char1 = ''
char2 = ''


length = max(len1, len2)
index = 0
count = 0
while(index < len1 or index < len2):
    if (index >= len1):
        char1 = '0'
    else:
        char1 = str1[len1 - index - 1]

    if(index >= len2):
        char2 = '0'
    else:
        char2 = str2[len2 - index - 1]

    if char1 != char2:
        count+=1

    index +=1
    
print (count)
