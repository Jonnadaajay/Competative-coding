class Solution:
    def rotate(self, arr):
        last = arr[-1]
        arr.pop()
        arr.insert(0,last)
        return arr
    
