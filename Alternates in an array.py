class Solution:
    def getAlternates(self, arr):
        # Code Here
        a = []
        for i in range(0,len(arr),2):
            a.append(arr[i])
        return a
