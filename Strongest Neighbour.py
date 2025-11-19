class Solution:
    def maxAdj(self, arr):
        # code here
        a=[]
        for i in range(len(arr)-1):
            if arr[i]>=arr[i+1]:
                a.append(arr[i])
            else:
                a.append(arr[i+1])
        return a
