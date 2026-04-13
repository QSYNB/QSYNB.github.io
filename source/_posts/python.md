---
title: python
date: 2026-02-24 11:22:46
tags:
---

<a id="fake-bin-join"></a>
#### fake_bin（join）
```python
def fake_bin(x):
    return "".join(["0" if int(d) < 5 else "1" for d in x])
```

<a id="fake-bin-translate"></a>
#### fake_bin（translate）
```python
def fake_bin(x):
    table = str.maketrans("0123456789", "0000011111")
    return x.translate(table)
```

<a id="remove-char"></a>
#### remove_char

```python
def remove_char(s):
    return s[1:-1]
```

关键知识点：`split()`

| 写法 | 说明 |
| --- | --- |
| `string.split(separator)` | 按分隔符拆分字符串 |
| `"10:5".split(":")` | 结果是 `["10", "5"]` |

<a id="points"></a>
#### points

```python
def points(games):
    return sum(3 if g[0] > g[2] else 1 if g[0] == g[2] else 0 for g in games)
```

<a id="find-needle"></a>
#### find_needle

```python
def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'
```

<a id="get-count"></a>
#### getCount

```python
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
```

<a id="validate-pin"></a>
#### validate_pin

```python
def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and all(n in "0123456789" for n in pin)


def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
```

<a id="count-positives-sum-negatives"></a>
#### count_positives_sum_negatives

```python
def count_positives_sum_negatives(arr):
    return [sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)] if arr else []
```

<a id="filter-list"></a>
#### filter_list

```python
def filter_list(l):
    return [i for i in l if isinstance(i, int)]
```

<a id="count-by"></a>
#### count_by

```python
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]
```

<a id="is-triangle"></a>
#### is_triangle

```python
def is_triangle(a, b, c):
    return (a < b + c) and (b < a + c) and (c < a + b)
```

<a id="to-jaden-case"></a>
#### to_jaden_case

```python
def to_jaden_case(string):
    return " ".join(word.capitalize() for word in string.split())
```

<a id="count-sheeps"></a>
#### count_sheeps

```python
def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)
```

<a id="dna-to-rna"></a>
#### dna_to_rna

```python
def DNAtoRNA(dna):
    return dna.replace("T", "U")


def dna_to_rna(dna):
    return "".join("U" if i == "T" else i for i in dna)
```

<a id="longest"></a>
#### longest

```python
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
```

<a id="min-max"></a>
#### min_max

```python
def min_max(lst):
    return [min(lst), max(lst)]
```

<a id="find-next-square"></a>
#### find_next_square

```python
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1) ** 2
    return -1
```

<a id="to-alternating-case"></a>
#### to_alternating_case

```python
def to_alternating_case(string):
    return string.swapcase()
```

<a id="stray"></a>
#### stray

```python
def stray(arr):
    return min(set(arr), key=arr.count)
```

<a id="solution"></a>
#### solution

```python
def solution(s):
    s += "_"
    return [s[i:i + 2] for i in range(0, len(s) - 1, 2)]
```

<a id="pig-it"></a>
#### pig_it

```python
def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalpha() else x for x in text.split())
```

<a id="move-zeros"></a>
#### move_zeros

```python
def move_zeros(arr):
    # isinstance(x, bool) 用来单独保留 True / False
    # 因为 False == 0，所以不能只写 x != 0
    l = [x for x in arr if isinstance(x, bool) or x != 0]
    # [0] * n 表示生成 n 个 0，再拼接到末尾
    return l + [0] * (len(arr) - len(l))
```

<a id="cakes"></a>
#### cakes

```python
def cakes(recipe, available):
    # dict.get(key, 0): 取字典里 key 对应的值，如果没有这个 key，就返回 0
    # recipe.items(): 同时遍历字典里的键和值
    return min(available.get(k, 0) // v for k, v in recipe.items())
```

<a id="is-solved"></a>
#### is_solved

```python
def is_solved(board):
    lines = []

    # lines.extend(x) 会把 x 里的元素一个个加到列表末尾
    lines.extend(board)
    lines.extend([[board[0][i], board[1][i], board[2][i]] for i in range(3)])
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line == [1, 1, 1]:
            return 1
        if line == [2, 2, 2]:
            return 2

    # any(...) 里只要有一个是 True，结果就是 True
    if any(0 in row for row in board):
        return -1

    return 0
```

### 方法速查

#### 字符串常用方法

| 方法/函数 | 作用 | 例子 |
| --- | --- | --- |
| `.split(sep=None)` | 拆分字符串 | [`string.split(separator)`](#to-jaden-case) |
| `.join(iterable)` | 把可迭代对象里的字符串拼接起来 | [`"".join([...])`](#fake-bin-join) |
| `.translate(table)` | 按映射表批量替换字符 | [`x.translate(table)`](#fake-bin-translate) |
| `str.maketrans(x, y)` | 创建字符映射表 | [`str.maketrans(...)`](#fake-bin-translate) |
| `.replace(old, new)` | 替换字符串中的内容 | [`"TATA".replace("T", "U")`](#dna-to-rna) |
| `.capitalize()` | 首字母大写，其余小写 | [`word.capitalize()`](#to-jaden-case) |
| `.swapcase()` | 大小写互换 | [`string.swapcase()`](#to-alternating-case) |
| `.isdigit()` | 判断是否全是数字字符 | [`pin.isdigit()`](#validate-pin) |
| `.isalpha()` | 判断是否全是字母字符 | [`x.isalpha()`](#pig-it) |
| `.index(x)` | 返回第一次出现的位置 | [`haystack.index("needle")`](#find-needle) |

#### 列表与序列

| 方法/写法 | 作用 | 例子 |
| --- | --- | --- |
| `.count(x)` | 统计元素出现次数 | [`arrayOfSheeps.count(True)`](#count-sheeps) |
| `s[a:b:c]` | 切片，截取序列的一部分 | [`s[1:-1]`](#remove-char) |
| `range(start, stop[, step])` | 生成整数序列，左闭右开 | [`range(1, n + 1)`](#count-by) |
| `.extend(iterable)` | 把 iterable 里的元素逐个加到列表末尾 | [`lines.extend(board)`](#is-solved) |
| `.append(x)` | 在列表末尾添加一个元素 | [`lines.append([...])`](#is-solved) |
| `.get(key, default)` | 安全取字典里的值，键不存在时返回默认值 | [`available.get(k, 0)`](#cakes) |
| `.items()` | 同时遍历字典里的键和值 | [`for k, v in recipe.items()`](#cakes) |

#### 常用内置函数

| 函数 | 作用 | 例子 |
| --- | --- | --- |
| `sum(iterable)` | 求和，也常配合生成式做计数 | [`sum(1 for x in arr if x > 0)`](#count-positives-sum-negatives) |
| `any(iterable)` | 只要有一个元素为真，就返回 True | [`any(0 in row for row in board)`](#is-solved) |
| `all(iterable)` | 所有元素都为真时返回 `True` | [`all(n in "0123456789" for n in pin)`](#validate-pin) |
| `len(x)` | 返回长度 | [`len(pin)`](#validate-pin) |
| `min(x)` | 取最小值 | [`min(available.get(k, 0) // v for k, v in recipe.items())`](#cakes) |
| `min(x)` | 取最小值 | [`min(lst)`](#min-max) |
| `max(x)` | 取最大值 | [`max(lst)`](#min-max) |
| `set(x)` | 去重，得到集合 | [`set(a1 + a2)`](#longest) |
| `sorted(x)` | 排序，返回新列表 | [`sorted(set(a1 + a2))`](#longest) |
| `int(x)` | 转成整数 | [`int(d)`](#fake-bin-join) |
| `isinstance(obj, type)` | 判断对象是否属于某个类型 | [`isinstance(x, bool)`](#move-zeros) |

#### 刷题里常见写法

| 写法 | 作用 | 例子 |
| --- | --- | --- |
| 列表推导式 | 快速生成列表 | [`[i for i in l if isinstance(i, int)]`](#filter-list) |
| 条件表达式 | 一行写简单分支 | [`"0" if int(d) < 5 else "1"`](#fake-bin-join) |
| 生成式计数 | 配合 `sum()` 统计数量 | [`sum(1 for let in inputStr if let in "aeiouAEIOU")`](#get-count) |
| `key=...` 比较 | 指定比较依据 | [`min(set(arr), key=arr.count)`](#stray) |
| f-string | 格式化字符串 | [`f"found the needle at position ..."`](#find-needle) |
| 平方根判断 | 判断是否为整数平方根 | [`root = sq ** 0.5`](#find-next-square) |
| 列表拼接 | 把两个列表接在一起 | [`l + [0] * n`](#move-zeros) |
| 列表重复 | 快速生成 n 个相同元素 | [`[0] * n`](#move-zeros) |
| 整除 `//` | 做除法并向下取整 | [`available.get(k, 0) // v`](#cakes) |
