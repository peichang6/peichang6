def twoSum(nums, target):
    result = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                result = [i, j]
    return result


result = twoSum([2, 11, 7, 15], 9)
print(result)
