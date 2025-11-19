class Solution:
    def countOfElements(self, x, arr):
        # Code Here
        y=[]
        for i in range(len(arr)):
            if arr[i]<=x:
                y.append(1)
        return(sum(y))
