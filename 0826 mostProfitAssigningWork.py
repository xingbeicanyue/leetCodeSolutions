"""
安排工作以达到最大收益

有一些工作：difficulty[i] 表示第 i 个工作的难度，profit[i] 表示第 i 个工作的收益。
现在我们有一些工人。worker[i] 是第 i 个工人的能力，即该工人只能完成难度小于等于 worker[i] 的工作。
每一个工人都最多只能安排一个工作，但是一个工作可以完成多次。
举个例子，如果 3 个工人都尝试完成一份报酬为 1 的同样工作，那么总收益为 $3。如果一个工人不能完成任何工作，他的收益为 $0 。
我们能得到的最大收益是多少？

示例：
输入: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
输出: 100
解释: 工人被分配的工作难度是 [4,4,6,6] ，分别获得 [20,20,30,30] 的收益。

提示:
* 1 <= difficulty.length = profit.length <= 10000
* 1 <= worker.length <= 10000
* difficulty[i], profit[i], worker[i]  的范围是 [1, 10^5]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/most-profit-assigning-work
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        works, worker = sorted(zip(difficulty, profit)), sorted(worker)
        workIdx, maxProfit, length, result = 0, 0, len(works), 0
        for w in worker:
            while workIdx < length and works[workIdx][0] <= w:
                maxProfit = max(maxProfit, works[workIdx][1])
                workIdx += 1
            result += maxProfit
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])
    print(r)
