---
layout: 7015
title: 7002 Final Notebook
date: 2026-01-21 14:13:22
tags:
---

# INFORMED SEARCH
## HEURISTICS FUNCTION 启发函数
- Intelligent search uses heuristics to avoid searching everywhere
-  Intelligent search does not guarantee finding a solution i.e. you could
get stuck
- Aims: to avoid exponential(指数) search & loop. (i.e. to get solutions in
more effective & efficient manner)

## Best-First Search 最佳优先搜索
- Main idea: pick the node which looks closest to the goal.
- f(n) = h(n) h(n) = estimated cost from n to goal (heuristic)
- Pick the lowest estimated cost to explore.

### Admissible Heuristic
- 当且仅当它永远不会高估 (Never Overestimates) 从当前节点到目标节点的实际最小代价。
    $$0 \leq h(n) \leq h^*(n)$$
    - $为什么 Admissible 这么重要？$
    如果 $h(n)$ 是 Admissible 的，A 算法一定能找到最优解（最短路径）。*
   
### Consistent Heuristic
- 如果一个启发函数 $h(n)$ 满足以下条件，我们称它是一致的 (Consistent) 或单调的 (Monotonicity)：
    The estimated cost to the goal from node $n$ is no greater than the step cost to a neighbor $n'$ plus the estimated cost from $n'$ to the goal.

    $$h(A) \leq cost(A, B) + h(B)$$
    - $h(A)$：从 A 直接飞到 Goal 的估计距离。
    - $cost(A, B)$：从 A 走到 B 的实际路程。
    - $h(B)$：从 B 飞到 Goal 的估计距离。 

    - 如果 $h(n)$ 是 Inconsistent (不一致) 会发生什么？ 
    - 这正是你笔记中提到的重点。如果 $h(n)$ 不一致：$f(n)$ 会下降： 在搜索过程中，你可能会发现路径上后续节点的 $f$ 值比父节点还要小。这在逻辑上很奇怪（因为你走得更远了，总代价估计反而变小了）。效率变低： A* 算法可能在第一次到达某个节点时，并没有找到到达该节点的“最短路径”。这意味着 A* 可能需要重复处理 (Re-expand) 同一个节点多次，这会大大增加计算量。修复方法： 为了保证找到最优解，如果 $h(n)$ 不一致，你必须在发现更好的路径时把已经关闭的节点重新放回“待处理列表 (Open List)”。
### 复杂度
- 时间复杂度：$O(b^d)$，其中 $b$ 是 branching factor（分支因子），$d$ 是目标节点的深度。
- 空间复杂度：$O(b^d)$，因为在最坏情况下，A* 算法需要存储所有可能的路径。

## A* Search  A*搜索
- Main idea: pick the node which looks most promising to explore
- f(n) = g(n) + h(n)
    - g(n) = cost so far to reach n
    - h(n) = estimated cost from n to goal (heuristic)
    - f(n) = estimated total cost of path through n to goal
### Properties of A* Search
- completeness: if a solution exists, A* is guaranteed to find it.
- optimality: A* always finds the optimal solution.
- time complexity: $O(b^d)$
- space complexity: $O(b^d)$

### Example Qustions
- Q1. Algorithm Comparison
Explain the fundamental difference between the evaluation functions $f(n)$ of Greedy Best-First Search and A Search*. How does this difference affect their ability to find the shortest path?

Greedy Best-First Search: F(n) = h(n) 
~~h(n) = cost of current node to the goal~~ h(n) = **estimated** cost from n to goal (heuristic)
A* search : f(n) = g(n)+h(n)
g(n) = ~~cost from the start to the current node~~ cost so far to reach n
h(n) = ~~cost from the current node to the goal~~  estimated cost from n to goal (heuristic)
f(n) = ~~total estimate cost~~ estimated total cost of path through n to goal
Greedy BFS is short-sighted (looks only at the goal)
A* is balanced (considers both the path cost and the goal distance).

- Heuristic Properties
Define what it means for a heuristic $h(n)$ to be admissible. Why is admissibility a mandatory requirement for A* Search to be optimal?
Admissible means the heuristic never overestimates the actual cost. If we overestimate, A* might skip the optimal path because it 'thinks' that path is too expensive.

- Q3. The Role of Lists
The Role of Lists In the context of A* Search, describe the purpose of the Open List and the Closed List. What happens if the algorithm encounters a node that is already in the Closed List?
The algorithm will discard/ignore the node to avoid redundant work and prevent infinite loops.

- Q4. Inconsistency Issues
Inconsistency Issues Based on your notes, what are the consequences of using an inconsistent heuristic in A* Search? How does it affect the efficiency of the "Closed List"?
The consequence is that the $f(n)$ value may decrease along a path. This forces the algorithm to re-open and re-evaluate nodes in the Closed List, which significantly reduces efficiency.

- Real-world Heuristics
Suppose you are designing a navigation app. You use Straight-Line Distance as your heuristic $h(n)$.
Is this heuristic admissible? Justify your answer.
Would Greedy Best-First Search always find the shortest driving route using this heuristic? Why or why not?

Because Greedy BFS only focuses on the distance to the goal. It might lead you into a dead end or a local optimum (like a road that goes straight toward the goal but is actually a cul-de-sac/blocked road). It doesn't care if the road it's taking is $100km$ long as long as it "looks" like it's heading toward the target.

# MACHINE LEARNING
## SUPPORT VECTOR MACHINE
Supervised Learning, classification problem
Support Vectors: the data points that are closest to the decision boundary.
Dicision boundary: the line that separate the tow classes.
Classification Margin: the distance between the decision boundary and the support vectors.
The distance between the hyperplane and the nearest data point from either class. SVM aims to maximize this margin.
最优超平面 (Optimal Hyperplane): separates data into two classes.

## The Kernel Trick
Kernels transform the input data from a low-dimensional space into a higher-dimensional space where a linear hyperplane can separate the data.
Linearly Inseparable
Kernels transform the input data from a low-dimensional space into a higher-dimensional space where a linear hyperplane can separate the data.
Common Kernels (常用核函数):
Linear Kernel
Polynomial Kernel
RBF (Radial Basis Function) / Gaussian Kernel

## how to do scaling for kernel
Reason: SVM finds the optimal hyperplane by maximizing the margin, which involves calculating Euclidean distances between points.
The Issue (问题): If one feature has a very large range (e.g., Income: $0 - 100,000$) and another has a small range (e.g., Age: $0 - 100$), the distance calculation will be dominated by the larger feature.
（如果一个特征的范围很大，而另一个很小，距离计算将被大范围特征主导，导致模型忽略小范围特征。）
Method (方法):Normalization (归一化): Scaling data into a range of $[0, 1]$.Standardization (标准化): Centering data around a mean of $0$ with a standard deviation of $1$.

. 现实世界应用 (Real-World Applications)
考试时，如果题目要求 "apply to real world"，你可以使用以下案例：

Bioinformatics / Medical Imaging (生物信息学/医学影像):

Scenario: Classifying tumors as Malignant (恶性) or Benign (良性) based on cell features.

Application: SVM uses multiple clinical features (size, texture, age) to find a boundary that separates healthy tissue from cancerous tissue.

Text Categorization (文本分类):

Scenario: Sorting news articles into categories like "Sports," "Politics," or "Tech."

Application: SVM is effective for high-dimensional data like text, where each word can be a feature

## k-NN (k-Nearest Neighbors / k-最近邻算法)
k-NN 是一种基于实例的学习 (Instance-based learning) 或 惰性学习 (Lazy learning) 算法。
Lazy Learning: 它在训练阶段不构建任何模型，只是把所有数据存起来。只有在进行预测（测试阶段）时，它才开始计算。
基本原理： "Tell me who your neighbors are, and I'll tell you who you are."（看你的邻居是谁，就知道你是谁。）

 为什么 k-NN 必须做 Scaling? (Crucial Point!)这是你笔记里 "how to do scaling for kernel" 同样适用的地方：k-NN 完全依赖于距离。如果一个特征（如收入 $0-100k$）的数值范围比另一个（如年龄 $0-80$）大得多，那么距离计算将完全被收入主导。结论： 在运行 k-NN 之前，必须进行 Normalization 或 Standardization。

 现实世界应用 (Real-world Application)
按照老师要求 "apply to real world"，可以准备这个例子：

推荐系统 (Recommender Systems):

场景： 电影推荐（类似 Netflix）。

应用： 如果用户 A 喜欢的电影类型、导演和评分习惯与用户 B、C、D 非常接近（即在特征空间中互为 Neighbors），那么系统就会把 B、C、D 看过但 A 没看过的电影推荐给 A。

# What Is AI Ethics?
AI Ethics refers to the study and application of moral values, principles, and governance mechanisms to:
• Guide design, development, deployment, and use of AI systems
• Prevent harm, unfairness, and misuse
• Ensure AI systems are trustworthy, accountable, and human-centric

## Responsible AI (RAI)

## Types of Harm Caused by Unethical AI

Ethical risk = probability that an AI system causes ethical harm

Risk Category： Bias Privacy Opacity Automation Bias Security