"""
不同的二叉搜索树

给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # 此处使用动态规划，时间复杂度 = θ(n^2)
        # 也可以直接用卡塔兰数，时间复杂度 = θ(n)
        counts = [0] * (n + 1)  # [下标个值组成的二叉搜索树种数]
        counts[0], counts[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(i):
                counts[i] += counts[j] * counts[i - 1 - j]  # 左子树种数 * 右子树种数
        return counts[-1]


if __name__ == '__main__':
    s = Solution()
    r = s.numTrees(3)
    print(r)
