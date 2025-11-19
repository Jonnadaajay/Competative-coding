class Solution:
    def modify(self, s):
        # code here
        res = ""
        
        for i in s:
            if(i == " "):
                continue
            else:
                res += i
        
        return res
