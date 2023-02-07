class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        currentSum = sum(nums)
        n = len(nums)
        intentedSum = n * (n + 1) / 2

        return int(intentedSum - currentSum)