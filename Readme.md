# Readme

随着开学季的到来，小组人数迎来了快速上升阶段。因此，我需要一款工具来帮助我检测小组人数的变化。

### 使用说明：

main.py 是主程序，需要在此处设置网址链接、用户名、密码，以及储存数据的地址。运行后会立即获取一次数据。

loop.py 是用来定时执行main程序的。

dataclean.py 是用来做数据清洗的，可以忽略；其它程序是做了模块化的package，需要和main放在同一个文件夹下。



## 更新日志

### 2022-09-05

新增：

1. 支持至多保存四个数据（data3和data4为可选参数）
2. 计算并保存话题数的增量
3. 计算并保存小组人数的增量


优化：

1. 保存的时间不显示秒，只精确到分钟
3. groupdata 返回值为 int 型，并去除无关文字
4. 数据保存地址统一作为变量设置


### 2022-09-01

新增：

1. 单篇话题的阅读量的跟踪
2. 计算并保存阅读量的增量

优化：

1. 数据保存地址移至在 main() 中修改



### 2022-08-30

程序运行起来了。每天的固定时间会自动爬取数据（人数、话题数），写入到 csv 文件中。

更新计划：

- [ ] 用 ticker 做一个窗口界面，可以有按钮点击“立即获取数据”
- [ ] 用 matplotilb 绘制折线图
- [x] 更多维度数据的获取（阅读量等）

