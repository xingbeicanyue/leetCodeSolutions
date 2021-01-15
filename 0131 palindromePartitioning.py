"""
分割回文串

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。

示例:
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：深度优先搜索、动态规划、回溯算法
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def addText(startIdx: int, partitions: List[str]):
            """ 添加一个回文 """
            if startIdx == len(s):
                result.append(partitions[:])
                return
            for i in range(startIdx + 1, len(s) + 1):
                subStr = s[startIdx: i]
                if subStr != subStr[::-1]:
                    continue
                partitions.append(subStr)
                addText(i, partitions)
                partitions.pop()

        result = []
        addText(0, [])
        return result


if __name__ == '__main__':
    s = Solution()
    r = s.partition('aab')
    print(r)
