class Solution:
    def longest(self, arr):
        # code here
        string=""
        for i in arr:
            if len(i)>len(string):
                string=i
        return string
