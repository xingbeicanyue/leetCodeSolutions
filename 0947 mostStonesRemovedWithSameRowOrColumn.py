"""
移除最多的同行或同列石头

n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
如果一块石头的同行或者同列上有其他石头存在，那么就可以移除这块石头。
给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回可以移除的石子的最大数量。

示例 1：
输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
输出：5
解释：一种移除 5 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。

示例 2：
输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
输出：3
解释：一种移除 3 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。

示例 3：
输入：stones = [[0,0]]
输出：0
解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。

提示：
* 1 <= stones.length <= 1000
* 0 <= xi, yi <= 10^4
* 不会有两块石头放在同一个坐标点上

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：深度优先搜索、并查集
"""

from typing import Dict, List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones, disjointSet = sorted(stones), {}
        lineSet, joinCount = {stones[0][1]}, 0  # {y坐标} | 合并次数
        for i in range(1, len(stones)):
            lineSet.add(stones[i][1])
            if stones[i - 1][0] != stones[i][0]:
                continue
            root1, root2 = self.getRoot(disjointSet, stones[i - 1][1]), self.getRoot(disjointSet, stones[i][1])
            if root1 != root2:
                disjointSet[root2] = root1
                joinCount += 1
        return len(stones) - len(lineSet) + joinCount

    def getRoot(self, disjointSet: Dict[int, int], idx: int):
        """ 获取并查集中idx对应的根节点 """
        visiteds = []
        while idx in disjointSet:
            visiteds.append(idx)
            idx = disjointSet[idx]
        for visited in visiteds:
            disjointSet[visited] = idx
        return idx


if __name__ == '__main__':
    s = Solution()
    r = s.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])
    print(r)
    r = s.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]])
    print(r)
    r = s.removeStones([[0, 0]])
    print(r)
