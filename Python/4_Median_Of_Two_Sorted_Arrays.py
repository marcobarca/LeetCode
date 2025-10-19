class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_left = (len(nums1) + len(nums2) + 1) // 2
        if len(nums1) <= len(nums2):
            left, right = 0, len(nums1)
            while left <= right:
                # Left array's cut
                i = (left + right) // 2
                # Right array's cut
                j = total_left - i
                nums1_left_max = nums1[i - 1] if i > 0 else None
                nums1_right_min = nums1[i]  if i < len(nums1) else None

                nums2_left_max = nums2[j - 1] if j > 0 else None
                nums2_right_min = nums2[j] if j < len(nums2) else None

                cond1 = (nums1_left_max is None or nums2_right_min is None or nums1_left_max <= nums2_right_min)
                cond2 = (nums2_left_max is None or nums1_right_min is None or nums2_left_max <= nums1_right_min)

                # cut found
                if cond1 and cond2:
                    left_candidates = [x for x in [nums1_left_max, nums2_left_max] if x is not None]
                    right_candidates = [x for x in [nums1_right_min, nums2_right_min] if x is not None]

                    left_max = max(left_candidates) if left_candidates else None
                    right_min = min(right_candidates) if right_candidates else None
                    if (len(nums1) + len(nums2)) % 2 > 0:
                        return float(left_max)
                    else:
                        return float((left_max + right_min) / 2)

                elif nums1_left_max is not None and nums2_right_min is not None and nums1_left_max > nums2_right_min:
                    right = i - 1
                else:
                    left = i + 1
        else:
           return self.findMedianSortedArrays(nums2, nums1)

        
