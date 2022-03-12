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
"""

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(cIdx: int, rowIdx: int, colIdx: int) -> bool:
            """ 匹配字符word[cIdx] """
            if visitedss[rowIdx][colIdx] or board[rowIdx][colIdx] != word[cIdx]:
                return False
            cIdx += 1
            if cIdx == len(word):  # 已全部匹配
                return True
            visitedss[rowIdx][colIdx] = True
            result = (rowIdx > 0 and dfs(cIdx, rowIdx - 1, colIdx)) or\
                     (rowIdx < height - 1) and dfs(cIdx, rowIdx + 1, colIdx) or\
                     (colIdx > 0 and dfs(cIdx, rowIdx, colIdx - 1)) or\
                     (colIdx < width - 1 and dfs(cIdx, rowIdx, colIdx + 1))
            visitedss[rowIdx][colIdx] = False
            return result

        height, width = len(board), len(board[0])
        visitedss = [[False] * width for _ in range(height)]
        return any(dfs(0, i, j) for i in range(height) for j in range(width))


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
