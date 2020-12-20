"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
使得 nums[i] = nums[j]，并且 i 和 j 的差的绝对值至多为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、哈希表
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numSet = set()
        windowWidth = k + 1
        for i in range(min(windowWidth, len(nums))):
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
        for i in range(windowWidth, len(nums)):
            numSet.remove(nums[i - windowWidth])
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.containsNearbyDuplicate([1, 2, 3, 1], 3)
    print(r)
    r = s.containsNearbyDuplicate([1, 0, 1, 1], 1)
    print(r)
    r = s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    print(r)
