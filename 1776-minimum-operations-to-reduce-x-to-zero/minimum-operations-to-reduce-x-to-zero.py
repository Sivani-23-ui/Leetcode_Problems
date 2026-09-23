class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x

        if target < 0:
            return -1

        left = 0
        s = 0
        longest = -1

        for right in range(len(nums)):
            s += nums[right]

            while s > target:
                s -= nums[left]
                left += 1

            if s == target:
                longest = max(longest, right - left + 1)

        if longest == -1:
            return -1

        return len(nums) - longest