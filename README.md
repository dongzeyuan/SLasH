# SLasH

## 打算做个文字挂机版的暗黑2
把暗黑2的一些耐玩的部分（其实就是刷装备啦）放到文字挂机版里
暂时还没想好到底该怎么做。

## 暗黑2我玩的东西
* 职业

最开始做的简单点，`idle adventure`那个游戏的职业做的挺有意思

* 技能树
* 装备物品（宝石，符文，底材）

如果做成文字类的，一些比较牛逼的符文之语可能没法展现出来了，比如`谜团`用文字怎么展现？画面效果没有啊。

* 任务（包括一些特殊任务，隐藏任务）
* 不同的地图场景
* 背景音乐

## 这个界面怎么展现呢？

是用纯命令行还是什么，我想用PYQT5做个游戏界面出来。

## 这个游戏不能是一个无聊的数值游戏
## 尽量避免出现唯一最优搭配的情况

## 最简战斗场景

玩家移动到某个地图，开始挂机，显示战斗日志
怪物有技能，玩家也有技能

## 琢磨琢磨IDLE这个游戏吧

## 一个典型的战斗流程是怎么样呢？
1. 进入某张地图
    1. 进入某张地图可以由玩家下达指令
        * 比如奇迹那个网游，打指令/move xxx 然后就移动到了xxx地图
        * 或者做成点选的，将地图列表呈现出来，然后玩家点击移动
        * 前期建议用命令方式
    2. 判断玩家是否进入某张地图可以用个状态参数来表示，该参数可以接收地图的ID
    3. 玩家进入地图后，根据玩家等级生成相应怪物
        1. 需要一个地图包含多少种怪物的列表
        2. 根据列表和玩家等级选择生成何种怪物
        3. 生成怪物实例
    4. 某张地图自身可能有一些特殊的参数，例如掉落等级（类似暗黑2）
    5. 上面的2和4其实可以弄成一个参数字典，这个字典里存贮地图的ID，掉落等级，最高的怪物等级等等地图信息。
2. 遇到怪物，进入战斗状态
    1. 玩家进入某张地图后间隔一段时间（毫秒级别）遇到怪物
    2. 玩家遇到怪物用某个状态参数来表示，进入地图一定时间后，该参数自动变成True
3. 攻击怪物
    1. 根据玩家的技能搭配和攻击速度进行攻击
    2. 怪物自身也有相应的技能和攻击速度，这些技能和攻击速度可以存储在一张大的技能表中，技能表中有技能等级，技能等级下最高的怪物等级
    3. 前期可以考虑玩家技能搭配最高5主动，3被动，怪物最高3主动，1被动。
4. 计算血量
    1. 轮询攻击，计算怪物和玩家血量，血量小于等于0的直接死亡
5. 玩家或怪物的血量<=0时战斗结束
6. 进入掉落计算，计算掉落什么装备
    1. 掉落计算这块一定得好好研究研究暗黑2的掉落池是怎么实现的。计算过程是什么。
7. 战斗结束

## 玩家属性

* 力量，智力，敏捷
* 技能槽位（5主动，3被动）
* 被动技能槽位
* 职业，进阶职业
* 种族？
* 3人或5人小队

## 项目结构上

* 开发环境和实际环境设置得区分好
* 设置项目单独存到某个文件里