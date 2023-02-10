class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums: return -1

        return 2 * sum(set(nums)) - sum(nums)