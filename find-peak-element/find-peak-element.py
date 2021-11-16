import random
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=len(nums)
        if l==1:
            return 0
        x=round(l/2)-1
        return self.findPeak(nums,x-1,x,x+1)
    
    def findPeak(self,nums,left_in,mid_in,right_in):     
            l=len(nums)
            if mid_in==0:
                left_in=l-1
            if mid_in==l-1:
                right_in=0
            mid=nums[mid_in]
            left=nums[left_in]
            right=nums[right_in]
            if mid==left or mid==right:
                return 0
            if mid>left:
                if mid>right:
                    return mid_in
                elif right>left:
                    return self.findPeak(nums,mid_in,right_in,right_in+1)
                else:
                    return self.findPeak(nums,left_in-1,left_in,mid_in)
            elif right>left:
                return self.findPeak(nums,mid_in,right_in,right_in+1)
            
            elif right==left:
                coin=choice([0,1])
                if coin:
                    return self.findPeak(nums,mid_in,right_in,right_in+1)
                else:     
                    return self.findPeak(nums,left_in-1,left_in,mid_in)
            else:
                return self.findPeak(nums,left_in-1,left_in,mid_in)