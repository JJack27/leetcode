class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        max_val = 0
        stack = []
        i = 0
        while i < len(heights):
            if(stack == [] or heights[stack[-1]] <= heights[i]):
                print("->", heights[i])
                stack.append(i)
                i += 1
            else:
                # pop from the stack
                min_val = stack.pop(-1)
                
                if(stack == []):
                    area = i * heights[min_val]
                else:
                    area = heights[min_val] * (i - stack[-1] -1)
                print(heights[min_val], heights[i], area)
                if(area > max_val):
                    max_val = area
            
        
        while(stack != []):
            min_val = stack.pop(-1)
            
            if(stack == []):
                area = i * heights[min_val]
            else:
                area = heights[min_val] * (i - stack[-1] -1)
            if(area > max_val):
                max_val = area
            print(heights[min_val], area)
        return max_val

a = Solution()
print(a.largestRectangleArea([6, 2, 6 ,5, 4, 5, 1, 6]))
