"""
单词搜索

给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：
* board 和 word 中只包含大写和小写英文字母。
* 1 <= board.length <= 200
* 1 <= board[i].length <= 200
* 1 <= word.length <= 10^3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、回溯算法
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def searchOnDir(cIdx: int, rowIdx: int, colIdx: int) -> bool:
            """ 探索一个方向 """
            if canVisitedss[rowIdx][colIdx] and board[rowIdx][colIdx] == word[cIdx]:
                canVisitedss[rowIdx][colIdx] = False
                if dfs(cIdx + 1, rowIdx, colIdx):
                    return True
                canVisitedss[rowIdx][colIdx] = True
            return False

        def dfs(cIdx: int, rowIdx: int, colIdx: int) -> bool:
            """ 深度优先搜索，探索一个字符 """
            if cIdx >= len(word):  # 已全部匹配
                return True
            rowIdx -= 1
            if rowIdx >= 0 and searchOnDir(cIdx, rowIdx, colIdx):
                return True
            rowIdx += 2
            if rowIdx < rowCount and searchOnDir(cIdx, rowIdx, colIdx):
                return True
            rowIdx -= 1
            colIdx -= 1
            if colIdx >= 0 and searchOnDir(cIdx, rowIdx, colIdx):
                return True
            colIdx += 2
            if colIdx < colCount and searchOnDir(cIdx, rowIdx, colIdx):
                return True
            return False

        rowCount, colCount = len(board), len(board[0])
        canVisitedss = [[True] * colCount for _ in range(rowCount)]
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == word[0]:
                    canVisitedss[i][j] = False
                    if dfs(1, i, j):
                        return True
                    canVisitedss[i][j] = True
        return False


if __name__ == '__main__':
    s = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    r = s.exist(board, 'ABCCED')
    print(r)
    r = s.exist(board, 'SEE')
    print(r)
    r = s.exist(board, 'ABCB')
    print(r)
