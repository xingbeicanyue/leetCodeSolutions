"""
由斜杠划分区域

在由 1 x 1 方格组成的 N x N 网格 grid 中，每个 1 x 1 方块由 /、\ 或空格构成。这些字符会将方块划分为一些共边的区域。
（请注意，反斜杠字符是转义的，因此 \ 用 "\\" 表示。）。
返回区域的数目。

示例 1：
输入：
[
  " /",
  "/ "
]
输出：2

示例 2：
输入：
[
  " /",
  "  "
]
输出：1

示例 3：
输入：
[
  "\\/",
  "/\\"
]
输出：4

示例 4：
输入：
[
  "/\\",
  "\\/"
]
输出：5

示例 5：
输入：
[
  "//",
  "/ "
]
输出：3

提示：
* 1 <= grid.length == grid[0].length <= 30
* grid[i][j] 是 '/'、'\'、或 ' '。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regions-cut-by-slashes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        def getRoot(disjointSet: List[int], idx: int):
            """ 获取并查集根节点 """
            while idx != disjointSet[idx]:
                idx = disjointSet[idx]
            return idx

        def updateNextConnects(ueIdx: int, deIdx: int):
            """ 更新连通区域（connects, nextConnects） """
            # 更新映射表
            root = getRoot(connects, usIdx)
            mapRoot = connectMap.get(root, dsIdx)
            for i in range(usIdx + 1, ueIdx + 1):
                root2 = getRoot(connects, i)
                mapRoot2 = connectMap.get(root2, dsIdx)
                if mapRoot <= mapRoot2:  # 需保证，映射后的下标更小的作为根节点
                    connects[root2] = root
                else:
                    connects[root] = root2
                    root, mapRoot = root2, mapRoot2
            connectMap[root] = mapRoot
            # 更新连通区域
            for i in range(dsIdx, deIdx + 1):
                connectIdxs[i] = ueIdx

        # 逐行遍历，维护每行连通区域、已结束的区域、新的区域
        length, result = len(grid), 0
        connects = [i for i in range(length)]  # 连通区域，用并查集表示，同组表示同一个连通区域，根节点为组内最小的成员
        for line in grid:
            connectIdxs = [-1] * length  # 每个元素表示该位置由哪个下标连通而来，负数表示新区域
            connectMap = {}  # {connects群组idx: nextConnects群组idx}
            usIdx = dsIdx = 0  # 上|下层连通起始下标
            for i, c in enumerate(line):
                if c == '\\':
                    if i == usIdx:  # 分裂出新区域
                        for j in range(dsIdx, i + 1):
                            connectIdxs[j] = -(i + 1 - dsIdx)  # -1:左侧靠墙区域; -2:中间^形区域
                    else:
                        updateNextConnects(i - 1, i)
                    usIdx, dsIdx = i, i + 1
                elif c == '/':
                    if i == dsIdx:  # 结束区域
                        if i - 1 >= 0:  # 宽度为2的区域合并时，需将connects相应位置合并
                            r1, r2 = getRoot(connects, i - 1), getRoot(connects, i)
                            nr1, nr2 = connectMap.get(r1, length), connectMap.get(r2, length)
                            if nr1 <= nr2:
                                connects[r2] = r1
                            else:
                                connects[r1] = r2
                    else:
                        updateNextConnects(i, i - 1)
                    usIdx, dsIdx = i + 1, i
            if dsIdx < length:
                if usIdx < length:
                    updateNextConnects(length - 1, length - 1)
                else:  # 分裂出新区域
                    connectIdxs[dsIdx] = -3  # 右侧靠墙区域
            # 更新已经结束的区域计数
            for i, c in enumerate(connects):
                result += i == c and (i not in connectMap)  # 没有通往下一层的映射表示该区域已经结束
            # 更新连通区域
            nextConnects = []
            for i, c in enumerate(connectIdxs):
                if c >= 0:
                    nextConnects.append(connectMap[getRoot(connects, c)])
                elif connectIdxs[i] != -2 or i == 0 or connectIdxs[i - 1] != -2:
                    nextConnects.append(i)
                else:  # 宽度为2新区域的后一格
                    nextConnects.append(i - 1)
                    connectIdxs[i] = 0  # 防止连续的-2影响后面的判断
            connects = nextConnects
        result += sum(i == c for i, c in enumerate(connects))
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.regionsBySlashes([" /", "/ "])
    print(r)
    r = s.regionsBySlashes([" /", "  "])
    print(r)
    r = s.regionsBySlashes(["\\/", "/\\"])
    print(r)
    r = s.regionsBySlashes(["/\\", "\\/"])
    print(r)
    r = s.regionsBySlashes(["//", "/ "])
    print(r)
