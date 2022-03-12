"""
扫地机器人

房间（用格栅表示）中有一个扫地机器人。格栅中的每一个格子有空和障碍物两种可能。
扫地机器人提供4个API，可以向前进，向左转或者向右转。每次转弯90度。
当扫地机器人试图进入障碍物格子时，它的碰撞传感器会探测出障碍物，使它停留在原地。
请利用提供的4个API编写让机器人清理整个房间的算法。

interface Robot {
  // 若下一个方格为空，则返回true，并移动至该方格
  // 若下一个方格为障碍物，则返回false，并停留在原地
  boolean move();

  // 在调用turnLeft/turnRight后机器人会停留在原位置
  // 每次转弯90度
  void turnLeft();
  void turnRight();

  // 清理所在方格
  void clean();
}

示例:
输入:
room = [
  [1,1,1,1,1,0,1,1],
  [1,1,1,1,1,0,1,1],
  [1,0,1,1,1,1,1,1],
  [0,0,0,1,0,0,0,0],
  [1,1,1,1,1,1,1,1]
],
row = 1,
col = 3

解析:
房间格栅用0或1填充。0表示障碍物，1表示可以通过。
机器人从row=1，col=3的初始位置出发。在左上角的一行以下，三列以右。

注意:
1. 输入只用于初始化房间和机器人的位置。你需要“盲解”这个问题。
换而言之，你必须在对房间和机器人位置一无所知的情况下，只使用4个给出的API解决问题。
2. 扫地机器人的初始位置一定是空地。
3. 扫地机器人的初始方向向上。
4. 所有可抵达的格子都是相连的，亦即所有标记为1的格子机器人都可以抵达。
5. 可以假定格栅的四周都被墙包围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/robot-room-cleaner
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Robot:

    def __init__(self, room, x, y):
        self._room = room
        self._height, self._width = len(room), len(room[0])
        self._x, self._y = x, y  # 当前行|列
        self._dir = 1  # 0:向右; 1:向上; 2:向左; 3:向下

    def move(self):
        if self._dir == 0:
            if self._y + 1 >= self._width or self._room[self._x][self._y + 1] == 0:
                return False
            self._y += 1
        elif self._dir == 1:
            if self._x - 1 < 0 or self._room[self._x - 1][self._y] == 0:
                return False
            self._x -= 1
        elif self._dir == 2:
            if self._y - 1 < 0 or self._room[self._x][self._y - 1] == 0:
                return False
            self._y -= 1
        else:
            if self._x + 1 >= self._height or self._room[self._x + 1][self._y] == 0:
                return False
            self._x += 1
        return True

    def turnLeft(self):
        self._dir = (self._dir + 1) % 4

    def turnRight(self):
        self._dir = (self._dir - 1) % 4

    def clean(self):
        print(f'clean {self._x}, {self._y}')


class Solution:
    def cleanRoom(self, robot: Robot):
        # 回溯法：从起点开始，每个点往四个方向尝试前进并清扫
        curDir = 1  # 0:向右; 1:向上; 2:向左; 3:向下
        cleanedPosSet = set()  # 已经清扫过的坐标

        def turnTo(toDir: int):
            """ 转向 """
            nonlocal curDir
            if curDir != toDir:
                if curDir - 1 == toDir or (curDir == 0 and toDir == 3):
                    robot.turnRight()
                elif curDir + 1 == toDir or (curDir == 3 and toDir == 0):
                    robot.turnLeft()
                else:
                    robot.turnRight()
                    robot.turnRight()
            curDir = toDir

        def explore(x: int, y: int):
            """ 探索一个位置 """
            robot.clean()
            cleanedPosSet.add((x, y))
            turnTo(0)
            if (x, y + 1) not in cleanedPosSet and robot.move():
                explore(x, y + 1)
                turnTo(2)
                robot.move()
            turnTo(1)
            if (x - 1, y) not in cleanedPosSet and robot.move():
                explore(x - 1, y)
                turnTo(3)
                robot.move()
            turnTo(2)
            if (x, y - 1) not in cleanedPosSet and robot.move():
                explore(x, y - 1)
                turnTo(0)
                robot.move()
            turnTo(3)
            if (x + 1, y) not in cleanedPosSet and robot.move():
                explore(x + 1, y)
                turnTo(1)
                robot.move()

        explore(0, 0)  # 以零点为起点开始探索


if __name__ == '__main__':
    room = [
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]
    robot = Robot(room, 0, 2)
    s = Solution()
    s.cleanRoom(robot)
