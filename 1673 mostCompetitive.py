"""
找出最具竞争力的子序列

给你一个整数数组 nums 和一个正整数 k ，返回长度为 k 且最具竞争力的 nums 子序列。
数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。
在子序列 a 和子序列 b 第一个不相同的位置上，如果 a 中的数字小于 b 中对应的数字，
那么我们称子序列 a 比子序列 b（相同长度下）更具竞争力。
例如，[1,3,4] 比 [1,3,5] 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， 4 小于 5 。

示例 1：
输入：nums = [3,5,2,6], k = 2
输出：[2,6]
解释：在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。

示例 2：
输入：nums = [2,4,3,3,5,4,9,6], k = 4
输出：[2,3,3,4]
 
提示：
* 1 <= nums.length <= 105
* 0 <= nums[i] <= 109
* 1 <= k <= nums.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-most-competitive-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：栈、贪心算法
"""

from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # 思路同#402
        result = []
        removeCount = len(nums) - k
        for num in nums:
            while result and removeCount > 0 and num < result[-1]:
                result.pop()
                removeCount -= 1
            result.append(num)
        del result[k:]
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.mostCompetitive([3, 5, 2, 6], 2)
    print(r)
    r = s.mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4)
    print(r)
