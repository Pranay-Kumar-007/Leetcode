class Solution:
    def isPalindrome(self, s: str) -> bool:
        z=""
        for i in s.lower():
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
                z=z+i
        j=len(z)-1
        for i in range(j):
            if z[i]!=z[j]:
                return False
            j=j-1
        return True
        
