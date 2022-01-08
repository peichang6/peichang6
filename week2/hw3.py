def maxProduct(nums):
    ans = 0
    if len(nums) == 2:
        ans = nums[0] * nums[1]
        print(ans)
        return ans
    else:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                if product > ans:
                    ans = product
        print(ans)
        return ans


maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([-1, -2, 0])
