"""
交换字符串中的元素

给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
你可以任意多次交换在 pairs 中任意一对索引处的字符。
返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。

示例 1:
输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"

示例 2：
输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"

示例 3：
输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1], s = "bca"
交换 s[1] 和 s[2], s = "bac"
交换 s[0] 和 s[1], s = "abc"
 
提示：
* 1 <= s.length <= 10^5
* 0 <= pairs.length <= 10^5
* 0 <= pairs[i][0], pairs[i][1] < s.length
* s 中只含有小写英文字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-string-with-swaps
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 生成并查集 -> groups
        groups = [-1] * len(s)
        for pair in pairs:
            rootIdx1, rootIdx2 = self.getGroupRoot(groups, pair[0]), self.getGroupRoot(groups, pair[1])
            if rootIdx1 != rootIdx2:
                groups[rootIdx2] = rootIdx1
        # 分组 -> groupMembers
        groupMembers = {}  # {root下标: [成员下标]}
        for i in range(len(groups)):
            groupMembers.setdefault(self.getGroupRoot(groups, i), []).append(i)
        # 排序字符并填入相应的位置 -> resultChars
        resultChars = [''] * len(s)
        for group in groupMembers:
            members = groupMembers[group]
            members.sort()
            chars = sorted(s[memberIdx] for memberIdx in members)
            for memberIdx, char in zip(members, chars):
                resultChars[memberIdx] = char
        return ''.join(resultChars)

    def getGroupRoot(self, groups: List[int], idx: int) -> int:
        """ 获取idx所在群组的根节点下标 """
        idxs = []
        while groups[idx] >= 0:
            idxs.append(idx)
            idx = groups[idx]
        for i in idxs:
            groups[i] = idx
        return idx


if __name__ == '__main__':
    s = Solution()
    r = s.smallestStringWithSwaps('dcab', [[0, 3], [1, 2]])
    print(r)
    r = s.smallestStringWithSwaps('dcab', [[0, 3], [1, 2], [0, 2]])
    print(r)
    r = s.smallestStringWithSwaps('cba', [[0, 1], [1, 2]])
    print(r)
