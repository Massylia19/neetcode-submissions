class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left, right = 0, 1
        count = [0] * 26 
        max_freq = 0 
        best = 0 

        for right in range(n): 
            index = ord(s[right]) - ord("A")
            count[index] += 1
            max_freq = max(max_freq, count[index])

            while (right - left + 1) - max_freq > k: 
                count[ord(s[left]) - ord("A")] -= 1 
                left += 1 

            best = max(best, right - left + 1)

        return best 
        