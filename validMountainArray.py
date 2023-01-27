class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if not arr: return False

        if len(arr) < 3: return False

        i = 1
        length = len(arr)
        while i < length and arr[i] > arr[i - 1]:
            i += 1

        if i == 1 or i == length:
            return False

        while i < length and arr[i] < arr[i - 1]:
            i += 1

        return i == length