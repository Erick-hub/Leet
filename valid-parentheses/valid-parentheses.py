class Solution:
    def isValid(self, s: str) -> bool:
        ans=True
        e=[]
        expect={'(':')','{':'}','[':']'}
        opening={'(':0,'{':0,'[':0}
        closing={')':0,'}':0,']':0}
        for i in s:
            if i in(opening.keys()):
                opening[i]+=1
                e+=[expect[i]]
            elif i in(closing.keys()):
                if len(e)==0:
                  ans=False
                  break
                if i!=e[-1]:
                  ans=False
                  break
                else: 
                  closing[i]+=1
                  e.pop()
        if opening['(']!=closing[')']:
            ans=False
        elif opening['{']!=closing['}']:
            ans=False
        elif opening['[']!=closing[']']:
            ans=False
        
        return ans