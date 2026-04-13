---
title: pyTorch
date: 2026-02-19 20:22:48
tags:
---

1. 把数组转换为 torch 张量
torch.as_tensor()

2. 求解线性方程组
torch.linalg.solve()
- 功能：求解线性方程组 $Ax = b$，其中 $A$ 是一个方阵，$x$ 和 $b$ 是向量或矩阵。
- 参数：
    - `A`：系数矩阵，形状为 `(n, n)`。
    - `b`：右侧向量或矩阵，形状为 `(n,)` 或 `(n, m)`。
- 返回值：
    - `x`：解向量或矩阵，形状与 `b` 相同。

3. 矩阵转置
torch.Tensor.T
X.T
必须大写

4. 矩阵拉平
torch.Tensor.flatten()
X.flatten()

5. 取整
torch.round(x, decimals=4)

### Standardization 和 Min-Max Normalization

1. 目的是什么
- `standardization`（标准化）是把数据变成均值为 0、标准差为 1 的分布。
- 它的目的是消除不同特征量纲和数值范围的影响，让模型更容易训练。
- `min-max normalization`（归一化）是把数据缩放到固定区间，最常见是 `[0, 1]`。
- 它的目的是让不同特征落在统一范围内，便于比较，也适合对输入范围敏感的模型。

2. 公式是什么
- `standardization`:
  `z = (x - mean) / std`
- `min-max normalization`:
  `x_norm = (x - x_min) / (x_max - x_min)`

3. PyTorch 用到的几个方法是什么
- `torch.mean(x, dim=0)`：按列求均值
- `torch.std(x, dim=0, unbiased=False)`：按列求标准差
- `torch.min(x, dim=0).values`：按列求最小值
- `torch.max(x, dim=0).values`：按列求最大值
- `torch.round(x, decimals=4)`：保留 4 位小数

4. 这两个的 PyTorch 表示
- `standardization`

```python
mean = torch.mean(x, dim=0)
std = torch.std(x, dim=0, unbiased=False)
standardized = torch.round((x - mean) / std, decimals=4)
```

- `min-max normalization`

```python
x_min = torch.min(x, dim=0).values
x_max = torch.max(x, dim=0).values
normalized = torch.round((x - x_min) / (x_max - x_min), decimals=4)
```

### sigmoid计算

1. 注意返回类型
- `torch.sigmoid()` 的结果还是 `tensor`。
- 如果题目要求返回 `Python float`，要把标量 tensor 转成普通浮点数。
- 常用写法：

```python
torch.sigmoid(z_t).item()
```

- 如果还要保留 4 位小数，可以写：

```python
round(torch.sigmoid(z_t).item(), 4)
```

2. sigmoid 的 input 一定要是 tensor
- 在 PyTorch 里，`torch.sigmoid()` 最稳妥的输入是 `tensor`。
- 如果输入只是普通数字，先转成 tensor 再算：

```python
z_t = torch.as_tensor(z)
```

3. `as_tensor` 是否要带 `dtype`
- 简单结论：不是一定要写。
- 如果是在做题或输入很简单，不写通常也可以。
- 如果是在工程里，尤其是数据输入边界，最好写清楚 `dtype=torch.float32`，这样更稳。

4. 扩展

<details>
<summary>sigmoid 的数学公式和主要用途</summary>

- 数学公式：
  `sigmoid(z) = 1 / (1 + e^(-z))`
- 输出范围：
  `(0, 1)`
- 主要用途：
  - 把任意实数压缩到 0 到 1 之间
  - 常用于二分类任务的输出层
  - 常用于把结果解释成概率

</details>

### torch方法速查

| 方法 | 作用 |
| --- | --- |
| `torch.as_tensor(x)` | 把 Python 数值、list、NumPy array 等转成 tensor |
| `torch.sigmoid(x)` | 计算 sigmoid 激活函数 |
| `tensor.item()` | 把单个标量 tensor 取成 Python 标量，比如 `float` |
| `torch.round(x, decimals=4)` | 对 tensor 做四舍五入，可以保留指定小数位 |
| `torch.mean(x, dim=0)` | 按指定维度求均值 |
| `torch.std(x, dim=0, unbiased=False)` | 按指定维度求标准差 |
| `torch.min(x, dim=0).values` | 按指定维度求最小值 |
| `torch.max(x, dim=0).values` | 按指定维度求最大值 |
| `F.softmax(x, dim=0)` | 计算 softmax，把一组分数转换成概率分布 |
| `tensor.tolist()` | 把 tensor 转成 Python 列表 |
| `torch.matmul(x, y)` | 做矩阵乘法或向量点积 |
| `torch.linalg.solve(A, B)` | 解线性方程 `A @ X = B` |

### 基底变换矩阵

1. 一句话记忆
- 从 `B` 到 `C` 的变换矩阵：
  `P = C^(-1) B`

2. 更稳的写法
- `torch.linalg.solve(c_t, b_t)` 的作用是解线性方程：
  `c_t @ P = b_t`
- 解出来的 `P` 就等价于：
  `P = C^(-1) B`
- 这个写法通常比先求逆再相乘更稳。

```python
import torch
from typing import List

def transform_basis(B: List[List[float]], C: List[List[float]]) -> List[List[float]]:
    # 把两个基底矩阵转成 tensor
    b_t = torch.as_tensor(B, dtype=torch.float32)
    c_t = torch.as_tensor(C, dtype=torch.float32)

    # 解方程 c_t @ P = b_t
    # 得到的 P 就是从 B 到 C 的变换矩阵
    # 等价于 P = C^(-1) B
    P = torch.linalg.solve(c_t, b_t)

    # 保留 4 位小数
    P = torch.round(P, decimals=4)

    # tensor -> Python nested list
    return P.tolist()
```

3. 这个变换矩阵会用在哪里
- 把同一个向量从一个坐标系/基底下的表示，转换到另一个基底下的表示
- 线性代数里的换基问题
- 3D 图形学和坐标系转换
- 机器人、计算机视觉里的坐标变换
- 机器学习里某些线性变换和表示变换问题

### 单神经元二分类模型

6. tuple 说明
- 这题返回值类型是：

```python
Tuple[List[float], float]
```

- `return probabilities, mse_value` 虽然没写括号，但返回的仍然是 `tuple`。
- 下面两种写法等价：

```python
return probabilities, mse_value
return (probabilities, mse_value)
```

7. 完整写法

```python
import torch
from typing import List, Tuple

def single_neuron_model(
    features: List[List[float]],
    labels: List[float],
    weights: List[float],
    bias: float
) -> Tuple[List[float], float]:
    # x: (样本数, 特征数)
    x = torch.as_tensor(features, dtype=torch.float32)
    # y: (样本数,)
    y = torch.as_tensor(labels, dtype=torch.float32)
    # w: (特征数,)
    w = torch.as_tensor(weights, dtype=torch.float32)
    # b: 标量
    b = torch.as_tensor(bias, dtype=torch.float32)

    # 矩阵乘法，得到每个样本的线性输出
    logits = torch.matmul(x, w) + b
    # 经过 sigmoid 得到预测概率
    probs = torch.sigmoid(logits)
    # 计算均方误差
    mse = torch.mean((probs - y) ** 2)

    # tensor -> Python list
    probabilities = [round(p, 4) for p in probs.tolist()]
    # tensor -> Python float
    mse_value = round(mse.item(), 4)

    return probabilities, mse_value
```

<details>
<summary>扩展：这题里各变量的形状</summary>

- `x` 的形状：`(样本数, 特征数)`
- `w` 的形状：`(特征数,)`
- `b` 的形状：标量
- `x @ w` 的结果形状：`(样本数,)`
- `probs` 的形状：`(样本数,)`

</details>

### softmax计算

1. softmax 的作用
- `softmax` 用来把一组原始分数（logits）转换成概率分布。
- 转换后每个值都在 `(0, 1)` 之间，并且所有值加起来等于 `1`。
- 常用于多分类任务的输出层。

2. softmax 的输入
- `softmax` 的输入通常是一组分数，所以在 PyTorch 里一般先把 `list` 或其他数据转成 `tensor`。
- 常用写法：

```python
scores_t = torch.as_tensor(scores, dtype=torch.float32)
```

3. softmax 的写法
- PyTorch 内置写法：

```python
probs = F.softmax(scores_t, dim=0)
```

- 如果输入是一维向量，`dim=0` 表示沿着这一维做 softmax。
- 最后如果题目要求返回 Python 的 `list`，要写：

```python
probs.tolist()
```

4. 返回类型
- `F.softmax()` 返回的是 `tensor`。
- 如果题目要求返回 `list[float]`，需要用 `.tolist()` 转成 Python 列表。

5. 这题的完整写法

```python
import torch
import torch.nn.functional as F

def softmax(scores: list[float]) -> list[float]:
    scores_t = torch.as_tensor(scores, dtype=torch.float32)
    probs = F.softmax(scores_t, dim=0)
    return probs.tolist()
```

<details>
<summary>softmax 的数学公式和主要用途</summary>

- 数学公式：
  `softmax(x_i) = e^(x_i) / Σ e^(x_j)`
- 输出特点：
  - 每个值都在 `(0, 1)` 之间
  - 所有输出之和等于 `1`
- 主要用途：
  - 多分类任务的输出层
  - 把一组分数转换成概率分布
  - 常用于分类模型最后一层

</details>
