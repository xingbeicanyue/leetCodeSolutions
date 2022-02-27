"""
N 皇后

n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个不同的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]

提示：
* 1 <= n <= 9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、回溯
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 回溯，逐列放置皇后
        result = []
        resultStrs = ['.' * i + 'Q' + '.' * (n - i - 1) for i in range(n)]  # [预设的结果字符串]
        # [横向/左下-右上斜向/左上-右下斜向 是否被攻击]
        attackRows, attackDTs, attackTDs = [False] * n, [False] * (n * 2 - 1), [False] * (n * 2 - 1)
        queenYs = []  # 当前解：[各列上的y坐标]

        def dfs(x, y: int):
            if attackRows[y] or attackDTs[x - y] or attackTDs[x + y]:
                return
            queenYs.append(y)
            if len(queenYs) == n:  # 找到答案
                result.append([resultStrs[y] for y in queenYs])
            else:
                attackRows[y] = attackDTs[x - y] = attackTDs[x + y] = True
                for i in range(n):
                    dfs(x + 1, i)
                attackRows[y] = attackDTs[x - y] = attackTDs[x + y] = False
            queenYs.pop()

        for i in range(n):
            dfs(0, i)
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.solveNQueens(4)
    print(r)

    r = s.solveNQueens(1)
    print(r)
