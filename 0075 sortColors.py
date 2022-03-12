"""
颜色分类

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]

示例 3：
输入：nums = [0]
输出：[0]

示例 4：
输入：nums = [1]
输出：[1]

提示：
* n == nums.length
* 1 <= n <= 300
* nums[i] 为 0、1 或 2

进阶：
* 你可以不使用代码库中的排序函数来解决这道题吗？
* 你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right, cur = 0, len(nums) - 1, 0  # nums[:left]为0的范围 | nums[right+1:]为2的范围
        while cur <= right:
            if nums[cur] == 0:
                nums[cur], nums[left] = 1, 0
                left += 1
                cur += 1
            elif nums[cur] == 1:
                cur += 1
            else:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1


if __name__ == '__main__':
    s = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    s.sortColors(nums)
    print(nums)

    nums = [2, 0, 1]
    s.sortColors(nums)
    print(nums)

    nums = [0]
    s.sortColors(nums)
    print(nums)

    nums = [1]
    s.sortColors(nums)
    print(nums)
