class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
            Median of two sorted arrays nums1 and nums2 of different length m, n, assuming m < n
            Partition as follows
            Left part              Right part
            A[0: i]              A[i: m]
            B[0: j]              B[j: n]
            Where i + j = (m+n+1)//2

            We find the max i satisfy A[i-1] <= B[j]
            Proof: 1. i exists   2. A[i] > B[j+1]  ----> A[i] > B[j-1]
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m = len(nums1)
        n = len(nums2)
        left, right = 0, m
        infi = 2**40
        while (left <= right):
            i = (left+right)//2
            j = (m+n+1)//2 - i
            nums1_leftmax = (-infi if i == 0 else nums1[i-1])
            nums1_rightmin = (infi if i == m else nums1[i])
            nums2_leftmax = (-infi if j == 0 else nums2[j - 1])
            nums2_rightmin = (infi if j == n else nums2[j])
            if nums1_leftmax <= nums2_rightmin:
                m1, m2 = max(nums1_leftmax, nums2_leftmax), min(nums1_rightmin, nums2_rightmin)
                left = i + 1
            else:
                right = i - 1

        if (m+n)%2 == 0:
            return (m1+m2)/2
        else:
            return m1

print(Solution().findMedianSortedArrays([1,2], [3,4]))
