"""
缺失的第一个正数

给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？

示例 1：
输入：nums = [1,2,0]
输出：3

示例 2：
输入：nums = [3,4,-1,1]
输出：2

示例 3：
输入：nums = [7,8,9,11,12]
输出：1

提示：
* 0 <= nums.length <= 300
* -2^31 <= nums[i] <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 负数和>len(nums)的数与结果无关，都改为0
        length = len(nums)
        for i in range(length):
            if nums[i] < 0 or nums[i] > length:
                nums[i] = 0
        # 使用与#448类似的方式标记访问到的数字
        length += 1  # 用以区分0和len(nums)
        for i, num in enumerate(nums):
            if num % length != 0:
                nums[num % length - 1] += length
        # 找到第一个<length的值对应的位置+1即为没有访问到的数字
        for i, num in enumerate(nums):
            if num < length:
                return i + 1
        return length


if __name__ == '__main__':
    s = Solution()
    r = s.firstMissingPositive([1, 2, 0])
    print(r)
    r = s.firstMissingPositive([3, 4, -1, 1])
    print(r)
    r = s.firstMissingPositive([7, 8, 9, 11, 12])
    print(r)
