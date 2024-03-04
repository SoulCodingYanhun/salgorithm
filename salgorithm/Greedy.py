def greedy_set_cover(universe, subsets):
    selected_subsets = []  # 存储被选择的子集

    while universe:  # 当宇宙集合非空时
        best_subset = None  # 当前最优子集
        max_covered = set()  # 当前最优子集覆盖的元素集合

        for subset in subsets:
            covered = universe.intersection(subset)  # 计算子集与宇宙集合的交集
            if len(covered) > len(max_covered):
                best_subset = subset
                max_covered = covered

        universe -= max_covered  # 从宇宙集合中移除被覆盖的元素
        selected_subsets.append(best_subset)  # 将最优子集加入到被选择的子集中

    return selected_subsets