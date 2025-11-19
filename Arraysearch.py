class Solution:
    def search(self, arr, x):
        # code here
        index = -1
        n = len(arr)
        for i in range(len(arr)):
            if arr[i]==x:
                index=i
                break
        return index
