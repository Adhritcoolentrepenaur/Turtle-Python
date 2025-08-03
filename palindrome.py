def palindrome(s):
    s = s.lower()
    ls = 0
    rs = len(s) - 1
    while ls < rs:
        if s[ls] != s[rs]:
            return False
        ls += 1
        rs -= 1
    return True
 
print( palindrome ('Adhrit'))
 