numbers = [4, 2, 7, 2, 9, 2, 4, 6, 2]
tung = len(numbers) - 1
i = 0
j = 0
res = []

#if i == 0:
#        res.append(numbers[0])
#        j = j + 1
#        i = i + 1
#
#for n in numbers:
#    if n != res[0]:
#        while i != 0 and j != tung:
#            if n != numbers[i - 1]:
#                i = i - 1
#                if i == 0:
#                    res.append(n)
#                    j = j + 1
#            else:
#                i = 0
#        i = j
#print(res)


for n in numbers:
    if n not in res:
        res.append(n)
print(res)