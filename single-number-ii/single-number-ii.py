class Solution:
    def singleNumber(self,nums: List[int])-> int:
        new_set= set(nums)
        for i in new_set:
            counter=0
            for n in nums:
                if (i==n):
                    counter+=1
                    if counter>1:
                        break
            if counter==1:
                return i   