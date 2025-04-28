def twoSum(nums, target):
    dict = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in dict:
            return [dict[complement], idx]
        dict[num] = idx 

# 測試
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # 輸出 [0, 1]
