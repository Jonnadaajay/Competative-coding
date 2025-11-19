def palindrome_check(num):
    str_num = str(num)
    if str_num==str_num[::-1]:
        return True
    else:
        return False
    

def isPalinArray(arr):
    # Code here
    return all(palindrome_check(n) for n in arr)
