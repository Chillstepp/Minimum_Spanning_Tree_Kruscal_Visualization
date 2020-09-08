# README

## 项目介绍：


​        大作业选择的是**《最小生成树的可视化形成》**这一选题，代码主体基于**Python**。

​        其中利用了**Tkinter库作为可视化界面的制作**，这是一款Tkinter 是 Python 的标准 GUI 库。Python 使用 Tkinter 可以快速的创建 GUI 应用程序。由于 Tkinter 是内置到 python 的安装包中、只要安装好 Python 之后就能 import Tkinter 库、而且 IDLE 也是用 Tkinter 编写而成、对于简单的图形界面 Tkinter 还是能应付自如。

​        在深度学习的一个视频中偶然看到Networkx这个库，它内置了常用的图与复杂网络分析算法，可以方便的进行复杂网络数据分析、仿真建模等工作。对于本次实验图的可视化这部分，Networkx+Matplotlib是一个很好的选择，操作方便而且功能多样。因此我选用了**Networkx+Matplotlib作为图的可视化呈现。**

## 提交内容说明

**X01814031_王浩宇\_最小生成树(基于kruscal算法+python实现).docx**    为我的实验报告

**最小生成树.exe** 为我的执行文件，文件大小100M，这么大的原因是因为我使用了pyinstaller作为打包exe的工具，它的好处是可以把python环境和库放进去一起打包，因此不会受电脑环境的问题而无法执行，缺点就是存储占用有些大。

**Kruscal_Visualization.py**  为我的Python代码。

## 运行方法：

#### 1.首先打开  **最小生成树.exe**  

[![tyEWNQ.png](https://s1.ax1x.com/2020/06/06/tyEWNQ.png)](https://imgchr.com/i/tyEWNQ)

然后打开后会出现这个画面

![tyEfhj.png](https://s1.ax1x.com/2020/06/06/tyEfhj.png)

#### 2.等待一会出现如下界面

![tyEON4.png](https://s1.ax1x.com/2020/06/06/tyEON4.png)

这个就是我的应用界面了，然后有两个输入框，第一个输入框**Please input the number of nodes是输入一个整数，代表有多少个点**。第二个框**Please input the Adjacency Matrix是输入邻接矩阵**，该矩阵大小为n*n，请在每行用空格隔开输入的数字(0代表没有路径)。

**例如：**

![tyVKDf.png](https://s1.ax1x.com/2020/06/06/tyVKDf.png)

#### 3.然后点击Run即可运行

![tyV35Q.png](https://s1.ax1x.com/2020/06/06/tyV35Q.png)

其中**左边**的图代表输入**邻接矩阵所形成的图**，**右边**是生成的**最小生成树的图**




# 谢谢阅读
