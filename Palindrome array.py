from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        # code here
        a=arr.copy()
        arr.reverse()
        if arr==a:
            return True
        else:
            return False
