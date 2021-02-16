"""
子集

给你一个整数数组 nums ，数组中的元素互不相同。返回该数组所有可能的子集（幂集）。
解集不能包含重复的子集。你可以按任意顺序返回解集。

示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

示例 2：
输入：nums = [0]
输出：[[],[0]]

提示：
* 1 <= nums.length <= 10
* -10 <= nums[i] <= 10
* nums 中的所有元素互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：位运算、数组、回溯算法
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(curNums: List[int], idx: int):
            if idx == len(nums):
                result.append(curNums)
                return
            dfs(curNums, idx + 1)
            dfs(curNums + [nums[idx]], idx + 1)

        result = []
        dfs([], 0)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.subsets([1, 2, 3])
    print(r)
    r = s.subsets([0])
    print(r)
