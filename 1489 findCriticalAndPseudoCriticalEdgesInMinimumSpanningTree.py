"""
找到最小生成树里的关键边和伪关键边

给你一个 n 个点的带权无向连通图，节点编号为 0 到 n-1 ，同时还有一个数组 edges ，
其中 edges[i] = [fromi, toi, weighti] 表示在 fromi 和 toi 节点之间有一条带权无向边。
最小生成树 (MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权值和最小。
请你找到给定图中最小生成树的所有关键边和伪关键边。
如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。
伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。
请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。

示例 1：
        2
     /     \
    /       \
   1 -- 0 -- 3
    \   |   /
     \  |  /
        4
输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
输出：[[0,1],[2,3,4,5]]
解释：上图描述了给定图。下图是所有的最小生成树。
        2               2              2              2
     /     \         /     \        /              /
    /       \       /       \      /              /
   1 -- 0    3     1 -- 0    3    1 -- 0 -- 3    1 -- 0 -- 3
            /           |                 /           |
           /            |                /            |
        4               4              4              4
注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。

示例 2 ：
        1
     /     \
    /       \
   0         2
    \       /
     \     /
        3
输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
输出：[[],[0,1,2,3]]
解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。

提示：
* 2 <= n <= 100
* 1 <= edges.length <= min(200, n * (n - 1) / 2)
* edges[i].length == 3
* 0 <= fromi < toi < n
* 1 <= weighti <= 1000
* 所有 (fromi, toi) 数对都是互不相同的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：深度优先搜索、并查集
"""

from typing import Dict, List, Set, Tuple


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 思路：
        # Kruskal生成最小生成树，最小生成树中的边可能是关键边，也可能不是
        # 遇到不是最小生成树的边则通过深度优先搜索找到环
        # 如果环中有至少另外一个权值等于当前边的边，则它们是伪关键边（包括当前边）
        # 遍历完最小生成树后，也要对与树中最大权值相等的剩余边进行上述找环判断的操作，他们也可能是伪关键边
        # 最小生成树中排除伪关键边后的剩余边即为关键边

        valueEdges = []  # [[权值, 起始节点, 终止节点, 边下标]]
        for i, edge in enumerate(edges):
            valueEdges.append([edge[2], edge[0], edge[1], i])
        valueEdges.sort()
        mstEdgeIdxs, pmstEdgeIdxs = set(), set()  # [最小生成树边] | [并不属于所有最小生成树的边]
        graph = {}  # 已访问的图 {边起点: {(边终点, 边下标)}}
        disjointSet, connectedCount, idx, maxValue = [-1] * n, 1, 0, 0
        while idx < len(valueEdges):
            edge = valueEdges[idx]
            r1, r2 = self._getRoot(disjointSet, edge[1]), self._getRoot(disjointSet, edge[2])
            if r1 != r2:
                disjointSet[r2] = r1
                mstEdgeIdxs.add(edge[3])
                graph.setdefault(edge[1], set()).add((edge[2], edge[3]))
                graph.setdefault(edge[2], set()).add((edge[1], edge[3]))
                connectedCount += 1
                if connectedCount == n:
                    maxValue = edge[0]  # 最小生成树中的边最大权值
                    break
            else:
                self._dfsFindRing(n, graph, edges, edge[3], edge[0], pmstEdgeIdxs)
            idx += 1
        for i in range(idx + 1, len(valueEdges)):
            edge = valueEdges[i]
            if edge[0] > maxValue:
                break
            self._dfsFindRing(n, graph, edges, edge[3], edge[0], pmstEdgeIdxs)
        return [list(mstEdgeIdxs - pmstEdgeIdxs), list(pmstEdgeIdxs)]

    def _getRoot(self, disjointSet: List[int], idx: int):
        """ 获取idx在并查集的根节点 """
        visiteds = []
        while disjointSet[idx] >= 0:
            visiteds.append(idx)
            idx = disjointSet[idx]
        for visited in visiteds:
            disjointSet[visited] = idx
        return idx

    def _dfsFindRing(self, n: int, graph: Dict[int, Set[Tuple[int, int]]], edges: List[List[int]], startEdgeIdx: int,
                     value: int, pmstEdgeIdxs: Set[int]):
        """ 深度优先搜索找环，将环中权值为value的边加入pmstEdgeIdxs """

        def doDfs() -> bool:
            nextNodes = graph.get(paths[-1][0], set())
            for nextNode in filter(lambda x: x[0] != paths[-2][0], nextNodes):  # 忽略直接来回的边
                paths.append(nextNode)
                if visiteds[nextNode[0]]:  # 找到环
                    for node in paths:
                        if edges[node[1]][2] == value:
                            maxValueEdges.add(node[1])
                    return True
                visiteds[nextNode[0]] = True
                if doDfs():
                    return True
                visiteds[nextNode[0]] = False
                paths.pop()

        startEdge = edges[startEdgeIdx]
        paths = [(startEdge[0], startEdgeIdx), (startEdge[1], startEdgeIdx)]
        visiteds = [False] * n
        visiteds[startEdge[0]], visiteds[startEdge[1]] = True, True
        maxValueEdges = {startEdgeIdx}
        doDfs()
        if len(maxValueEdges) >= 2:
            pmstEdgeIdxs |= maxValueEdges


if __name__ == '__main__':
    s = Solution()
    r = s.findCriticalAndPseudoCriticalEdges(5, [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3],
                                                 [1, 4, 6]])
    print(r)
    r = s.findCriticalAndPseudoCriticalEdges(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]])
    print(r)
