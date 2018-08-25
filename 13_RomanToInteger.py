class Solution:
    trans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        skip_next = False
        for i in range(len(s)):
            if not skip_next:
                if(i < len(s)-1 ):
                    if self.compare(s[i], s[i+1]):
                        total += self.trans[s[i+1]] - self.trans[s[i]]
                        skip_next = True
                    else:
                        total += self.trans[s[i]]
                else:
                    total += self.trans[s[i]]
            else:
                skip_next = False
        return total

    
    def compare(self, s1, s2):
        return self.trans[s1] < self.trans[s2]