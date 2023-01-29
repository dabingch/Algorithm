class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        window = {}

        left, right = 0, 0
        res = 0

        while right < len(s):
            c = s[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            
            res = max(res, right - left)
        
        return res