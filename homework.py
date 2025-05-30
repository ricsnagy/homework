nums = [1, 3, 5, 7, 9]

if nums == []:
    print(0)
else:
    s = 0
    for i in range(0, len(nums), 2):
        s += nums[i]
    print(s * nums[-1])
