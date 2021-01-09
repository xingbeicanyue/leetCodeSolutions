"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：字符串
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        maxLen = len(min(strs, key=len))
        for i in range(maxLen):
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    return s[:i]
        else:
            return strs[0][:maxLen]


if __name__ == '__main__':
    s = Solution()
    r = s.longestCommonPrefix(["flower", "flow", "flight"])
    print(r)
    r = s.longestCommonPrefix(["dog", "racecar", "car"])
    print(r)
