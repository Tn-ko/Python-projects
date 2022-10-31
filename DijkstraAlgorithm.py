graph = {}
graph["start"] = {}
graph ["start"]["a"] = 6
graph ["start"]["b"] = 2

graph ["a"] = {}
graph ["a"]["end"] = 1

graph ["b"] = {}
graph ["b"]["a"] = 3
graph ["b"]["end"] = 5

graph ["end"] = {} 

infinity = float("inf")
costs = {}
costs["a"] = 6 # 5
costs["b"] = 2
costs["end"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
            return lowest_cost_node

node = find_lowest_cost_node(costs) # выбор узла с наименьшим весом, который ещё не проверен

while node is None:
    cost = costs[node]
    neighbors = graph[node]

    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            cost[n] = new_cost
            parents[n] = node

            processed.append(node)

            node = find_lowest_cost_node

print(costs)