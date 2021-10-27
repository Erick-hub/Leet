class Solution(object):
    def wordBreak(self, s, wordDict):
        def canBreak(s, m, wordDict):
            #exit condition
            if s in m: return m[s]
            
            if s in wordDict: 
                m[s] = True
                return True
           
            for i in range(1, len(s)):
                r = s[i:] #right side           #s[0:i]left side
                if r in wordDict and canBreak(s[0:i], m, wordDict):
                    m[s] = True
                    return True
            
            m[s] = False
            return False
            
        return canBreak(s, {}, set(wordDict))