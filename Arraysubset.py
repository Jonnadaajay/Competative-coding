class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a = sorted(a)
        b = sorted(b)
        j=0
        
        for i in range(len(a)):
           
            if j<len(b) and a[i]==b[j]:

                j=j+1
                if j==len(b):
                   
                    break
        
        if j==len(b):
            return 1
        return 0
