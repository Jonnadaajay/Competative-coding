class Solution:
    def isBinary(self, s):
        #code here
        for i in range(0,len(s)):
            if s[i] != '0' and s[i] != '1':
                return False
        return True
