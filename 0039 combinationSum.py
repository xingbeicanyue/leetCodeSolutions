"""
组合总和

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

说明：
* 所有数字（包括 target）都是正整数。
* 解集不能包含重复的组合。 

示例 1：
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]

示例 2：
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

提示：
* 1 <= candidates.length <= 30
* 1 <= candidates[i] <= 200
* candidate 中的每个元素都是独一无二的。
* 1 <= target <= 500

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidateIdx: int, curNums: List[int], sum_: int):
            if sum_ == target:
                result.append(curNums)
                return
            if candidateIdx >= len(candidates):
                return
            curVal = candidates[candidateIdx]
            if curVal > target - sum_:
                return
            while sum_ <= target:
                dfs(candidateIdx + 1, curNums, sum_)
                curNums = curNums + [curVal]
                sum_ += curVal

        result, candidates = [], sorted(candidates)
        dfs(0, [], 0)
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.combinationSum([2, 3, 6, 7], 7)
    print(r)
    r = s.combinationSum([2, 3, 5], 8)
    print(r)
