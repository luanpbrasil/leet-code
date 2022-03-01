class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = {}
        left = 0
        output = 0
        for i, char in enumerate(s):
            if char not in seen:
                output = max(output, i-left+1)
            else:
                if seen[char] < left:
                    output = max(output, i-left+1)
                else:
                    left = seen[char] + 1
            seen[char] = i
        return output
        