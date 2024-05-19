# SAlgorithms

这是一个Python算法库,包含了各种常见的搜索、排序、图和加密算法的实现。该库旨在提供一组易于使用、高效且经过测试的算法,以帮助开发者快速实现和应用这些算法。

## 安装

要使用该库,只需将其克隆到本地即可:

```bash
pip install salgorithms
```

然后,你可以将 `algorithms` 目录添加到你的 Python 项目中,或者将其添加到 Python 的模块搜索路径中。

## 使用

要使用该库中的算法,只需从相应的模块中导入所需的函数即可。例如:

```python
from algorithms.searching import binary_search
from algorithms.sorting import bubble_sort
from algorithms.graph import bfs
from algorithms.cipher import caesar_cipher

# 使用二分查找
result = binary_search([1, 3, 5, 7, 9], 5)
print(f"Binary Search: {result.result}, Time: {result.time}")

# 使用冒泡排序
result = bubble_sort([64, 34, 25, 12, 22, 11, 90])
print(f"Bubble Sort: {result.result}, Time: {result.time}")

# 使用广度优先搜索
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(graph, 'A')

# 使用凯撒密码
encrypted_text = caesar_cipher("Hello, World!", 3)
print(f"Caesar Cipher: {encrypted_text}")
```

每个算法函数都使用了 `@timer_decorator` 装饰器,因此它们的返回值是一个 `AlgorithmResult` 对象,其中包含算法的执行结果和执行时间。

## 算法

该库包含以下算法:

### 搜索算法
- 二分查找
- 线性查找
- 插值查找
- 跳跃查找

### 排序算法
- 冒泡排序
- 堆排序
- 插入排序
- 归并排序
- 快速排序
- 选择排序
- 桶排序
- 鸡尾酒排序
- 基数排序
- 希尔排序

### 图算法
- 广度优先搜索 (BFS)
- 深度优先搜索 (DFS)
- 贪心集合覆盖

### 加密算法
- 凯撒密码
- 维吉尼亚密码
- 置换密码
- RSA加密

## 贡献

如果你想为该库做出贡献,欢迎提交问题和拉取请求。在提交拉取请求之前,请确保你的代码符合项目的编码风格,并通过了所有测试。

## 许可证

该项目采用 MIT 许可证。有关更多信息,请参阅 `LICENSE` 文件。