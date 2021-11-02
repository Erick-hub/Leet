class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        ans=1
        largest=1
        
        nums=self.merge_sort(nums)
        temp=nums[0]
  
        for i in nums[1:]:
           
            if i==temp+1:    
                ans+=1
            elif i==temp:
                continue
            else:
                if ans>largest:
                    largest=ans
                    ans=1
                else:
                    ans=1
            temp=i
        if ans>largest:
                    largest=ans
                    ans=1
        return largest
    
    def merge_sort(self,l):
      if len(l) > 1:
          output=[]
          mid= len(l)//2
          L= l[:mid]
          R= l[mid:]

          self.merge_sort(L)
          self.merge_sort(R)
          i=j=k=0
          while i < len(L) and j < len(R):
              temp=[]
              if L[i]> R[j]:
                  l[k]=R[j]
                  j+=1

              else:
                  l[k]=L[i]
                  i+=1
              k+=1
          while i < len(L):
              l[k] = L[i]
              i += 1
              k += 1

          while j < len(R):
              l[k] = R[j]
              j += 1
              k += 1
          return l