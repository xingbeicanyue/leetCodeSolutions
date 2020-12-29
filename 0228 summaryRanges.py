"""
给定一个无重复元素的有序整数数组 nums 。
返回恰好覆盖数组中所有数字的最小有序区间范围列表。
也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：
* "a->b" ，如果 a != b
* "a" ，如果 a == b

示例 1：
输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

示例 2：
输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

示例 3：
输入：nums = []
输出：[]

示例 4：
输入：nums = [-1]
输出：["-1"]

示例 5：
输入：nums = [0]
输出：["0"]

提示：
* 0 <= nums.length <= 20
* -2^31 <= nums[i] <= 2^31 - 1
* nums 中的所有值都 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/summary-ranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组
"""

from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result, sIdx = [], 0
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i + 1] > nums[i] + 1:
                result.append(f'{nums[sIdx]}->{nums[i]}' if i > sIdx else str(nums[i]))
                sIdx = i + 1
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.summaryRanges([0, 1, 2, 4, 5, 7])
    print(r)
    r = s.summaryRanges([0, 2, 3, 4, 6, 8, 9])
    print(r)
    r = s.summaryRanges([])
    print(r)
    r = s.summaryRanges([-1])
    print(r)
    r = s.summaryRanges([0])
    print(r)
