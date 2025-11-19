class Solution:
    def largest(self, arr):
        # code here
        largest = arr[0]
        for big in arr:
            if big > largest:
                largest = big
        return largest
