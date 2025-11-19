class Solution:
    def countOddEven(self, arr):
        #Code here
        x=0
        y=0
        for i in arr:
            if i%2==0:
                x=x+1
            else:
                y=y+1
        return(y,x)
