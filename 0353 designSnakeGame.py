"""
贪吃蛇

请你设计一个贪吃蛇游戏，该游戏将会在一个 屏幕尺寸 = 宽度 x 高度 的屏幕上运行。

起初时，蛇在左上角的 (0, 0) 位置，身体长度为 1 个单位。

你将会被给出一个数组形式的食物位置序列 food ，其中 food[i] = (ri, ci) 。
当蛇吃到食物时，身子的长度会增加 1 个单位，得分也会 +1 。

食物不会同时出现，会按列表的顺序逐一显示在屏幕上。比方讲，第一个食物被蛇吃掉后，第二个食物才会出现。
当一个食物在屏幕上出现时，保证不会出现在被蛇身体占据的格子里。

如果蛇越界（与边界相撞）或者头与移动后的身体相撞（即，身长为 4 的蛇无法与自己相撞），游戏结束。

实现 SnakeGame 类：

SnakeGame(int width, int height, int[][] food) 初始化对象，屏幕大小为 height x width ，食物位置序列为 food
int move(String direction) 返回蛇在方向 direction 上移动后的得分。如果游戏结束，返回 -1 。
 
示例 1：
  S * *  -->  * S *  -->  * * *  -->  * F *  -->  * F S  -->  * S S  -->  game over
  * * F   右  * * F   下  * S F   右  * S S   上  * * S   左  * * S   上
输入：
["SnakeGame", "move", "move", "move", "move", "move", "move"]
[[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]]
输出：
[null, 0, 0, 1, 1, 2, -1]

解释：
SnakeGame snakeGame = new SnakeGame(3, 2, [[1, 2], [0, 1]]);
snakeGame.move("R"); // 返回 0
snakeGame.move("D"); // 返回 0
snakeGame.move("R"); // 返回 1 ，蛇吃掉了第一个食物，同时第二个食物出现在 (0, 1)
snakeGame.move("U"); // 返回 1
snakeGame.move("L"); // 返回 2 ，蛇吃掉了第二个食物，没有出现更多食物
snakeGame.move("U"); // 返回 -1 ，蛇与边界相撞，游戏结束
 
提示：
* 1 <= width, height <= 10^4
* 1 <= food.length <= 50
* food[i].length == 2
* 0 <= ri < height
* 0 <= ci < width
* direction.length == 1
* direction is 'U', 'D', 'L', or 'R'.
* 最多调用 10^4 次 move 方法

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-snake-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import deque
from typing import List


class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self._width, self._height = width, height
        self._foods = food
        self._curFoodIdx = 0
        self._snake = deque()  # 蛇，蛇头下标为0
        self._snake.append([0, 0])
        self._snakeBodys = {(0, 0)}  # 被蛇占据的位置集合

    def move(self, direction: str) -> int:
        # 计算新蛇头位置 -> newHead
        curHead = self._snake[0]
        if direction == 'L':
            newHead = [curHead[0], curHead[1] - 1]
        elif direction == 'R':
            newHead = [curHead[0], curHead[1] + 1]
        elif direction == 'D':
            newHead = [curHead[0] + 1, curHead[1]]
        else:
            newHead = [curHead[0] - 1, curHead[1]]

        if self._curFoodIdx < len(self._foods) and newHead == self._foods[self._curFoodIdx]:
            # 吃到食物，更新食物数据
            self._curFoodIdx += 1
        else:
            # 检查是否出界或自交，同时更新蛇的位置
            self._snakeBodys.remove(tuple(self._snake[-1]))
            if newHead[0] < 0 or newHead[0] >= self._height or newHead[1] < 0 or newHead[1] >= self._width or\
               tuple(newHead) in self._snakeBodys:
                return -1
            self._snake.pop()
        self._snake.appendleft(newHead)
        self._snakeBodys.add(tuple(newHead))
        return self._curFoodIdx
        

if __name__ == '__main__':
    snakeGame = SnakeGame(3, 2, [[1, 2], [0, 1]])
    print(snakeGame.move('R'))
    print(snakeGame.move('D'))
    print(snakeGame.move('R'))
    print(snakeGame.move('U'))
    print(snakeGame.move('L'))
    print(snakeGame.move('U'))
