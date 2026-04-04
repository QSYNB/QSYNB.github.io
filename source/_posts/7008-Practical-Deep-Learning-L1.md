---
title: 7008 Practical Deep Learning L1
date: 2026-04-04 17:05:00
tags:
  - Deep Learning
  - Probability
  - Optimization
  - WQF7008
---

# WQF7008 Lecture 1 笔记

PDF: `D:\15_MAI\7008\WQF7008_L1.pdf`

这份 Lecture 1 的主题是：

**Applied Math for Deep Learning: Probability & Numerical Computation**

它把深度学习需要的数学基础拆成两大支柱：

1. **Chapter 3: Probability**
2. **Chapter 4: Numerical Computation / Optimization**

一句话理解这节课：

> 深度学习先用概率描述世界，再用优化算法让模型参数朝着更好的方向更新。

---

## 1. 总体框架

第二页把课程结构讲得很清楚：

### Pillar 1: The Language of Uncertainty

为什么需要：

- 现实世界是有随机性的
- 观察数据通常不完整
- 模型本身也不完美

工具箱：

- Probability Distributions
- Information Theory
- Structured Graphical Models

### Pillar 2: The Engine of Learning

为什么需要：

- 深度神经网络几乎不可能有精确解析解
- 数字计算本身有精度限制

工具箱：

- Iterative Optimization
- Gradients
- Floating-Point Stabilization
- Constraint Management

讲义自己的总结也很到位：

> Deep Learning = Uncertain Representations (Ch 3) optimized via Imperfect Digital Computation (Ch 4)

---

## 2. Random Variables 与分布基础

讲义先区分了两类随机变量：

### 2.1 离散随机变量

- 使用 **PMF**: `P(x)`
- 条件：
  - 定义域是所有可能取值
  - `0 <= P(x) <= 1`
  - `sum P(x) = 1`

例子：

- 均匀离散分布：`P(x = x_i) = 1 / k`

### 2.2 连续随机变量

- 使用 **PDF**: `p(x)`
- 条件：
  - `p(x) >= 0`
  - `integral p(x) dx = 1`
- 注意：
  - 连续型里的 `p(x)` 可以大于 1
  - 真正有概率意义的是区间积分，不是单点值本身

例子：

- 均匀连续分布：`u(x; a, b) = 1 / (b - a)`

### 2.3 记号

讲义中随机变量写作：

- 标量：`x`
- 向量：粗体 `x`
- 矩阵：大写 `X`

这在后面看梯度、协方差矩阵、Jacobian、Hessian 时很重要。

---

## 3. 概率四个基本规则

这页是考试和理解都很重要的一页。

### 3.1 Marginal Probability

核心思想：从联合分布里“边缘化”掉其他变量。

离散：

```text
P(x = x) = sum_y P(x = x, y = y)
```

连续：

```text
p(x) = integral p(x, y) dy
```

理解：

- 已知联合分布 `p(x, y)`
- 如果只关心 `x`
- 就把 `y` 所有可能都加总或积分掉

### 3.2 Conditional Probability

```text
P(y = y | x = x) = P(y = y, x = x) / P(x = x)
```

前提：

- `P(x = x) > 0`

理解：

- 在已知 `x` 已发生时，重新衡量 `y` 的概率

### 3.3 Chain Rule

```text
P(x^(1), ..., x^(n)) = P(x^(1)) * product_i P(x^(i) | x^(1), ..., x^(i-1))
```

意义：

- 联合分布可以拆成一串条件分布
- 这是 Bayesian Network 和自回归模型等方法的基础

### 3.4 Independence

绝对独立：

```text
p(x, y) = p(x)p(y)
```

条件独立：

```text
p(x, y | z) = p(x | z)p(y | z)
```

理解：

- 如果两个变量独立，就能把复杂联合分布拆简单
- 这也是图模型能简化推断的重要原因

---

## 4. 期望、方差、协方差

### 4.1 Expectation

定义：

- 函数 `f(x)` 在分布 `P` 下的平均取值

公式：

```text
E[f(x)] = sum P(x)f(x)
```

连续情况则改成积分。

最重要性质：

```text
E[af(x) + bg(x)] = aE[f(x)] + bE[g(x)]
```

也就是 **线性性**。

### 4.2 Variance

方差描述数据围绕均值的离散程度：

```text
Var(f(x)) = E[(f(x) - E[f(x)])^2]
```

补充：

- 标准差就是方差开根号
- 方差越大，分布越“宽”

### 4.3 Covariance

协方差衡量两个变量的线性关系：

```text
Cov(f(x), g(y)) = E[(f(x) - E[f(x)])(g(y) - E[g(y)])]
```

矩阵视角：

- 随机向量的 covariance matrix
- 对角线是各维的 variance
- 非对角线是维度之间的 covariance

这个思想对理解数据相关性、PCA、二阶优化都很有帮助。

---

## 5. 常见概率分布

### 5.1 Bernoulli

- 单个二元变量
- 例如 0/1、是/否

```text
P(x = 1) = phi
```

适合：

- 二分类标签
- 神经网络输出单个概率

### 5.2 Multinoulli

- 单个离散变量，有 `k` 个状态
- 分类任务里非常常见

适合：

- 多分类输出

### 5.3 Exponential

```text
p(x; lambda) = lambda * exp(-lambda x), x >= 0
```

特点：

- 右偏
- 常用于等待时间类建模

### 5.4 Laplace

```text
Laplace(x; mu, gamma) = 1/(2gamma) * exp(-|x-mu|/gamma)
```

特点：

- 中心更尖
- 尾部比高斯更重

### 5.5 Dirac Delta

- 所有概率质量集中在一个点

```text
p(x) = delta(x - mu)
```

理解：

- 极端确定性
- 常用来做理论表达

### 5.6 Empirical Distribution

```text
p_data(x) = (1/m) * sum delta(x - x^(i))
```

理解：

- 经验分布就是“数据样本本身”
- 机器学习里，我们很多时候并不知道真实分布，只能看到经验分布

### 5.7 Mixture Model

- 用多个分布组合成更复杂的分布
- 例子：Gaussian Mixture Model

意义：

- 真实数据往往不是单峰分布
- mixture 可以更灵活地拟合多簇结构

---

## 6. Gaussian 与常见概率变换

### 6.1 Gaussian Distribution

高斯分布公式：

```text
N(x; mu, sigma^2) = 1 / sqrt(2pi sigma^2) * exp(-(x - mu)^2 / (2sigma^2))
```

讲义强调它为什么是默认选择：

1. **Central Limit Theorem**
2. **Maximum Entropy**

也就是：

- 很多独立随机变量的和会近似高斯
- 在给定方差下，高斯分布最“不带偏见”

### 6.2 Precision

讲义提到一个替代表达：

```text
beta = sigma^(-2)
```

即 precision 是 variance 的倒数，计算上有时更方便。

### 6.3 Probability Transfer Functions

#### Logistic Sigmoid

```text
sigma(x) = 1 / (1 + exp(-x))
```

作用：

- 把任意实数压到 `(0, 1)`
- 常用于 Bernoulli 参数输出

#### Softplus

```text
zeta(x) = log(1 + exp(x))
```

作用：

- 是 ReLU 的平滑版本
- 输出范围 `(0, infinity)`
- 可用于约束某些参数必须为正，例如 Gaussian 的 `beta` 或 `sigma`

---

## 7. 信息论到损失函数

这部分非常关键，因为它直接把“概率”连到了“深度学习训练目标”。

### 7.1 Self-Information

```text
I(x) = -log P(x)
```

理解：

- 事件越常见，信息量越低
- 事件越罕见，信息量越高

### 7.2 Shannon Entropy

```text
H(x) = E[I(x)] = -E[log P(x)]
```

理解：

- 衡量整个分布平均不确定性

### 7.3 KL Divergence

```text
D_KL(P || Q) = E_{x~P}[log P(x) - log Q(x)]
```

意义：

- 衡量模型分布 `Q` 与真实分布 `P` 的差距
- 不是对称的

### 7.4 Cross-Entropy

```text
H(P, Q) = H(P) + D_KL(P || Q) = -E_{x~P}[log Q(x)]
```

关键结论：

> 最小化 cross-entropy，等价于最小化 KL divergence。

这就是为什么分类任务里常用 cross-entropy loss。

---

## 8. Structured Probabilistic Models

### 8.1 Directed Models: Bayesian Networks

结构：

- 有向无环图 DAG

联合分布分解：

```text
p(x) = product_i p(x_i | Pa_G(x_i))
```

其中 `Pa_G(x_i)` 是图中该节点的父节点。

### 8.2 Undirected Models: Markov Random Fields

特点：

- 无向图
- 用 clique 上的 potential function 建模

形式：

```text
p(x) = (1 / Z) * product_C phi(C)
```

### 8.3 Partition Function

```text
Z = integral p_tilde(x) dx
```

作用：

- 归一化常数
- 确保总概率为 1

讲义提醒：

- 在很多深度学习模型里，`Z` 的计算可能非常困难

---

## 9. 数值计算：硬件限制

这一页是在告诉我们：

> 公式是连续数学，计算机是有限精度机器。

### 9.1 Underflow

- 非常接近 0 的数被舍入成 0

后果：

- 除法可能坏掉
- `log(0)` 会变成 `-infinity`

### 9.2 Overflow

- 非常大的数近似成 `infinity`

后果：

- 算术运算可能得到 `NaN`

### 9.3 Poor Conditioning

- 输入变化很小，输出变化却很大
- 与 condition number 有关

这在深度学习优化里会影响稳定性和收敛。

### 9.4 Softmax 的稳定实现

普通 softmax：

```text
softmax(x)_i = exp(x_i) / sum_j exp(x_j)
```

稳定版做法：

```text
z = x - max_i x_i
```

然后再算 softmax。

为什么有效：

- 最大项变成 0，避免分子爆炸
- 至少有一项是 `exp(0)=1`，减少分母下溢风险

这是一条非常实用的实现细节。

---

## 10. 梯度优化基础

### 10.1 Objective 与 Derivative

目标：

- 最小化代价函数 `f(x)`

导数：

- `f'(x)` 给出斜率
- 往反方向移动可以减小函数值

### 10.2 Gradient Descent

多维情况使用梯度：

```text
x' = x - epsilon * grad f(x)
```

其中：

- `epsilon` 是 learning rate / step size

### 10.3 Jacobian

讲义定义：

- Jacobian 是一个向量值函数的所有一阶偏导数组成的矩阵

用途：

- 多输出函数微分
- 神经网络反向传播里非常常见

### 10.4 Lipschitz Continuity

讲义给出：

```text
|f(x) - f(y)| <= L ||x - y||_2
```

意义：

- 梯度不能变化得无限快
- 是分析优化稳定性的重要假设

---

## 11. 二阶优化

### 11.1 Hessian

- Hessian 是二阶导数组成的矩阵
- 它描述曲率

### 11.2 Newton's Method

```text
x* = x^(0) - H(f(x^(0)))^(-1) grad f(x^(0))
```

理解：

- 利用二阶信息，直接朝二次近似的极值点跳

### 11.3 Local Min / Local Max / Saddle Point

讲义强调三种局部结构：

- Local minimum: `f''(x) > 0`
- Local maximum: `f''(x) < 0`
- Saddle point: 曲率混合

### 11.4 为什么 Newton 方法在深度学习里不理想

讲义给出的核心原因：

- 神经网络里 saddle point 非常多
- 梯度为 0 不代表真的是最小值
- Newton 方法可能被二阶信息“带进”鞍点
- Gradient descent 反而更容易滚过去

这是一个很重要的直觉点。

---

## 12. 约束优化与 KKT 条件

目标：

- 在可行域 `S` 内找 `f(x)` 的最优值

### 12.1 Generalized Lagrangian

```text
L(x, lambda, alpha) = f(x) + sum lambda_i g^(i)(x) + sum alpha_j h^(j)(x)
```

作用：

- 把约束问题变成统一处理的拉格朗日形式

### 12.2 KKT 条件

最优点通常要满足：

1. 拉格朗日函数梯度为 0
2. 所有约束满足
3. Complementary slackness:

```text
alpha ⊙ h(x) = 0
```

含义：

- 活跃的不等式约束会对应正的乘子
- 不活跃的约束乘子可以为 0

---

## 13. 应用例子：Linear Least Squares

目标函数：

```text
f(x) = 1/2 ||Ax - b||_2^2
```

### 13.1 无约束解法

梯度：

```text
grad f(x) = A^T(Ax - b)
```

令梯度为 0：

```text
A^T A x - A^T b = 0
```

得到 normal equation：

```text
x = (A^T A)^(-1) A^T b
```

### 13.2 加约束的版本

如果加入 `L2` 范数约束：

```text
x^T x <= 1
```

就可以写成拉格朗日形式并求解。

讲义 takeaway：

- regularized least squares 本质上就是 constrained optimization

这也是理解 ridge regression 的一个很好的入口。

---

## 14. 整节课怎么连到深度学习训练

最后一页给了一个非常适合背诵的闭环：

### 1. Define the World

- 用概率分布表示模型预测
- 典型输出层：`sigmoid` / `softmax`

### 2. Measure the Error

- 用 `cross-entropy` / `KL divergence`
- 比较模型分布和真实数据分布

### 3. Calculate the Path

- 计算梯度
- 同时处理数值稳定性问题，比如 underflow/overflow

### 4. Update the System

- 用 gradient descent 更新参数

一句话总结：

> Probability 决定“模型在表达什么”，Optimization 决定“模型如何学会它”。

---

## 15. 适合复习时直接记住的重点

### 概率部分

- 离散变量用 PMF，连续变量用 PDF
- 边缘概率 = 对联合分布求和或积分
- 条件概率 = 联合概率 / 条件事件概率
- 链式法则能把联合分布拆成条件分布乘积
- 独立性会大幅简化概率表达

### 统计量部分

- Expectation 是平均
- Variance 是离散程度
- Covariance 是线性关系
- 协方差矩阵对角线是方差

### 分布与信息论

- Gaussian 是默认重要分布
- Sigmoid 输出概率
- Softplus 保证输出为正
- Self-information, entropy, KL, cross-entropy 是一条链
- 最小化 cross-entropy 等价于最小化 KL

### 数值与优化

- Underflow 会把小数压成 0
- Overflow 会把大数变成 infinity
- softmax 要减去最大值做稳定化
- Gradient descent 是一阶优化核心
- Hessian 描述曲率
- Newton 方法在深度网络里容易受 saddle point 影响
- KKT 条件是约束优化基础

---

## 16. 速查公式

```text
P(y|x) = P(x,y) / P(x)
```

```text
p(x) = integral p(x,y) dy
```

```text
E[f(x)] = sum P(x)f(x)
```

```text
Var(f(x)) = E[(f(x) - E[f(x)])^2]
```

```text
Cov(f(x), g(y)) = E[(f(x) - E[f(x)])(g(y) - E[g(y)])]
```

```text
sigma(x) = 1 / (1 + exp(-x))
```

```text
softplus(x) = log(1 + exp(x))
```

```text
D_KL(P || Q) = E_{x~P}[log P(x) - log Q(x)]
```

```text
H(P, Q) = -E_{x~P}[log Q(x)]
```

```text
softmax(x)_i = exp(x_i) / sum_j exp(x_j)
```

```text
x' = x - epsilon * grad f(x)
```

```text
x = (A^T A)^(-1) A^T b
```

---

## 17. 一句话总复盘

这节课的核心不是单独记很多公式，而是理解一个完整链条：

**用概率描述不确定性，用信息论定义损失，用数值稳定技巧保证可算，用梯度优化让模型真正学会。**
