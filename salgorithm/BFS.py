from collections import deque

def bfs(graph, start):
    visited = set()  # 用于记录已访问的节点
    queue = deque([start])  # 使用队列来进行广度优先搜索
    visited.add(start)  # 将起始节点标记为已访问

    while queue:
        node = queue.popleft()  # 取出队列中的节点
        print(node, end=" ")  # 输出节点值

        # 遍历当前节点的邻居节点
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)  # 将未访问的邻居节点加入队列
                visited.add(neighbor)  # 标记邻居节点为已访问
