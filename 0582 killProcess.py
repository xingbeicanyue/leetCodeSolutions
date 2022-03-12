"""
杀掉进程

系统中存在 n 个进程，形成一个有根树结构。给你两个整数数组 pid 和 ppid ，
其中 pid[i] 是第 i 个进程的 ID ，ppid[i] 是第 i 个进程的父进程 ID。

每一个进程只有一个父进程，但是可能会有一个或者多个子进程。只有一个进程的 ppid[i] = 0 ，意味着这个进程没有父进程。
当一个进程被杀掉的时候，它所有的子进程和后代进程都要被杀掉。

给你一个整数 kill 表示要杀掉​​进程的 ID ，返回杀掉该进程后的所有进程 ID 的列表。可以按任意顺序返回答案。

示例 1：
    3
   / \
  1   5*
     /
    10*
输入：pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
输出：[5,10]
解释：打星号的进程是应该被杀掉的进程。

示例 2：
输入：pid = [1], ppid = [0], kill = 1
输出：[1]

提示：
* n == pid.length
* n == ppid.length
* 1 <= n <= 5 * 10^4
* 1 <= pid[i] <= 5 * 10^4
* 0 <= ppid[i] <= 5 * 10^4
* 仅有一个进程没有父进程
* pid 中的所有值互不相同
* 题目数据保证 kill 在 pid 中

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kill-process
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # 可以根据ppid反推进程对应所有子进程在pid中的下标，由此即可知道每个进程的子进程列表
        # 层次遍历以kill为根节点的树即为所求

        pidChildNodeIdxsDict = {}  # {pid: [子下标]}
        for i, parent in enumerate(ppid):
            pidChildNodeIdxsDict.setdefault(parent, []).append(i)
        result, nextIdx = [kill], 0
        while nextIdx < len(result):
            for childIdx in pidChildNodeIdxsDict.get(result[nextIdx], []):
                result.append(pid[childIdx])
            nextIdx += 1
        return result


if __name__ == '__main__':
    s = Solution()

    r = s.killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5)
    print(r)

    r = s.killProcess([1], [0], 1)
    print(r)
