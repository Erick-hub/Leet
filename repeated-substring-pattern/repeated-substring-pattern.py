class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
       if not s:
        return false
        
       ss=s+s
       return s in ss[1:-1]
        