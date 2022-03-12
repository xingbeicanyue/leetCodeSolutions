"""
保证图可完全遍历

Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3 种类型的边：
* 类型 1：只能由 Alice 遍历。
* 类型 2：只能由 Bob 遍历。
* 类型 3：Alice 和 Bob 都可以遍历。
给你一个数组 edges ，其中 edges[i] = [typei, ui, vi] 表示节点 ui 和 vi 之间存在类型为 typei 的双向边。
请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。
如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。
返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。

示例 1：
输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
输出：2
解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。
再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是 2 。

示例 2：
输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
输出：0
解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。

示例 3：
输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
输出：-1
解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。

提示：
* 1 <= n <= 10^5
* 1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
* edges[i].length == 3
* 1 <= edges[i][0] <= 3
* 1 <= edges[i][1] < edges[i][2] <= n
* 所有元组 (typei, ui, vi) 互不相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # 先连通公共边
        edges1, edges2, remainCount = [], [], n - 1
        disjointSet = [-1] * (n + 1)
        for edge in edges:
            if edge[0] == 3:
                r1, r2 = self._getRoot(disjointSet, edge[1]), self._getRoot(disjointSet, edge[2])
                if r1 != r2:
                    disjointSet[r2] = r1
                    remainCount -= 1
                    if remainCount == 0:  # 已经全部连通
                        return len(edges) - n + 1
            else:
                (edges1 if edge[0] == 1 else edges2).append(edge)
        # 再分别连通类型1、2的边
        disjointSet2 = disjointSet[:]
        if not self._connectEdges(disjointSet, edges1, remainCount) or\
           not self._connectEdges(disjointSet2, edges2, remainCount):
            return -1
        return len(edges) - n + 1 - remainCount

    def _getRoot(self, disjointSet: List[int], idx: int):
        """ 获取并查集根节点 """
        visiteds = []
        while disjointSet[idx] >= 0:
            visiteds.append(idx)
            idx = disjointSet[idx]
        for visited in visiteds:
            disjointSet[visited] = idx
        return idx

    def _connectEdges(self, disjointSet: List[int], edges: List[List[int]], remainCount: int) -> bool:
        """ 连接节点直至全部连通
        :returns: 是否可以连通
        """
        for edge in edges:
            r1, r2 = self._getRoot(disjointSet, edge[1]), self._getRoot(disjointSet, edge[2])
            if r1 != r2:
                disjointSet[r2] = r1
                remainCount -= 1
                if remainCount == 0:
                    return True
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]])
    print(r)
    r = s.maxNumEdgesToRemove(4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]])
    print(r)
    r = s.maxNumEdgesToRemove(4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]])
    print(r)
