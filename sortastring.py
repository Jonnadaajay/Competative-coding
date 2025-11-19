class Solution:
    def sort(self, s): 
        #code here
        a = ""
        s1 = sorted(s)
        for i in s1:
            a += i
        return a
