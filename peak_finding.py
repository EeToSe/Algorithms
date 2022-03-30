class Solution(object):
    def __init__(self):
        pass
    def findPeakElement(self, nums):
        """
        Recurrence: find the peak value
        """
        num = len(nums)
        # base case
        if num == 0:
            return None
        mid = num // 2
        if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
            peak = self.findPeakElement(nums[0:mid])
            if peak:
                return peak
        elif mid + 1 < num and nums[mid] < nums[mid + 1]:
            peak = self.findPeakElement(nums[mid+1:])
            if peak:
                return peak
        else:
            return nums[mid]
    # def findPeakElement(self, nums):
    #     """
    #     left and right pointer: find the peak index
    #     """
    #     left = 0
    #     right = len(nums) - 1
    #     ans = None
    #     while (left <= right):
    #         mid = (left+right) // 2
    #         if mid - 1 >= left and nums[mid] < nums[mid - 1]:
    #             right = mid - 1
    #         elif mid + 1 <= right and nums[mid] < nums[mid +1]:
    #             left = mid + 1
    #         else:
    #             ans = mid
    #             break
    #     return ans
peak = Solution().findPeakElement([1,2,3,1])
print(peak)