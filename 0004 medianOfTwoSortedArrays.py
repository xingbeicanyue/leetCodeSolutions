"""
寻找两个正序数组的中位数

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000

提示：
* nums1.length == m
* nums2.length == n
* 0 <= m <= 1000
* 0 <= n <= 1000
* 1 <= m + n <= 2000
* -10^6 <= nums1[i], nums2[i] <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、二分查找、分治算法
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:  # 保证nums1长度<=nums2
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1
        sideCount = (len1 + len2 - 1) // 2  # 平均数左侧的数字数，不断减少至0后left1、left2即为中位数的位置
        left1 = left2 = 0
        while sideCount > 0 and left1 < len1:
            off = (sideCount - 1) // 2
            if left1 + off >= len1:
                newLeft1, newLeft2 = len1 - 1, left2 + sideCount - (len1 - left1)
            else:
                newLeft1, newLeft2 = left1 + off, left2 + off
            if nums1[newLeft1] <= nums2[newLeft2]:
                sideCount -= newLeft1 - left1 + 1
                left1 = newLeft1 + 1
            else:
                sideCount -= newLeft2 - left2 + 1
                left2 = newLeft2 + 1
        if left1 >= len1:
            return (nums2[left2 + sideCount] + nums2[left2 + sideCount + ((len1 + len2) % 2 == 0)]) / 2
        else:
            if (len1 + len2) % 2 == 1:
                return min(nums1[left1], nums2[left2])
            if nums1[left1] <= nums2[left2]:
                if left1 + 1 < len1 and nums1[left1 + 1] <= nums2[left2]:
                    return (nums1[left1] + nums1[left1 + 1]) / 2
            else:
                if left2 + 1 < len2 and nums2[left2 + 1] <= nums1[left1]:
                    return (nums2[left2] + nums2[left2 + 1]) / 2
            return (nums1[left1] + nums2[left2]) / 2


if __name__ == '__main__':
    s = Solution()
    r = s.findMedianSortedArrays([1, 3], [2])
    print(r)
    r = s.findMedianSortedArrays([1, 2], [3, 4])
    print(r)
    r = s.findMedianSortedArrays([0, 0], [0, 0])
    print(r)
    r = s.findMedianSortedArrays([], [1])
    print(r)
    r = s.findMedianSortedArrays([2], [])
    print(r)
