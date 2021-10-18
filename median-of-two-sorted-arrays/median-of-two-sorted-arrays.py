class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged= nums1+nums2
        if len(merged)==1 or len(set(merged))==1 :
            return merged[0]
            
        merged= self.merge_sort(merged)
        m=len(nums1)
        n=len(nums2)
        new_len= m+n
        
       
    
        if (new_len)%2==0:
            mid= new_len//2-1

            return (merged[mid]+ merged[mid+1])/2
        else:
            mid= new_len//2
            return merged [mid]
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