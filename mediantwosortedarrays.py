class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
         # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        half_len = (m + n + 1) // 2
        
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2      # Partition in nums1
            j = half_len - i        # Complementary partition in nums2
            
            # Check edge values, using -inf/inf for out‐of‐bounds
            nums1_left  = nums1[i-1] if i > 0 else float("-inf")
            nums1_right = nums1[i]   if i < m else float("inf")
            nums2_left  = nums2[j-1] if j > 0 else float("-inf")
            nums2_right = nums2[j]   if j < n else float("inf")
            
            # If partitions are too far right in nums1, move left
            if nums1_left > nums2_right:
                hi = i - 1
            # If partitions are too far left in nums1, move right
            elif nums2_left > nums1_right:
                lo = i + 1
            else:
                # Found perfect partition
                if (m + n) % 2 == 1:
                    # Odd total length → max of left halves
                    return max(nums1_left, nums2_left)
                else:
                    # Even total length → average of max left and min right
                    left_max  = max(nums1_left, nums2_left)
                    right_min = min(nums1_right, nums2_right)
                    return (left_max + right_min) / 2.0