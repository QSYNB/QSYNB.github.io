---
title: python
date: 2026-02-24 11:22:46
tags:
---
``` python
def fake_bin(x):
    # 一行搞定：遍历 x，如果是 <5 就给 '0'，否则给 '1'
    # .join() 把列表里的元素用 '' 连接起来
    # 单引号或者双引号都可以
    return "".join(["0" if int(d) < 5 else "1" for d in x]) 

```
``` python
def fake_bin(x):
    # 创建映射表：01234 变成 0，56789 变成 1
    table = str.maketrans("0123456789", "0000011111")
    # .translate() 把 x 里的字符根据 table 映射表替换
    return x.translate(table)
```
``` python
def remove_char(s):
    # 从索引 1 开始，截取到倒数第 1 个之前
    return s[1:-1]
```
关键知识点：split()
语法：string.split(separator)
例子："10:5".split(":") 结果是 ['10', '5']。

``` python 
def points(games):
    # 逻辑：如果是赢(3分)，如果是平(1分)，否则0分
    return sum(3 if g[0] > g[2] else 1 if g[0] == g[2] else 0 for g in games)
```
``` python
def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'
    # .index() 查找子字符串第一次出现的索引
```
``` python
def getCount(inputStr):
return sum(1 for let in inputStr if let in "aeiouAEIOU")
# let in "aeiouAEIOU" 检查 let 是否在这个字符串里 
```
``` python
def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and all(n in "0123456789" for n in pin)
    # all() 检查可迭代对象里的所有元素是否都为 True

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
    # pin.isdigit() 检查 pin 是否只包含数字字符
```
``` python
def count_positives_sum_negatives(arr):
    return [sum(1 for x in arr if x > 0),sum(x for x in arr if x <0)] if arr else []
```
```python
def filter_list(l):
    # 翻译：如果 i 是 int 类型的一个实例
    return [i for i in l if isinstance(i, int)]
```
```python
def count_by(x, n):
    # 产生 1 到 n 的数字（注意 range 是左闭右开，所以要 n + 1）
    # range(start, stop[, step])
    return [i * x for i in range(1, n + 1)]
```
```python
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
```
```python
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())
    ### .join() 把列表里的元素用 '' 连接起来
    ### .split() 把字符串用 '' 分割成列表
    ### .capitalize() 把字符串的第一个字符变成大写
```
```python
def count_sheeps(arrayOfSheeps):
  return arrayOfSheeps.count(True)
```
```python
def DNAtoRNA(dna):
    return dna.replace('T', 'U')

def dna_to_rna(dna):
    # 注意：DNA 里的胸腺嘧啶是 T，RNA 里的尿嘧啶是大写的 U 喔！
    return "".join("U" if i == "T" else i for i in dna)

    ### 筛选逻辑（只要精华）：if 放在 for 后面。
    ### 二选一逻辑（这个变那个）：if-else 整个结构必须放在 for 的前面。
```
```python
def longest(a1, a2):
    # your code
    return "".join(sorted(set(a1 + a2)))
```
```python
def min_max(lst):
    return [min(lst),max(lst)]
```
```python
def find_next_square(sq):
    root = sq ** 0.5 # 计算平方根
    if root.is_integer(): # 如果平方根是整数
        return (root + 1)**2
    return -1
```
```python
def to_alternating_case(string):
    return string.swapcase()
    ### .swapcase() 把字符串里的大写字母变成小写字母，小写字母变成大写字母
```
```python   
def stray(arr):
    return min(set(arr), key=arr.count)
    ### .count() 统计元素在列表里的出现次数
    ### .set() 把列表里的重复元素去掉
    ### key=arr.count 按出现次数最少的元素排序
```
```python
def solution(s):
    # 先补一个下划线，防止末尾落单
    s += "_"
    # 从 0 开始，每隔 2 个取一段，长度为 2
    # range 里的 len(s)-1 是为了防止偶数长度时多出一个 "__"
    return [s[i:i+2] for i in range(0, len(s)-1, 2)]
```
