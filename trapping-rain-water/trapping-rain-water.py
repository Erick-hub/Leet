class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        size = n - 1
        prev = height[0]
        prev_index = 0
        water = 0
        temp = 0
        
        for i in range(1, size + 1):
            if (height[i] >= prev):
                prev = height[i]
                prev_index = i
                temp = 0
            else:
                water += prev - height[i]
                temp += prev - height[i]



        if (prev_index < size):
            water -= temp
            prev = height[size]
            for i in range(size, prev_index - 1, -1):
                if (height[i] >= prev):
                    prev = height[i]
                else:
                    water += prev - height[i]
        return water