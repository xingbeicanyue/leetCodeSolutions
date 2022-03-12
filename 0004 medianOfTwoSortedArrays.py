"""
寻找两个正序数组的中位数

给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

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
"""

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 方法1：
        # 若nums1有m个数字，nums2有n个数字，合并后中位数下标e=(m+n-1)//2（总数为偶数的话e+1也是中位数）
        # 对于nums1的下标i，对应nums2的下标j=e-i，若nums1[i] <= nums2[j]
        # 则nums1中下标<i的一定不是中位数，nums2中下标>j的一定不是中位数
        # 因此，如果找到i使nums1[i]<=nums2[j]，且nums1[i+1]>=nums2[j-1]，则中位数一定在这四个数中
        # 假设m<=n，使用二分法找到i，则时间复杂度：O(lg(min(m, n)))

        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:  # 保证nums1长度<=nums2
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1
        medianIdx = (len1 + len2 - 1) // 2  # 合并后下标midIdx或midIdx+1（总数为偶数）的数为中位数
        if len1 == 0:
            return nums2[medianIdx] if len2 % 2 == 1 else (nums2[medianIdx] + nums2[medianIdx + 1]) / 2
        left, right = -1, len1
        while right - left > 1:
            mid1 = (left + right) // 2
            mid2 = medianIdx - mid1
            if nums1[mid1] <= nums2[mid2]:
                left = mid1
            else:
                right = mid1
        left1, right1, left2, right2 = left, left + 1, medianIdx - left - 1, medianIdx - left
        leftMedian = max(nums1[left1] if left1 >= 0 else -1000000, nums2[left2] if left2 >= 0 else -1000000)
        if (len1 + len2) % 2 == 1:
            return leftMedian
        rightMedian = min(nums1[right1] if right1 < len1 else 1000000, nums2[right2] if right2 < len2 else 1000000)
        return (leftMedian + rightMedian) / 2


        # 方法2：
        # 若nums1有m个数字，nums2有n个数字，此问题等价于找第(m+n)/2大的数字（理想情况，不考虑不能被2整除的问题）
        # 使用二分，每次（第k次，从1开始）排除(m+n)/2^(k+1)个数字
        # 第一次排除(m+n)/4个数字，比较a=nums1[(m+n)/4] 与 b=nums2[(m+n)/4]
        # 若a<=b，则表示a必然>=nums1中比a小的数，且a可能>=nums2中比b小的数，因此nums1中比a小的数不可能是中位数
        # 第二次排除(m+n)/8个数字，比较nums1[(m+n)/4+(m+n)/8] 与 nums2[(m+n)/8]，以此类推，最终总共排除(m+n)/2个数组
        # 如果某次比较的数字已超出某数组范围，则中位数必然在另一个数组中
        # 时间复杂度：O(lg(m+n))

        # len1, len2 = len(nums1), len(nums2)
        # if len1 > len2:  # 保证nums1长度<=nums2
        #     nums1, nums2, len1, len2 = nums2, nums1, len2, len1
        # sideCount = (len1 + len2 - 1) // 2  # 平均数左侧未排除的数字数，不断减少至0后left1、left2即为中位数的位置
        # left1 = left2 = 0  # 两个数组中该下标的左侧为已排除的数字
        # while sideCount > 0 and left1 < len1:
        #     off = (sideCount - 1) // 2
        #     if left1 + off >= len1:
        #         newLeft1, newLeft2 = len1 - 1, left2 + sideCount - (len1 - left1)
        #     else:
        #         newLeft1, newLeft2 = left1 + off, left2 + off
        #     if nums1[newLeft1] <= nums2[newLeft2]:
        #         sideCount -= newLeft1 - left1 + 1
        #         left1 = newLeft1 + 1
        #     else:
        #         sideCount -= newLeft2 - left2 + 1
        #         left2 = newLeft2 + 1
        # if left1 >= len1:
        #     return (nums2[left2 + sideCount] + nums2[left2 + sideCount + ((len1 + len2) % 2 == 0)]) / 2
        # else:
        #     if (len1 + len2) % 2 == 1:
        #         return min(nums1[left1], nums2[left2])
        #     if nums1[left1] <= nums2[left2]:
        #         if left1 + 1 < len1 and nums1[left1 + 1] <= nums2[left2]:
        #             return (nums1[left1] + nums1[left1 + 1]) / 2
        #     else:
        #         if left2 + 1 < len2 and nums2[left2 + 1] <= nums1[left1]:
        #             return (nums2[left2] + nums2[left2 + 1]) / 2
        #     return (nums1[left1] + nums2[left2]) / 2


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
