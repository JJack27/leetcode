class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ""
        maximum = 0

        for i in range(len(s)):
            substring = s[i]
            for j in range(i+1,len(s)):
                if s[j] not in substring:
                    substring += s[j]
                    subLength = len(substring)
                    if subLength > maximum:
                        maximum = subLength
                else:
                    subLength = len(substring)
                    if subLength > maximum:
                        maximum = subLength
                    break
            subLength = len(substring)
            if subLength > maximum:
                maximum = subLength

        return maximum