class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0 
        current_substring = set()
        max_length = 0 

        while right < len(s):
            if s[right] in current_substring:
                current_substring.remove(s[left])
                left += 1
            else:
                current_substring.add(s[right])
                max_length = max(max_length, right-left +1)
                right += 1

        return max_length