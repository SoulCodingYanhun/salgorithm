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
9. 桶排序（Bucket Sort）
10. 鸡尾酒（Cocktail Sort）
11. 基数排序（Radix sort）
12. Shell排序（Shell sort）
13. 线性搜索（Linear Search）
14. 插值搜索（Interpolation Search）
15. 跳转搜索（Jump Search）
16. 禁忌搜索（Tabu Search）
17. 凯撒密码
18. Vigenère密码
19. RSA (Rivest–Shamir–Adleman)

### 调用库：

```python
# 调用
from salgorithm import *
# 还要加上
import random
import math
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

# 桶排序
arr = [4, 6, 2, 4.99, 0.39, 1, 5]
sorted_arr = bucket_sort(arr)
print(sorted_arr)

# 鸡尾酒排序
arr = [5, 3, 8, 4, 2, 0, 1]
sorted_arr = cocktail_sort(arr)
print(sorted_arr)

# 基数排序
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_arr = radix_sort(arr)
print(sorted_arr)

# Shell排序
arr = [5, 3, 8, 4, 2, 0, 1]
sorted_arr = shell_sort(arr)
print(sorted_arr)

# 线性搜索
arr = [5, 2, 9, 1, 7]
target = 9

result = linear_search(arr, target)
if result != -1:
    print(f"目标值 {target} 在数组中的索引为 {result}")
else:
    print("目标值不在数组中")

# 插值搜索代码
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6

result = interpolation_search(arr, target)
if result != -1:
    print(f"目标值 {target} 在数组中的索引为 {result}")
else:
    print("目标值不在数组中")

# 跳转搜索
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 11

result = jump_search(arr, target)
if result != -1:
    print(f"目标值 {target} 在数组中的索引为 {result}")
else:
    print("目标值不在数组中")

# 禁忌搜索（Tabu Search）
import random
import math

def distance(city1, city2):
    # 计算两个城市之间的距离
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def generate_initial_solution(num_cities):
    # 生成初始解，随机排列城市
    cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_cities)]
    return random.sample(cities, num_cities)

def generate_neighborhood(solution):
    # 生成当前解的邻域解，交换两个城市的位置
    neighborhood = []
    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            neighbor = solution.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighborhood.append(neighbor)
    return neighborhood

def calculate_total_distance(solution):
    # 计算解的总距离
    total_distance = 0
    for i in range(len(solution)-1):
        total_distance += distance(solution[i], solution[i+1])
    total_distance += distance(solution[-1], solution[0])
    return total_distance

def tabu_search(initial_solution, neighborhood_func, objective_func, tabu_list_size, max_iterations):
    current_solution = initial_solution
    best_solution = current_solution
    tabu_list = []

    for _ in range(max_iterations):
        neighborhood = neighborhood_func(current_solution)
        best_neighbor = None
        best_neighbor_value = float('inf')

        for neighbor in neighborhood:
            if neighbor not in tabu_list:
                neighbor_value = objective_func(neighbor)
                if neighbor_value < best_neighbor_value:
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value

        if best_neighbor is None:
            break

        current_solution = best_neighbor
        tabu_list.append(best_neighbor)
        if len(tabu_list) > tabu_list_size:
            tabu_list.pop(0)

        if objective_func(best_neighbor) < objective_func(best_solution):
            best_solution = best_neighbor

    return best_solution

# 参数设置
num_cities = 10
tabu_list_size = 5
max_iterations = 100
	# 生成初始解
initial_solution = generate_initial_solution(num_cities)
	# 定义邻域函数和目标函数
neighborhood_func = generate_neighborhood
objective_func = calculate_total_distance
	# 运行禁忌搜索算法
best_solution = tabu_search(initial_solution, neighborhood_func, objective_func, tabu_list_size, max_iterations)
	# 输出结果
print("最佳路径：", best_solution)
print("最佳路径长度：", calculate_total_distance(best_solution))

# 凯撒密码
text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Encrypted Text:", encrypted_text)
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted Text:", decrypted_text)

# Vigenère密码
text = "Hello, World!"
key = "KEY"
encrypted_text = vigenere_cipher(text, key)
print("Encrypted Text:", encrypted_text)
decrypted_text = vigenere_cipher(encrypted_text, key)
print("Decrypted Text:", decrypted_text)


# 转置密码
text = "Hello, World!"
key = "KEY"
encrypted_text = transpose_cipher(text, key)
print("Encrypted Text:", encrypted_text)
decrypted_text = transpose_cipher(encrypted_text, key)
print("Decrypted Text:", decrypted_text)

# RSA (Rivest–Shamir–Adleman)
	# 选择两个不同的质数作为p和q
p = 61
q = 53
	# 生成公钥和私钥
public_key, private_key = generate_keypair(p, q)
	# 要加密的消息
message = "Hello, World!"
	# 加密消息
encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)
	# 解密消息
decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
```




