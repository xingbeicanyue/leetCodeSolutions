"""
存在重复元素 III

在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums[i] 和 nums[j] 的差的绝对值小于等于 t ，
且满足 i 和 j 的差的绝对值也小于等于 ķ 。
如果存在则返回 true，不存在返回 false。

示例 1:
输入: nums = [1,2,3,1], k = 3, t = 0
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1, t = 2
输出: true

示例 3:
输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        def checkAndAdd(num: int) -> bool:
            """ 检查是否有相近数字并加入当前数字至字典中 """
            n = num // t if t != 0 else num
            if (n in numDict) or \
               (n - 1 in numDict and abs(numDict[n - 1] - num) <= t) or \
               (n + 1 in numDict and abs(numDict[n + 1] - num) <= t):
                return True
            numDict[n] = num
            return False

        # 保持#219的滑动窗口
        # 对数字转为t进制，如果除个位以外都相同则表示相近，另需检查窗口中十位±1对应的数字是否相近
        numDict = {}  # {数字//t : 数字}
        windowWidth = k + 1
        for i in range(min(windowWidth, len(nums))):
            if checkAndAdd(nums[i]):
                return True
        for i in range(windowWidth, len(nums)):
            numDict.pop(nums[i - windowWidth] // t if t != 0 else nums[i - windowWidth])
            if checkAndAdd(nums[i]):
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
    print(r)
    r = s.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)
    print(r)
    r = s.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
    print(r)
