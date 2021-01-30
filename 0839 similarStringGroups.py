"""
相似字符串组

如果交换字符串 X 中的两个不同位置的字母，使得它和字符串 Y 相等，那么称 X 和 Y 两个字符串相似。
如果这两个字符串本身是相等的，那它们也是相似的。
例如，"tars" 和 "rats" 是相似的 (交换 0 与 2 的位置)；
"rats" 和 "arts" 也是相似的，但是 "star" 不与 "tars"，"rats"，或 "arts" 相似。
总之，它们通过相似性形成了两个关联组：{"tars", "rats", "arts"} 和 {"star"}。
注意，"tars" 和 "arts" 是在同一组中，即使它们并不相似。
形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。
给你一个字符串列表 strs。列表中的每个字符串都是 strs 中其它所有字符串的一个字母异位词。请问 strs 中有多少个相似字符串组？

示例 1：
输入：strs = ["tars","rats","arts","star"]
输出：2

示例 2：
输入：strs = ["omv","ovm"]
输出：1

提示
* 1 <= strs.length <= 100
* 1 <= strs[i].length <= 1000
* sum(strs[i].length) <= 2 * 10^4
* strs[i] 只包含小写字母。
* strs 中的所有单词都具有相同的长度，且是彼此的字母异位词。
 
备注：
字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/similar-string-groups
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

标签：深度优先搜索、并查集、图
"""

from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        length, connectCount = len(strs), 0
        disjointSet = [-1] * length
        for i in range(length):
            for j in range(i + 1, length):
                r1, r2 = self._getRoot(disjointSet, i), self._getRoot(disjointSet, j)
                if r1 != r2 and self._isSimilar(strs[i], strs[j]):
                    disjointSet[r2] = r1
                    connectCount += 1
        return length - connectCount

    def _getRoot(self, disjointSet: List[int], idx: int) -> int:
        """ 获取并查集中的根节点 """
        visiteds = []
        while disjointSet[idx] >= 0:
            visiteds.append(idx)
            idx = disjointSet[idx]
        for visited in visiteds:
            disjointSet[visited] = idx
        return idx

    def _isSimilar(self, s1: str, s2: str) -> bool:
        """ 判断两个字符串是否相似 """
        diffCount = 0
        for c1, c2 in zip(s1, s2):
            diffCount += (c1 != c2)
            if diffCount > 2:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.numSimilarGroups(["tars", "rats", "arts", "star"])
    print(r)
    r = s.numSimilarGroups(["omv", "ovm"])
    print(r)
