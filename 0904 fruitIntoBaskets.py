"""
水果成篮

你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果种类。

你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：
* 你只有两个篮子，并且每个篮子只能装单一类型的水果。每个篮子能够装的水果总量没有限制。
* 你可以选择任意一棵树开始采摘，你必须从每棵树（包括开始采摘的树）上恰好摘一个水果 。采摘的水果应当符合篮子中的水果类型。
  每采摘一次，你将会向右移动到下一棵树，并继续采摘。
* 一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。

给你一个整数数组 fruits ，返回你可以收集的水果的最大数目。

示例 1：
输入：fruits = [1,2,1]
输出：3
解释：可以采摘全部 3 棵树。

示例 2：
输入：fruits = [0,1,2,2]
输出：3
解释：可以采摘 [1,2,2] 这三棵树。
如果从第一棵树开始采摘，则只能采摘 [0,1] 这两棵树。

示例 3：
输入：fruits = [1,2,3,2,2]
输出：4
解释：可以采摘 [2,3,2,2] 这四棵树。
如果从第一棵树开始采摘，则只能采摘 [1,2] 这两棵树。

示例 4：
输入：fruits = [3,3,3,1,2,1,1,2,3,3,4]
输出：5
解释：可以采摘 [1,2,1,1,2] 这五棵树。

提示：
* 1 <= fruits.length <= 10^5
* 0 <= fruits[i] < fruits.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fruit-into-baskets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 滑动窗口，窗口内的水果为收集的水果
        # 向右移动右指针，直至出现第三种水果，记录当前水果数，然后向右移动左指针直至减为两种水果。再循环移动右指针，左指针……
        # 取所有记录的水果数中最大的即可
        result = 0
        fruitCount = 0
        fruitNumbers = [0] * len(fruits)
        leftIdx = 0
        for rightIdx, fruit in enumerate(fruits):
            if fruitNumbers[fruit] == 0:
                if fruitCount == 2:
                    result = max(result, rightIdx - leftIdx)
                    while True:  # 移动左指针直至水果种类变为1
                        fruitNumbers[fruits[leftIdx]] -= 1
                        leftIdx += 1
                        if fruitNumbers[fruits[leftIdx - 1]] == 0:
                            break
                else:
                    fruitCount += 1
            fruitNumbers[fruit] += 1
        return max(result, len(fruits) - leftIdx)


if __name__ == '__main__':
    s = Solution()

    r = s.totalFruit([1, 2, 1])
    print(r)

    r = s.totalFruit([0, 1, 2, 2])
    print(r)

    r = s.totalFruit([1, 2, 3, 2, 2])
    print(r)

    r = s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4])
    print(r)
