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
