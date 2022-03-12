"""
非递减数列

给你一个长度为 n 的整数数组 nums ，请你判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的：对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个 4 变成 1 来使得它成为一个非递减数列。

示例 2:
输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

提示：
* n == nums.length
* 1 <= n <= 10^4
* -10^5 <= nums[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-decreasing-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 遍历数组，若出现nums[i] > nums[i + 1]则必须修改其中一个数字
        # 若将nums[i]降低为nums[i + 1]则可以对之后的影响更小，但需保证nums[i] >= nums[i - 1]
        # 否则只能将nums[i + 1]提升为nums[i]
        # 修改完后继续检查，再次出现不满足非递减的情况即无法调整
        if len(nums) <= 2:
            return True
        errorCount = nums[0] > nums[1]
        lastNum = nums[1]
        for i in range(2, len(nums)):
            if nums[i] < lastNum:
                if errorCount == 1:
                    return False
                errorCount = 1
                if nums[i] >= nums[i - 2]:
                    lastNum = nums[i]
            else:
                lastNum = nums[i]
        return True


if __name__ == '__main__':
    s = Solution()

    r = s.checkPossibility([4, 2, 3])
    print(r)

    r = s.checkPossibility([4, 2, 1])
    print(r)
