---
title: 7015 assignment
date: 2025-12-15 19:35:45
tags: []
---

## Introduction
Traditional image-only models can classify
abnormalities but cannot understand clinical questions or provide interactive responses.
To address this, recent AI systems combine vision and language to perform Medical Visual Question Answering (Med-VQA), where a model answers natural-language questions
based on a medical image (e.g., “Is there pneumonia?”, “What organ is shown?”, “Is there
a mass?”).

## dataset choice
We choose the most popular dataset for Med-VQA, which is SLACK.

### Analysis of SLACK Dataset

## Steps
### Data Preparation
1. Import data
    ```python
    from datasets import load_dataset
    dataset = load_dataset("slack")
    ```
    运行之前要安装datasets库
    ```python
    pip install datasets
    ```
    这段代码在选择的数据集里面可以复制到（
    查看数据集的基本信息
    ```python
    print(dataset)
    ```

2. 答案词汇表构建和编码
    从数据集的训练集和验证集中提取所有可能的答案词汇，并构建一个词汇表。
    每个答案词汇都被映射到一个唯一的整数索引。
    为什么需要这样？
    因为模型需要将答案词汇转换为向量表示，而整数索引可以方便地进行这种转换。


### conda 新环境
``` conda create -p D:\important\Conda_Envs\cv7006 python=3.10 ```

### 激活jupyer notebook
pip install notebook ipykernel
python -m ipykernel install --user --name mp --display-name "Python (mp)"


