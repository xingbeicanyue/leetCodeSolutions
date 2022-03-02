"""
零钱兑换

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0

示例 4：
输入：coins = [1], amount = 1
输出：1

示例 5：
输入：coins = [1], amount = 2
输出：2

提示：
* 1 <= coins.length <= 12
* 1 <= coins[i] <= 2^31 - 1
* 0 <= amount <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：广度优先搜索、数组、动态规划
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # 方法1：深度优先搜索 + 剪枝
        def dfs(curAmount: int, nextCoinIdx: int, curCount: int):
            """ 使用nextCoinIdx及之后的硬币拼出curAmount
            :param curCount: 之前已使用的硬币数
            """
            nonlocal result
            coin = sortedCoins[nextCoinIdx]
            curMaxCoinCount = curAmount // coin
            if curCount + curMaxCoinCount >= result:  # 已经不可能超过当前最优解
                return
            if curMaxCoinCount * coin == curAmount:  # 已使用当前最大面额拼出指定金额
                result = curCount + curMaxCoinCount
            elif nextCoinIdx < len(sortedCoins) - 1:
                for j in range(curMaxCoinCount, -1, -1):
                    dfs(curAmount - j * coin, nextCoinIdx + 1, curCount + j)

        # 深度优先搜索，从大到小，依次决定每个面额使用的硬币数
        sortedCoins = sorted(coins, reverse=True)  # 先使用大面额的硬币可以大概率更快找到最优解
        result = amount + 1
        dfs(amount, 0, 0)
        return result if result <= amount else -1


        # 方法2：动态规划
        # def getMinChange(amount: int) -> int:
        #     """ 计算拼出amount的最小硬币数 """
        #     if amount not in changes:
        #         if amount <= 0:
        #             changes[amount] = amount
        #         else:
        #             result = amount + 1  # 若之后result依然>amount，则表示无法组成该金额
        #             for coin in coins:
        #                 count = getMinChange(amount - coin)
        #                 if count >= 0:
        #                     result = min(result, count)
        #             changes[amount] = result + 1 if result <= amount else -1
        #     return changes[amount]
        #
        # changes = {}  # {金额: 最小硬币个数（负数表示无法组成该金额）}
        # return getMinChange(amount)


if __name__ == '__main__':
    s = Solution()

    r = s.coinChange([1, 2, 5], 11)
    print(r)

    r = s.coinChange([2], 3)
    print(r)

    r = s.coinChange([1], 0)
    print(r)

    r = s.coinChange([1], 1)
    print(r)

    r = s.coinChange([1], 2)
    print(r)
