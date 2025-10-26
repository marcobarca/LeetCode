from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead - O(m+n)
        """
        t = []
        nums1_copy = nums1[:m]
        i = j = 0
        while i < m and j < n:
            if nums1_copy[i] < nums2[j]:
                t.append(nums1_copy[i])
                i +=1
            else:
                t.append(nums2[j])
                j += 1

        t.extend(nums1_copy[i:])
        t.extend(nums2[j:])
        nums1[:] = t
