"""
通过删除字母匹配到字典里最长单词

给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。

示例 1：
输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"

示例 2：
输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"

提示：
* 1 <= s.length <= 1000
* 1 <= dictionary.length <= 1000
* 1 <= dictionary[i].length <= 1000
* s 和 dictionary[i] 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：数组、双指针、字符串、排序
"""

from typing import List


class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        strs = sorted(dictionary, key=lambda x: (-len(x), x))  # 按长度降序与字典升序对dictionary排序
        for s2 in strs:
            idx = -1
            for c in s2:
                idx = s.find(c, idx + 1)
                if idx < 0:  # 匹配失败
                    break
            if idx >= 0:  # 匹配成功
                return s2
        return ''


if __name__ == '__main__':
    s = Solution()

    r = s.findLongestWord('abpcplea', ['ale', 'apple', 'monkey', 'plea'])
    print(r)

    r = s.findLongestWord('abpcplea', ['a', 'b', 'c'])
    print(r)
