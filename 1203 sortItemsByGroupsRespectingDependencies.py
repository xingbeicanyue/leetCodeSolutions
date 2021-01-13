"""
公司共有 n 个项目和  m 个小组，每个项目要不无人接手，要不就由 m 个小组之一负责。
group[i] 表示第 i 个项目所属的小组，如果这个项目目前无人接手，那么 group[i] 就等于 -1。
（项目和小组都是从零开始编号的）小组可能存在没有接手任何项目的情况。
请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：
* 同一小组的项目，排序后在列表中彼此相邻。
* 项目之间存在一定的依赖关系，我们用一个列表 beforeItems 来表示，其中 beforeItems[i] 表示在进行第 i 个项目前
 （位于第 i 个项目左侧）应该完成的所有项目。
如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个空列表。

示例 1：
  Item    Group   Before
  0       -1
  1       -1      6
  2       1       5
  3       0       6
  4       0       3,6
  5       1
  6       0
  7       -1
输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
输出：[6,3,4,1,5,2,0,7]

示例 2：
输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
输出：[]
解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。

提示：
* 1 <= m <= n <= 3 * 10^4
* group.length == beforeItems.length == n
* -1 <= group[i] <= m - 1
* 0 <= beforeItems[i].length <= n - 1
* 0 <= beforeItems[i][j] <= n - 1
* i != beforeItems[i][j]
* beforeItems[i] 不含重复元素

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：深度优先搜索、图、拓扑排序
"""

from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        def doItem(item: int, group: int):
            """ 执行项目 """
            result.append(item)
            # 更新项目数据
            for afterItem in afterItems[item]:
                itemIndegrees[afterItem] -= 1
                if itemIndegrees[afterItem] == 0 and newGroup[afterItem] == group:
                    doItem(afterItem, group)

        newGroup = [g if g >= 0 else m + i for i, g in enumerate(group)]  # 给每个无人接手的项目都赋予新的项目组以示区分
        itemIndegrees, afterItems = [len(beforeItem) for beforeItem in beforeItems], [[] for _ in range(n)]
        beforeGroups, afterGroups = [set() for _ in range(m + n)], [set() for _ in range(m + n)]
        for afterItem, items in enumerate(beforeItems):
            for beforeItem in items:
                afterItems[beforeItem].append(afterItem)
                beforeGroup, afterGroup = newGroup[beforeItem], newGroup[afterItem]
                if beforeGroup != afterGroup:
                    beforeGroups[afterGroup].add(beforeGroup)
                    afterGroups[beforeGroup].add(afterGroup)
        groupItems = [set() for _ in range(m + n)]
        for item, g in enumerate(newGroup):
            groupItems[g].add(item)

        result = []
        nextGroups = [i for i, g in enumerate(beforeGroups) if not g]  # [候选小组]
        while nextGroups:
            canDoGroup = nextGroups.pop()  # [即将工作的小组]
            canDoItems = [item for item in groupItems[canDoGroup] if itemIndegrees[item] == 0]  # [即将进行的项目]
            beforeCount = len(result)
            for canDoItem in canDoItems:
                doItem(canDoItem, canDoGroup)
            if len(result) < beforeCount + len(groupItems[canDoGroup]):  # 该组还有剩余的项目无法进行
                return []
            # 更新小组数据
            for afterGroup in afterGroups[canDoGroup]:
                beforeGroups[afterGroup].remove(canDoGroup)
                if not beforeGroups[afterGroup]:
                    nextGroups.append(afterGroup)

        return result if len(result) == n else []


if __name__ == '__main__':
    s = Solution()
    r = s.sortItems(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []])
    print(r)
    r = s.sortItems(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3], [], [4], []])
    print(r)
