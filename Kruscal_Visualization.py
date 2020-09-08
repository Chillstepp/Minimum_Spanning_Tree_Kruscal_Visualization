import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk

# 调用三个库：Networkx用于连接顶点形成图
# matplotlib用于配合Networkx显示图象
# Tkinter用于制作可视化输入台/控制台。

N = 10005
Father = [0] + [n+1 for n in range(N)]
R = [0] * (N+1)
_ = 1 << 10
graph = []
n = 0
#定义图的相关定义。
#text_content = []#用来储存每一行内容的列表



# 定义并查集中的find
# 用于kruscal算法中的搜索是否已加入最小生成树，防止成环。

def find(x):  # 并查集的find
    global Father
    if x == Father[x]:
        return x
    Father[x] = find(Father[x])
    return Father[x]



# 定义并查集中的合并，将顶点加入生成树
# 这里的Union还做了平衡处理，加快查找的速度。
def union(x, y):  # 并查集的union
    global Father, R
    x = find(x)
    y = find(y)
    if R[x] > R[y]:
        R[y], R[x] = R[x], R[y]
    Father[x] = y
    if R[x] == R[y]:
        R[y] += 1


# kruscal算法，用作寻找最小生成树，返回一个集合Set，该集合即为最小生成树的边集。
def kruskal(G, num):
    E = []
    for u in range(num):
        for v in range(num):
            if u != v:
                E.append((G[u][v], u+1, v+1))
    T = set()
    T.clear()
    for _, u, v in sorted(E):
        if len(T) == num-1:
            break
        if find(u) != find(v):
            T.add((u, v))
            union(u, v)
    return T


# 用作button的command功能：
# 1.输入数据，对接收到的文本框字符进行切片，转换为二维列表，同时要注意忽略结尾的空格或者回车，利用stricp()函数即可。
# 2.对原图进行绘制：利用networkx的add_edges_from功能，并用Matplotlib来进行图像的显示。
# 3.执行kruscal算法，计算最小生成树。
# 4.对最小生成树进行绘制：利用networkx的add_edges_from功能，并用Matplotlib来进行图像的显示。


def insert_data():
    global n
    n = int(numofnodes.get())
    print(n)
    tep = data_mat.get("0.0", "end").strip()
    graph=[[int(i) for i in row.split(' ')]for row in tep.split('\n')]
    #graph.pop()  # 列表最后一个元素是空删除它
    Gbefore = nx.Graph()
    print(graph[0][0])
    for i in range(n):
        for j in range(n):
            if (graph[i][j] != 0):
                Gbefore.add_edges_from([(i + 1, j + 1)])
            else:
                graph[i][j] = _
    plt.figure(figsize=(15, 7))
    plt.subplot(1, 2, 1)
    plt.title("The input graph :")
    nx.draw(Gbefore, with_labels=True, edge_color='black', node_color='orange', node_size=1000)
    G = nx.Graph()
    G.clear()
    # 导入所有边，每条边分别用tuple表示
    # a_list = []
    G.add_edges_from(list(kruskal(graph, len(graph))))
    print(len(graph))
    plt.subplot(1, 2, 2)
    plt.title("Minimum Spanning Tree's picture after using Kruscal")
    nx.draw(G, with_labels=True, edge_color='black', node_color='orange', node_size=1000)
    plt.show()

# 创建一个窗口，
# 窗口名为：Minimum Spanning Tree(kruscal)，
# 窗口大小为：700x700
window=tk.Tk()
window.title('Minimum Spanning Tree(kruscal)')
window.geometry('700x700')

# 创建提示字模块，
# 在窗口上显示：please input the number of nodes:
# 字体大小为12，字体类型为Arial
# 字模块宽40，高2

I=tk.Label(window,
           text="please input the number of nodes:",
           font=('Arial',12),
           width=40,height=2)
I.pack()


# 创建一个文本输入框，放在提示字下方

numofnodes = tk.Entry(window)
numofnodes.pack()

# 创建提示字模块，
# 在窗口上显示：please input the Adjacency Matrix
# 字体大小为12，字体类型为Arial，
# 字模块宽40，高2

L2=tk.Label(window,
           text="please input the Adjacency Matrix",
           font=('Arial',12),
           width=40,height=2)
L2.pack()

#创建一个文本输入框，放在提示字下方
data_mat = tk.Text(window,height=10)
data_mat.pack()


# 创建一个按钮：
# 显示名字为Run
# 按钮大小为：长15，高4。
# 点击后触发 Insert_data函数的功能

b=tk.Button(window,text='Run',width=15,height=4,command=insert_data)
b.pack()

# Window.mainloop()是让窗口不关闭

window.mainloop()










