class Solution:

	def maxProduct(self,arr):
		# code here
		arr.sort(reverse=True)
        
        return arr[0]*arr[1]
