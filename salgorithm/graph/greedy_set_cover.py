from algorithms.utils.timer import timer_decorator

@timer_decorator
def greedy_set_cover(universe, subsets):
    covered = set()
    selected_subsets = []

    while covered != universe:
        best_subset = None
        best_coverage = 0

        for subset in subsets:
            coverage = len(subset - covered)
            if coverage > best_coverage:
                best_subset = subset
                best_coverage = coverage

        covered |= best_subset
        selected_subsets.append(best_subset)

    return selected_subsets