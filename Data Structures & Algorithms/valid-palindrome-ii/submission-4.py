class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        missed = [False]

        def checkPalindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    if missed[0]:
                        return False
                    else:
                        missed[0] = True
                        return checkPalindrome(l+1,r) or checkPalindrome(l,r-1)

                l+=1
                r-=1
            
            return True
        
        return checkPalindrome(l,r)



''' 
abcdefdcba
'''