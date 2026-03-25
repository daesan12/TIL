nums = [int(input()) for _ in range(9)]

max_num = max(nums)
idx = nums.index(max_num) + 1

print(max_num)
print(idx)