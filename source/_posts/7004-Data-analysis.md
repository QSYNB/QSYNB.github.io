---
title: 7004 Data analysis
date: 2026-04-04 15:58:38
tags:
  - Data Analysis
  - Pandas
  - EDA
---

# Lab 4: Understanding your dataset

## 5. 代码流程拆解

### 5.1 读取数据

```python
import pandas as pd

df = pd.read_csv(path)
df.head()
```

作用：

- `pd.read_csv(path)`：读取 CSV
- `df.head()`：先快速看前 5 行，确认字段和数据长相

这是最常见的第一步，因为你需要先知道：

- 列名是否正确
- 数据是否成功读取
- 有没有明显脏数据

### 5.2 用 `info()` 看结构

```python
df.info()
```

这个函数非常重要，一次就能看到：

- 总行数
- 总列数
- 每列非空数量
- 每列数据类型
- 内存占用

如果只记一个 EDA 入门函数，那基本就是 `df.info()`。

### 5.3 选列

```python
x = df[['Salary']]
x = df[['Age', 'Context', 'Salary']]
```

注意这里要用双层中括号：

- `df['Salary']` 返回 `Series`
- `df[['Salary']]` 返回 `DataFrame`

这个区别很常见，也很重要。

### 5.4 按条件选行

```python
x = df[df['Salary'] == '55,000']
```

这一步是条件筛选。  
因为最开始 `Salary` 还是字符串，所以比较值也必须写成字符串。

### 5.5 先清洗再做数值比较

```python
df['Salary'] = df['Salary'].replace(',', '', regex=True)
df['Salary'] = df['Salary'].astype(int)
```

这两步分别在做：

1. 去掉逗号，把 `55,000` 变成 `55000`
2. 把字符串转换成整数

转换以后就能正常做数值筛选：

```python
x = df[df['Salary'] < 50000]
```

### 5.6 查找缺失值所在的行

```python
x = df['Context']
y = x[x.isna()]
```

思路是：

1. 先取出 `Context` 这一列
2. `x.isna()` 会返回一个布尔序列
3. 用这个布尔序列再次筛选，就能拿到缺失值对应的行

这是理解 `pandas` 布尔索引的一个很好的练习。

---

## 6. 常用函数速查

下面这一部分可以直接当考试前速查表看。

### 6.1 读取与初步查看

| 函数 / 写法 | 作用 |
| --- | --- |
| `pd.read_csv(path)` | 读取 CSV 文件 |
| `df.head()` | 查看前 5 行 |
| `df.head(2)` | 查看前 2 行 |
| `df.info()` | 查看行数、列数、非空数、类型 |
| `df.columns` | 查看全部列名 |
| `df.shape` | 查看 `(行数, 列数)` |

### 6.2 选列与选行

| 函数 / 写法 | 作用 |
| --- | --- |
| `df['Salary']` | 取单列，返回 `Series` |
| `df[['Salary']]` | 取单列，返回 `DataFrame` |
| `df[['Age', 'Salary']]` | 取多列 |
| `df[df['Salary'] == 55000]` | 按条件筛选行 |
| `df[df['Salary'] < 50000]` | 数值条件筛选 |
| `df[df['Context'].isna()]` | 取某列为空的行 |

### 6.3 缺失值处理

| 函数 / 写法 | 作用 |
| --- | --- |
| `df.isna()` | 判断整个表哪些位置是缺失值 |
| `df['Context'].isna()` | 判断某列哪些值缺失 |
| `x[x.isna()]` | 取出缺失值对应的内容 |
| `df.info()` | 快速看每列 non-null 数量 |

### 6.4 类型与字符串清洗

| 函数 / 写法 | 作用 |
| --- | --- |
| `df['Salary'].replace(',', '', regex=True)` | 去掉字符串中的逗号 |
| `df['Salary'].astype(int)` | 把列转成整数 |
| `df['Salary'].astype(float)` | 把列转成浮点数 |

### 6.5 这次 lab 最常用的模板

```python
import pandas as pd

df = pd.read_csv(path)
df.head()
df.info()

# 选列
df[['Age', 'Salary']]

# 条件筛选
df[df['Salary'] == '55,000']

# 清洗并转类型
df['Salary'] = df['Salary'].replace(',', '', regex=True)
df['Salary'] = df['Salary'].astype(int)

# 数值筛选
df[df['Salary'] < 50000]

# 找缺失值
df[df['Context'].isna()]
```

---

## 7. 这份 lab 真正想训练的能力

表面上它是在教 `pandas`，但本质上是在训练下面这些能力：

### 7.1 数据阅读能力

不是一上来就建模，而是先回答：

- 数据里有什么
- 每列是什么含义
- 哪些列能用
- 哪些列缺失严重

### 7.2 提问题的能力

数据分析不是“看到表就跑模型”，而是先定义问题。  
这个 lab 一直在强调：

- 看列名
- 看业务背景
- 看你到底想解释什么

# WQF7005 课程笔记：隐私与算法偏见

## 一、课程概述 (Agenda)

本节课主要探讨在 AI 语境下如何定义、管理并评估隐私与算法偏见，重点关注以下内容：

- 伦理隐私 (Ethical Privacy) 的定义与维度。
- 驱动因素 (Drivers) 与抑制因素 (Inhibitors)。
- IEEE 伦理基础要求 (Ethical Foundational Requirements, EFRs) 的认证标准。
- 算法偏见 (Algorithmic Bias) 的成因及其缓解措施。

---

## 二、伦理隐私 (Ethical Privacy)

### 1. 定义与核心理念

- 定义：指在 AI 系统的设计、部署和治理中，保护个人的自主权 (Personal Autonomy)、尊严 (Dignity) 和数据相关权利。
- 超越合规：它不仅是遵守法律（如 GDPR），更强调以人为本 (Human-centric) 的决策，确保数据使用不会剥削或操纵用户。

### 2. 五大维度 (Dimensions)

- 信息隐私 (Informational Privacy)：对个人数据及其披露的控制。
- 决策隐私 (Decisional Privacy)：不受 AI 推断干预个人私密决策，如医疗、生育权等。
- 位置隐私 (Locational Privacy)：对地理位置追踪的控制。
- 关联隐私 (Associational Privacy)：保持社交关系私密性的权利。
- 心理隐私 (Psychological Privacy)：保护个体免受行为预测，如情绪识别带来的操纵。

### 3. 关键利益相关者 (Key Stakeholders)

- 开发人员 (Developer, D)：构建系统并负责伦理设计。
- 集成商 (Integrator, I)：整合组件。
- 操作员 (Operator, O)：在真实环境中运行系统。
- 维护人员 (Maintainer, M)：监控并更新系统。
- 监管机构 (Regulator, R)：强制执行合规与认证。

---

## 三、隐私的驱动因素与抑制因素

### 1. 正向驱动因素 (Ethical Privacy Drivers)

- 组织治理与成熟度 (Organizational Governance & Maturity)：明确问责结构，将隐私纳入风险管理。
- 系统运行清晰度 (Clarity of AIS Operations)：确保技术和非技术用户都能追踪系统行为。
- 伦理架构与设计 (Ethical Architecture & Design)：践行隐私设计 (Privacy-by-design)，在构思阶段就嵌入伦理。
- 人类监督 (Human Oversight)：设立监督角色，并为用户提供救济途径 (Redress Pathways)。
- 最终用户赋权 (End-user Empowerment)：解释数据用途，允许用户选择加入/退出 (Opt in/out)。
- 隐私完整性维护 (Maintaining Privacy Integrity)：在系统升级过程中确保持续对齐隐私标准。
- 负责任的退役 (Responsible Decommissioning)：计划安全销毁数据和模型，进行匿名化 (Anonymize) 处理。

### 2. 负面抑制因素 (Inhibitors)

- 过度扩张与过度拟合 (Overreaching & Overfitting)：收集超出功能需求的数据，违反数据最小化 (Data Minimization) 原则。
- 威权压力 (Authoritarian Pressure)：缺乏司法监督的强制性数据共享。
- 偶然暴露 (Accidental/Incidental Exposure)：由于人为错误或配置不当导致的内部泄露。
- 恶意暴露 (Malicious Exposure)：如黑客攻击、勒索软件。
- 系统性漏洞 (Systemic Vulnerability)：架构中的设计缺陷或模型重用带来的风险。

---

## 四、算法偏见 (Algorithmic Bias)

### 1. 定义与影响

- 定义：指 AI 系统中导致不公平结果的系统性且可重复的错误 (Systematic and Repeatable Errors)。
- 成因：可能源于偏见数据、错误假设或缺乏监督。
- 后果：会强化社会不平等，导致服务被拒 (Denial of Services) 或不公平对待 (Unfair Treatment) 等现实伤害。

### 2. 偏见缓解的驱动因素

- 适当的环境对齐 (Appropriate Context Alignment)：在不同领域部署时，根据当地文化和法律进行调整。
- 受保护特征的正当使用 (Justified Use of Protected Characteristics)：明确并证明使用性别、种族等敏感属性的必要性。
- 系统行为监控 (System Behavior Monitoring)：进行全生命周期的公平性审核 (Fairness Audits)。
- 维持可接受的偏见特征 (Maintaining Acceptable Bias Profile)：培训员工识别新兴偏见。

### 3. 主要抑制因素

- 缺乏流程透明度 (Lack of Process Transparency)：如果数据源、特征选择和决策规则不透明，就无法有效缓解偏见。

---

## 五、IEEE 认证与综合总结

### 1. IEEE 认证要求 (EFR Summary)

- 基于 6 个驱动目标和 1 个主要抑制因素进行衡量。
- 评分标准：1（不达标）到 5（卓越），3 分为及格线。
- 核心要求：记录公平性评估、风险减轻计划、退役策略及透明沟通。

### 2. 隐私与偏见的相互作用 (Interplay)

- 冲突点：追求个性化以增加公平性，可能威胁数据最小化原则；为了防止偏见，有时又需要收集受隐私法保护的敏感人口统计数据。
- 解决方案：通过比例性 (Proportionality) 评估、强有力的监督以及可解释性 (Explainability) 措施来进行伦理设计。

### 7.3 发现数据问题的能力

例如：

- `Salary` 看起来像数字，其实是字符串
- 有些列缺失非常严重
- 有些列虽然存在，但不一定对问题有帮助

这些都是后续预处理前必须先发现的东西。

---

## 8. 可以直接记住的结论

### 8.1 一个数据集值不值得分析，先看三件事

1. 样本量够不够
2. 字段是否有信息量
3. 缺失值和数据类型是否会影响分析

### 8.2 `df.info()` 是 EDA 起点

如果只做一个动作来快速理解数据，优先做：

```python
df.info()
```

### 8.3 “能看起来像数字”不等于“能参与数值计算”

例如：

- `'55,000'` 是字符串
- `55000` 才是真正可比较的数值

所以实际分析前，通常要先做数据清洗和类型转换。

### 8.4 缺失值不只是“有没有”，还要看“缺失得多不多”

像 `Context` 这种缺失超过两万行的列，即使存在，也不能直接默认它可用。

---

## 9. 易错点

### 9.1 `df['col']` 和 `df[['col']]` 不一样

- 前者返回 `Series`
- 后者返回 `DataFrame`

### 9.2 字符串列不能直接当数值列比较

错误或不可靠写法：

```python
df[df['Salary'] < '55,000']
```

更合理的做法是先转类型，再比较。

### 9.3 `NaN` 不是 0

- `0` 是明确的数值
- `NaN` 是缺失值

分析时这两者意义完全不同。

---

## 10. 一句话总结

这个 lab 是一个很典型的 **数据理解 + pandas 基础操作** 练习。  
重点不是“做复杂分析”，而是学会在真正分析之前，先用 `head()`、`info()`、条件筛选、缺失值检查和类型转换，把数据看明白。

# WEEK 5
# 7004 课堂笔记：Data Preprocessing 1

## 一、这节课在做什么

这份 notebook 讲的是一个完整的数据科学流程，但这节课真正的重点放在数据预处理。

整体流程是：

1. 定义问题：能不能根据现有特征预测 `Salary`
2. 读取数据：用 `pandas.read_csv()` 导入工资调查数据
3. 数据预处理：重命名列、处理缺失值、清理异常值、统一币种
4. EDA：先看分布，再看变量关系
5. 建模：用线性回归做一个基础预测模型

一句话总结：

这节课不是在追求最强模型，而是在学“如何把原始脏数据整理成可分析、可建模的数据”。

---

## 二、课堂核心思路

### 1. 先明确目标，再决定清洗方式

课上的问题是：

`Can we predict salary based on available features in the dataset?`

所以后面的所有预处理，都是围绕这个目标服务：

- 哪些列对预测工资有帮助，就尽量保留
- 哪些列是噪音、自由文本、缺失太严重，就删掉或简化
- 哪些列原本不能直接进模型，就转换成数值或编码形式

### 2. 数据预处理不是“统一一个方法”，而是“按列处理”

这节课很强调一件事：

不同类型的列，清洗方法不同。

- 标识列：直接删
- 自由文本列：通常删
- 类别列：填众数或填 `Unknown`
- 数值列：填中位数、处理异常值
- 区间文本列：转成数值中点
- 币种列：统一汇率换算

也就是说，预处理的核心不是死记函数，而是先判断“这列是什么数据、要拿来干什么”。

---

## 三、这节课的预处理流程

### Step 1. 重命名列名

原始调查数据列名很长，不方便操作，所以先用 `df.rename(columns={...})` 统一改成简洁名字，比如：

- `How old are you?` -> `Age`
- `What industry do you work in?` -> `Industry`
- 长工资问题 -> `Salary`
- 额外补偿 -> `Compensation`

这样做的目的：

- 代码更清楚
- 后面选列更方便
- 减少输入错误

### Step 2. 检查数据结构

课上先用了：

- `df.info()`
- `df.describe()`

用途：

- 看每列的数据类型
- 看有没有缺失值
- 看数值列范围是否异常

注意到 `Salary` 一开始是字符串，所以先把逗号去掉，再转整数：

```python
df['Salary'] = df['Salary'].replace(',', '', regex=True)
df['Salary'] = df['Salary'].astype(int)
```

这一步说明：

有些“看起来像数字”的列，实际读进来可能是 `object`，不能直接拿去建模。

### Step 3. 删除无关列

课上删掉了这些列：

- `Timestamp`
- `Job title context`
- `Salary context`
- `Other currency`

原因：

- `Timestamp` 只是提交时间，对工资预测价值不大
- `Job title context` / `Salary context` 是自由文本，不好直接进基础模型
- `Other currency` 缺失极高，而且几乎不用

这一步对应的方法：

```python
df = df.drop([...], axis=1, errors='ignore')
```

### Step 4. 先统计缺失值，再决定怎么补

课上的关键思想不是“统一 fillna”，而是先做：

```python
df.isna().sum()
```

然后按缺失比例分类处理。

#### 4.1 缺失为 0% 的列

比如：

- `Age`
- `Salary`
- `Currency`
- `Country`
- `Overall years of experience`
- `Years of experience in current job`

这些列不用处理，保持原样。

#### 4.2 少量缺失（<1%）的类别列：用众数填补

课上对这些列用 `mode()`：

- `Industry`
- `Job title`
- `City`
- `Education level`
- `Gender`
- `Race`

代码：

```python
fill_mode_cols = ['Industry', 'Job title', 'City', 'Education level', 'Gender', 'Race']

for col in fill_mode_cols:
    df[col] = df[col].fillna(df[col].mode()[0])
```

为什么用众数：

- 都是类别变量
- 缺失比例很小
- 没必要为了少量缺失把整行删掉
- 众数通常最稳妥，也最不破坏分布

#### 4.3 缺失较多时：数值列用中位数，类别列用 `Unknown`

课上给了两个典型例子：

- `Compensation`：26.1% 缺失 -> 用中位数
- `State`：17.9% 缺失 -> 用 `Unknown`

代码：

```python
df['Compensation'] = df['Compensation'].fillna(df['Compensation'].median())
df['State'] = df['State'].fillna('Unknown')
```

为什么这样做：

- `Compensation` 是数值列，而且容易受极端值影响，所以用中位数比均值更稳
- `State` 的缺失并不一定是错误，很多非美国受访者本来就没有州信息，所以不能硬填众数，单独设成 `Unknown` 更合理

### Step 5. 把区间型文本转成数值

#### 5.1 Age 列

`Age` 原本是这种形式：

- `18-24`
- `25-34`
- `35-44`

课上的思想是：

如果目标是建模，可以把年龄段转成中点值，例如：

- `18-24` -> `21`
- `25-34` -> `29.5`
- `35-44` -> `39.5`

这样做的好处：

- 模型更容易学习年龄与工资的趋势关系
- 可以做相关分析
- 方便后续回归或树模型

但老师也提醒：

如果只是做描述分析，年龄段也可以先保留为类别。

#### 5.2 工作经验列

两列经验数据也都是区间：

- `Overall years of experience`
- `Years of experience in current job`

例如：

- `1 year or less` -> `0.5`
- `2 - 4 years` -> `3`
- `5 - 7 years` -> `6`
- `8 - 10 years` -> `9`
- `11 - 20 years` -> `15.5`

在 notebook 最后的建模部分，实际用了两个函数：

```python
def convert_age_to_midpoint(age_range):
    ...

def convert_experience_to_midpoint(exp_range):
    ...
```

然后：

```python
df['Age'] = df['Age'].apply(convert_age_to_midpoint)
df['Overall years of experience'] = df['Overall years of experience'].apply(convert_experience_to_midpoint)
df['Years of experience in current job'] = df['Years of experience in current job'].apply(convert_experience_to_midpoint)
```

这一块是考试和作业里很常见的思路：

“把有顺序的类别区间，映射成有意义的数值”。

### Step 6. 处理不合理数值和异常值

#### 6.1 负数处理

工资和补偿不应该是负值，所以先检查：

```python
df[(df['Salary'] < 0) | (df['Compensation'] < 0)]
```

然后用 `clip(lower=0)` 把负值截断到 0：

```python
df['Salary'] = df['Salary'].clip(lower=0)
df['Compensation'] = df['Compensation'].clip(lower=0)
```

#### 6.2 0 值处理

课上的判断非常重要：

- `Salary = 0` 通常不合理 -> 视为缺失更合适
- `Compensation = 0` 是合理的 -> 因为很多工作确实没有奖金/加班费

所以只处理工资列：

```python
df['Salary'] = df['Salary'].replace(0, np.nan)
```

#### 6.3 用 IQR 做异常值截尾

老师没有直接删掉极端高工资，而是选择 capping（截尾）。

做法：

1. 计算第一四分位数 `Q1`
2. 计算第三四分位数 `Q3`
3. 计算 `IQR = Q3 - Q1`
4. 上界设为 `Q3 + 1.5 * IQR`
5. 超过上界的值替换成上界

代码：

```python
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + 1.5 * IQR

df['Salary'] = np.where(df['Salary'] > upper_limit, upper_limit, df['Salary'])
```

`Compensation` 也是同样逻辑。

为什么不用直接删：

- 有些高薪是真实存在的
- 直接删除会损失样本
- 截尾能降低极端值对均值、图形和模型的影响

### Step 7. 统一货币

原始 `Currency` 有多种币种：

- `USD`
- `EUR`
- `GBP`
- `CAD`
- `CHF`
- `ZAR`
- `SEK`
- `HKD`
- `JPY`
- `AUD/NZD`

课上先排除了 `Currency == 'Other'` 的记录，因为无法稳定换算：

```python
df = df[df['Currency'] != 'Other'].reset_index(drop=True)
```

然后用汇率字典转换成美元：

```python
df['Salary_USD'] = df['Salary'] * df['Currency'].map(conversion_rates)
df['Compensation_USD'] = df['Compensation'] * df['Currency'].map(conversion_rates)
```

最后删掉原始 `Currency` 列。

这一步的意义：

- 不同币种不能直接比较
- 不统一单位，平均值、分布图和模型都会失真

### Step 8. 高基数类别的处理思路

课上虽然没有把代码写完，但给了方向。

#### Job title 高基数问题

`Job title` 有 14000+ 个唯一值，不能直接简单 one-hot。

老师建议的思路：

- 全部转小写
- 去标点
- 提取 seniority 关键词，如 `senior`、`junior`、`lead`
- 提取大类角色，如 `data scientist`、`software engineer`

这属于“类别归一化”。

#### 类别编码思路

老师提到：

- 小基数类别 -> one-hot encoding
- 大基数类别 -> frequency encoding 或先做归类

---

## 四、EDA 和建模部分在讲什么

### 1. EDA

课上用了两个最基础的方法：

```python
df.hist(figsize=(10,6))
```

作用：

- 看数值列分布
- 判断偏态、离群值、多峰情况

```python
sns.pairplot(df)
```

作用：

- 看数值变量两两关系
- 初步观察相关性和线性趋势

### 2. 建模

最后用的是线性回归：

1. 先把 `Age` 和经验列转数值
2. `dropna()` 去掉剩余缺失
3. 设定特征 `X` 和目标 `y`
4. 把类别变量做 `get_dummies()`
5. 划分训练集/测试集
6. 训练 `LinearRegression()`
7. 用 `mean_squared_error` 评估

对应代码骨架：

```python
X = df.drop(['Salary', 'USERID'], axis=1)
y = df['Salary']

categorical_cols = X.select_dtypes(include='object').columns
X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)
mse = mean_squared_error(y_test, preds)
```

---

## 五、这节课最该记住的几个原则

### 原则 1：先看缺失比例，再决定填补方法

- 缺失很少 -> 可以用众数/中位数
- 缺失很多 -> 要考虑业务含义
- 不是所有缺失都代表错误

### 原则 2：数值列和类别列要分开处理

- 数值列常用：中位数、均值、IQR
- 类别列常用：众数、`Unknown`、编码

### 原则 3：区间文本如果有顺序，可以转中点

像年龄段、工作年限这种数据，转成数值后更适合回归模型。

### 原则 4：异常值不一定要删，很多时候可以截尾

IQR capping 是这节课的重要方法。

### 原则 5：统一单位再分析

多币种工资必须先转成同一单位，否则比较没有意义。

### 原则 6：预处理目标要和任务一致

如果目标是机器学习，就要优先考虑：

- 能不能数值化
- 能不能编码
- 模型会不会受异常值影响

如果目标只是做描述统计，保留原始类别有时更自然。

---

## 六、方法速查

### 1. 读数据与初步查看

```python
import pandas as pd

df = pd.read_csv('xxx.csv')
df.head()
df.info()
df.describe()
```

用途：

- `read_csv()`：读取 CSV
- `head()`：看前几行
- `info()`：看类型和缺失
- `describe()`：看数值统计摘要

### 2. 改列名

```python
df = df.rename(columns={
    'old_name': 'new_name'
})
```

### 3. 删列

```python
df = df.drop(['col1', 'col2'], axis=1, errors='ignore')
```

说明：

- `axis=1` 表示删列
- `errors='ignore'` 表示列不存在时不报错

### 4. 查缺失值

```python
df.isna().sum()
```

### 5. 用众数填补类别缺失

```python
df['col'] = df['col'].fillna(df['col'].mode()[0])
```

适合：

- 类别型数据
- 缺失比例很小

### 6. 用中位数填补数值缺失

```python
df['col'] = df['col'].fillna(df['col'].median())
```

适合：

- 数值型数据
- 有偏态或异常值时比均值更稳

### 7. 把缺失当作新类别

```python
df['col'] = df['col'].fillna('Unknown')
```

适合：

- 类别列
- 缺失本身有意义

### 8. 字符串数字转整数

```python
df['Salary'] = df['Salary'].replace(',', '', regex=True)
df['Salary'] = df['Salary'].astype(int)
```

### 9. 截断负值

```python
df['col'] = df['col'].clip(lower=0)
```

### 10. 替换指定值

```python
df['Salary'] = df['Salary'].replace(0, np.nan)
```

### 11. 用 IQR 处理异常值

```python
Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1
upper = Q3 + 1.5 * IQR

df['col'] = np.where(df['col'] > upper, upper, df['col'])
```

### 12. 过滤某类数据

```python
df = df[df['Currency'] != 'Other'].reset_index(drop=True)
```

### 13. 用字典做映射转换

```python
conversion_rates = {'USD': 1, 'EUR': 1.07}
df['Salary_USD'] = df['Salary'] * df['Currency'].map(conversion_rates)
```

### 14. 用 `apply()` 做区间转中点

```python
def convert_experience_to_midpoint(x):
    if x == '2 - 4 years':
        return 3
    return x

df['Experience'] = df['Experience'].apply(convert_experience_to_midpoint)
```

### 15. 找类别列

```python
categorical_cols = X.select_dtypes(include='object').columns
```

### 16. One-hot encoding

```python
X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)
```

说明：

- 把类别变量拆成 0/1 特征
- `drop_first=True` 可以减少共线性

### 17. 切分训练集和测试集

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### 18. 训练线性回归

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
preds = model.predict(X_test)
```

### 19. 计算均方误差

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, preds)
```

### 20. 画直方图和变量关系图

```python
import matplotlib.pyplot as plt
import seaborn as sns

df.hist(figsize=(10, 6))
plt.tight_layout()
plt.show()

sns.pairplot(df)
plt.show()
```

---

## 七、复习时可以直接背的答题模板

### 如果题目问：如何处理缺失值？

可以这样答：

先用 `df.isna().sum()` 检查每列缺失情况，再按数据类型和缺失比例处理。缺失很少的类别列可用众数填补，数值列通常用中位数填补；若某类别变量的缺失本身有业务含义，则可填成 `Unknown`，而不是直接用众数。

### 如果题目问：为什么用中位数而不是均值？

可以这样答：

因为工资、奖金这类数据往往存在异常值，中位数比均值更不容易被极端值拉偏，因此填补缺失时更稳健。

### 如果题目问：为什么要把年龄段和工作年限转数值？

可以这样答：

因为线性回归等模型更适合处理数值特征。将区间类别映射为中点值后，模型更容易学习年龄或经验与工资之间的趋势关系。

### 如果题目问：为什么要统一币种？

可以这样答：

因为不同货币单位下的工资数值不能直接比较。如果不先换算到统一单位，后续统计分析、可视化和建模结果都会失真。

### 如果题目问：为什么不用直接删除异常值？

可以这样答：

因为部分高工资可能是真实样本，直接删除会损失数据。使用 IQR 截尾既能保留样本，又能减少极端值对统计结果和模型的干扰。

---

## 八、这份 notebook 里要特别注意的地方

1. `Age` 和经验列在预处理部分还是占位，真正的转换逻辑写在最后建模单元里。
2. `USERID` 在前面说明里说应删除，但最后建模前才在 `X = df.drop(['Salary', 'USERID'], axis=1)` 里排除。
3. `Job title` 高基数处理和类别编码只是讲思路，还没有完整实现。
4. 这份代码更像教学示范版，重点是理解流程，不是工业级最优清洗方案。

---

## 九、一句话收尾

这节课最重要的不是记住每一行代码，而是记住这条逻辑链：

先理解数据 -> 再按列判断问题 -> 选择合适的清洗方式 -> 统一成可分析、可建模的格式 -> 再做 EDA 和建模。
