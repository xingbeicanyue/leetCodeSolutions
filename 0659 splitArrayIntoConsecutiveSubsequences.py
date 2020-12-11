"""
给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个长度至少为 3 的子序列，其中每个子序列都由连续整数组成。
如果可以完成上述分割，则返回 true ；否则，返回 false 。

示例 1：
输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5

示例 2：
输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3, 4, 5
3, 4, 5

示例 3：
输入: [1,2,3,4,4,5]
输出: False
 
提示：
* 1 <= nums.length <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：堆、贪心算法
"""


class Solution:
    def isPossible(self, nums: list) -> bool:
        if len(nums) == 0 or nums[-1] - nums[0] < 2:
            return False

        len1Count, len2Count, len3pCount = 0, 0, 0  # 长度为 1 | 2 | >3 的且可以继续连接的序列数
        nextDigitIdx, prevDigit = 0, nums[0] - 2  # 下一个要访问的数首个下标 | 上一个数
        while nextDigitIdx < len(nums):  # 每轮处理一种数字
            # 获取下一个数字开始位置 -> nextDigitIdx
            curDigitIdx, curDigit = nextDigitIdx, nums[nextDigitIdx]
            while nextDigitIdx < len(nums):
                if nums[nextDigitIdx] > curDigit:
                    break
                nextDigitIdx += 1

            digitCount = nextDigitIdx - curDigitIdx  # 当前数字数量
            if curDigit > prevDigit + 1:  # 数字不连续
                if len1Count + len2Count > 0:  # 有剩余必须连接的序列
                    return False
                else:
                    len1Count = digitCount
            else:
                # 以长度为1、2、3+的顺序为优先级连接序列，其中长度为1、2的序列必须连接，若有剩余则创建新序列
                if digitCount < len1Count + len2Count:
                    return False
                digitLeft = digitCount - (len1Count + len2Count)
                oriLen3pCount = len3pCount
                len3pCount = min(digitLeft, len3pCount) + len2Count
                len2Count = len1Count
                len1Count = max(digitLeft - oriLen3pCount, 0)
            prevDigit = curDigit
        return len1Count + len2Count == 0


if __name__ == '__main__':
    s = Solution()
    r = s.isPossible([1, 2, 3, 3, 4, 5])
    print(r)
    r = s.isPossible([1, 2, 3, 3, 4, 4, 5, 5])
    print(r)
    r = s.isPossible([1, 2, 3, 4, 4, 5])
    print(r)
