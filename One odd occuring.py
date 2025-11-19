class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]%2==1:
                return i
