class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        #code here
        a = len(arr) // 2
        left_ele = arr[:a]
        right_ele = arr[a:]
        total = sum(left_ele) - sum(right_ele)
        return abs(total)
