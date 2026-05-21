class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []  # Stores indices
        max_area = 0
        n = len(heights)
        
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                # If stack is empty, it means the popped height was the smallest so far,
                # so its width extends from index 0 to i.
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
            
        # Clear the remaining elements in the stack
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)
            
        return max_area
