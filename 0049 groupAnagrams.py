"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：
* 所有输入均为小写字母。
* 不考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：哈希表、字符串
"""


class Solution:
    def groupAnagrams(self, strs: list) -> list:
        sortedStrs = {}  # {按字符排序的单词 : 原单词}
        for word in strs:
            sortedStrs.setdefault(''.join(sorted(word)), []).append(word)
        return list(sortedStrs.values())


if __name__ == '__main__':
    s = Solution()
    r = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(r)
