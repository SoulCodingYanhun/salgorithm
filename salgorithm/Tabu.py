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
