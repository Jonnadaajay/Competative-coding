class Solution:
    def getMoreAndLess(self, arr, target):
		# code here
		a=[]
        b=[]
        for i in range(len(arr)):
            if arr[i]<=target:
                a.append(i)
            if arr[i]>=target:
                b.append(i)
        return len(a),len(b)
