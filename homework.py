nums = [0, 1, 0, 3, 0, 5]

result = []


for i in nums:
    if i != 0:
        result.append(i)


for i in nums:
    if i == 0:
        result.append(i)

print(result)
