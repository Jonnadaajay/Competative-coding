class Solution:
    def firstRep(self, s):
        # code here
        n=len(s)
        for i in range(n):
            if s[i] in s[i+1:n]:
                return  s[i]
        return '#'
