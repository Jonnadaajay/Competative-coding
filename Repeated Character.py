class Solution:
    def firstRep(self, s):
        # code here
        n=len(s)
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    return s[i]
        return s[j]
