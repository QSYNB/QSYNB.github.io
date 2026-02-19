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
