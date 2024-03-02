# salgorithm

### 介绍：

此库是一个算法简化工具可以让算法只用一行代码就吧复杂的算法写成一个简单的只用函数就能调用的算法

### 简化的算法：

1. 冒泡排序（Bubble Sort）
2. 选择排序（Selection Sort）
3. 插入排序（Insertion Sort）
4. 归并排序（Merge Sort）
5. 快速排序（Quick Sort）
6. 堆排序（Heap Sort）
7. 二分查找（Binary Search）
8. 深度优先搜索（Depth First Search，DFS）

### 调用库：

```python
from salgorithm import *
```

### 算法调用：

```python
# 冒泡排序（Bubble Sort）
arr = [5, 3, 8, 2, 1, 9, 4, 7, 6, 10]
sorted_arr = bubble_sort(arr)
print(f"冒泡排序结果：{sorted_arr}")


# 选择排序（Selection Sort）
arr = [5, 3, 8, 2, 1, 9, 4, 7, 6, 10]
sorted_arr = selection_sort(arr)
print(f"选择排序结果：{sorted_arr}")


# 插入排序（Insertion Sort）
arr = [5, 3, 8, 2, 1, 9, 4, 7, 6, 10]
sorted_arr = insertion_sort(arr)
print(f"插入排序结果：{sorted_arr}")


# 归并排序（Merge Sort）
arr = [5, 3, 8, 2, 1, 9, 4, 7, 6, 10]
sorted_arr = merge(arr)
print(f"归并排序结果：{sorted_arr}")


# 快速排序（Quick Sort）
arr = [5, 3, 8, 2, 1, 9, 4, 7, 6, 10]
sorted_arr = quick_sort(arr)
print(f"快速排序结果：{sorted_arr}")


# 堆排序（Heap Sort）
arr = [5, 3, 8, 2, 1, 9, 4, 7, 6, 10]
heapify(arr)
print(f"堆排序结果：{arr}")


# 二分查找（Binary Search）
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search(arr, target)
print(f"二分搜索结果：{result}")


# 深度优先搜索（Depth First Search，DFS）
# 此算法简易暂时别用因为还没完全写好
graph = {
	'A': ['B', 'C'],
	'B': ['D', 'E'],
	'C': ['F'],
	'D': [],
	'E': ['F'],
	'F': []
}
start_node = 'A'
dfs(graph, start_node)
```




