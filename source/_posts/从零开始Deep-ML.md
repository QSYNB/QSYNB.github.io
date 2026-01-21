---
title: 从零开始Deep-ML
date: 2025-12-03 19:29:33
tags: [learning, 找工作, note]
categories: [MAI]
---

### Covariance Matrix 协方差矩阵 
- what is Covariance Matrix mathematically?
    - 协方差矩阵是一个方阵，每个元素表示两个随机变量之间的协方差。（协方差是两个特征的差距相乘之后平均）
    - 协方差矩阵的第i行第j列元素表示第i个随机变量和第j个随机变量的协方差。
    - 协方差矩阵的第i行第i列元素表示第i个随机变量的方差。（协方差矩阵是对称的）
    - 协方差大于0表示两个随机变量正相关，小于0表示负相关，等于0表示不相关。

- pytorch求协方差的函数
    - torch.cov()
        - 输入：一个二维张量，每一行表示一个随机变量，每一列表示一个样本。
        - 输出：一个二维张量，即协方差矩阵。

### Solve Linear Equations using Jacobi Method
- What is Jacobi Method?
    - 雅可比方法是一种迭代方法，用于求解线性方程组Ax=b。（求一个x，使得Ax=b）
    - 输入：一个系数矩阵A，一个常数向量b，一个初始解向量x0，一个迭代次数N。
    - 输出：一个解向量x，即方程组的解。

- pytorch实现雅可比方法（没有直接的函数，要自己实现）
    - 实现思路
        - 雅可比方法的迭代公式为：$x_{new} = D^{-1} (b - R x_{old})$
        - 其中，$D$ 是系数矩阵 $A$ 的对角矩阵，$R$ 是 $A$ 去掉对角线元素后的矩阵。
        - 每次迭代都将 $x_{new}$ 赋值给 $x_{old}$，直到收敛。
        
    
    ```python
        #get the diagonal elements of tensor 获得对角线上的元素
        D = torch.diag(A) 
        # 创建一个和A一样的矩阵，但是元素为0
        D = torch.zeros_like(A)
        # 填充对角线元素为 A 的对角线元素
        D.fill_diagonal_(A.diag())
        # 矩阵相乘
        x = torch.matmul(R, x)
        # 戒断小数位，保留4位
        x = torch.round(x * 10000) / 10000
    ```

```python
import torch

def solve_jacobi(A, b, n) -> torch.Tensor:
    """
    Solve Ax = b using the Jacobi iterative method for n iterations.
    """
    A_t = torch.as_tensor(A, dtype=torch.float) #change A to tensor
    b_t = torch.as_tensor(b, dtype=torch.float) #change b to tensor
    
    # 1. 初始化 x 为全零向量 (Standard initialization for Jacobi)
    x = torch.zeros_like(b_t)
    
    # 2. 提取对角线元素 D
    D = torch.diag(A_t)
    
    # 3. 构建剩余矩阵 R (即 A 去掉对角线元素)
    # Jacobi 公式: x_new = D^-1 * (b - (A-D)x_old)
    R = A_t.clone()
    R.fill_diagonal_(0)
    
    # 4. 迭代 n 次
    for _ in range(n):
        # 计算 (b - R * x)
        # torch.matmul(R, x) 计算的是除了对角线外的 a_ij * x_j 的和
        numerator = b_t - torch.matmul(R, x)
        
        # 除去对角线元素 D
        x_new = numerator / D
        
        # 核心要求：每一步中间结果保留 4 位小数
        # 使用 torch.round(x * 10000) / 10000 来截断小数位
        x = torch.round(x_new * 10000) / 10000
        
    return x
```
        
    