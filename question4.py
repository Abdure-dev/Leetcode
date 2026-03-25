

def findMedianSortedArrays(nums1: list[int], nums2: list[int])->float:
    if len(nums1) == 0:
        return nums2
    if len(nums2) == 0:
        return nums1
    else:
        first1, *rest1 = nums1
        first2, *rest2 = nums2

        if first1 < first2:
            return [first1] + findMedianSortedArrays(rest1,nums2)
        else:
            return [first2] + findMedianSortedArrays(nums1, rest2)
        
def find_median(list1, list2):
    sorted_list = findMedianSortedArrays(list1,list2)
    middle = len(sorted_list)//2
    if len(sorted_list)%2 == 0:
        return (sorted_list[middle] + sorted_list[middle-1])/2
    else:
        return sorted_list[middle]

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        merged = []
        n, m = len(nums1), len(nums2)

        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        if i < n:
            merged.extend(nums1[i:])
        if j < m:
            merged.extend(nums2[j:])

        mid = (n + m) // 2
        if (n + m) % 2 == 1:
            return float(merged[mid])
        return (merged[mid - 1] + merged[mid]) / 2.0
