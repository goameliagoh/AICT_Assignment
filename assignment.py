import heapq
import time
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt



def path_exists(graph, start, target):
    visited = set()  # create set to store visited/explored nodes
    queue = deque([start])  # Create and initialize queue/frontier with start node
    
    while queue:
        node = queue.popleft()  # Pop front node from queue
        
        if node == target:  # Check if target node is reached
            return True
        
        if node not in visited:
            visited.add(node)  # Add node to visited/explored
            
            # Expand and add unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return False 

# BFS - Breadth-First Search
from collections import deque

def bfs_path(graph, start, end):
    start_time = time.time()
    queue = deque([start])  # Queue stores nodes only
    visited = set([start])  # Start with the initial node visited
    parent = {start: None}  # To reconstruct the path
    cost = {start: 0}

    while queue:
        node = queue.popleft()  # Get the current node

        if node == end:
            # Reconstruct the path from start to goal
            path = []
            totalCost = cost[node]
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()  # Reverse the path to get start-to-goal order
            end_time = time.time()  # Record the end time
            runtime = end_time - start_time
            return {'path':path, 'runtime':runtime, 'gCost':totalCost,'nodesVisited':len(visited)}

        for neighbor,weight in graph[node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node  # Set the current node as the parent of the neighbor
                cost[neighbor] = cost[node] + weight 
                queue.append(neighbor)

    return None  # Return None if no path is found

    

# DFS - Depth-First Search
def dfs_path(graph, start, end):
    start_time = time.time()
    stack = [start]  # Stack stores nodes only
    visited = set()  # To keep track of visited nodes
    parent = {start: None}  # To reconstruct the path
    cost = {start:0}
    while stack:
        node = stack.pop()  # Pop the most recent node

        if node == end:
            # Reconstruct the path from start to goal
            path = []
            totalCost = cost[node]
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()  # Reverse the path to get start-to-goal order
            end_time = time.time()  # Record the end time
            runtime = end_time - start_time
            return {'path':path, 'runtime':runtime, 'gCost':totalCost, 'nodesVisited':len(visited)}

        if node not in visited:
            visited.add(node)  # Mark the node as visited

            for neighbor,weight in graph[node].items():
                if neighbor not in visited:
                    parent[neighbor] = node  # Set the current node as the parent of the neighbor
                    cost[neighbor] = cost[node] + weight 
                    stack.append(neighbor)  # Add the neighbor to the stack for further exploration

    return None  # Return None if no path is found


# GBFS - Greedy Best-First Search

def gbfs(graph, start, goal, heuristic):
    start_time = time.time()
    open_list = [(0, start)]  # (priority, node)
    visited = set()
    parent = {start: None}
    g_cost = {start: 0}

    while open_list:
        _, node = heapq.heappop(open_list)

        if node == goal:
            # Reconstruct the path
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()  # Reverse for start-to-goal order
            end_time = time.time()  # Record the end time
            runtime = end_time - start_time
            return {'path': path, 'gCost': g_cost[path[-1]], 'runtime': runtime, 'nodesVisited':len(visited)}  # Return total cost of path

        visited.add(node)

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                parent[neighbor] = node
                g_cost[neighbor] = g_cost[node] + weight
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    return None  # If no path is found


# A* Search Algorithm
def a_star(graph, start, goal, heuristic):
    start_time = time.time()

    open_list = [(0, start)]  # (f_cost, node)
    visited = {start}
    parent = {start: None}
    g_cost = {start: 0}

    while open_list:
        _, node = heapq.heappop(open_list)

        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            end_time = time.time()  # Record the end time
            runtime = end_time - start_time
            return {'path':path, 'gCost':g_cost[goal], 'nodesVisited':len(visited), 'runtime':runtime}

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = node
                g_cost[neighbor] = g_cost[node] + weight
                h_cost = heuristic[neighbor]
                f_cost = g_cost[neighbor] + h_cost
                heapq.heappush(open_list, (f_cost, neighbor))
    return None  # No path found

# Example heuristic function for GBFS and A*
def heuristic(node):
    # This is a simple heuristic, you can customize based on your problem
    # In a real-world application, you would compute heuristic based on the city's layout
    return 0

# Example graph creation and usage
graph = {
    'A': {'B': 5, 'C': 10, 'D':4},
    'B': {'A': 5, 'C': 8, 'D': 7, 'E': 9, 'F': 14},
    'C': {'B': 8, 'D': 6, 'E': 11, 'F': 10},
    'D': {'A': 3, 'B': 7, 'C': 6, 'E': 4, 'F': 8},
    'E': {'B': 9, 'C': 11, 'D': 4, 'F': 13},
    'F': {'A': 12, 'B': 14, 'C': 10},
    'G': {'B': 6, 'C': 9, 'D': 7, 'E': 11},
    'H': {'B': 5, 'C': 7, 'D': 6, 'E': 12, 'F': 10},
    'I': {'A': 9, 'F': 9},
    'J': {'A': 7, 'F': 6}
}

heuristics = {
    'A': 0,
    'B': 5,
    'C': 6,
    'D': 3,
    'E': 4,
    'F': 7,
    'G': 5,
    'H': 6,
    'I': 4,
    'J': 6
}


G = nx.DiGraph()

# Add edges and weights
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# Draw the graph
pos = nx.spring_layout(G)  # Position the nodes using the spring layout
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=100, font_size=10, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, "weight")  # Get edge weights
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Add labels to edges

# Show the graph
plt.title("Node Graph Visualization")
plt.show()
def graphs(start,goal,graph,heuristic):
    results = {
        "A*": a_star(graph, start, goal, heuristic),
        "GBFS": gbfs(graph, start, goal, heuristic),
        "BFS": bfs_path(graph, start, goal),
        "DFS": dfs_path(graph, start, goal)
    }

    algorithms = list(results.keys())
    path_costs = [results[algo]['gCost'] for algo in algorithms]
    nodes_expanded = [results[algo]['nodesVisited'] for algo in algorithms]
    runtimes = [results[algo]['runtime'] for algo in algorithms]

    # Create bar graphs
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    # Bar chart for path cost
    axs[0].bar(algorithms, path_costs, color=['blue', 'green', 'red', 'purple'])
    axs[0].set_title("Path Cost Comparison")
    axs[0].set_ylabel("Cost")

    # Bar chart for nodes expanded
    axs[1].bar(algorithms, nodes_expanded, color=['blue', 'green', 'red', 'purple'])
    axs[1].set_title("Nodes Expanded Comparison")
    axs[1].set_ylabel("Nodes Visited")

    # Bar chart for execution time
    axs[2].bar(algorithms, runtimes, color=['blue', 'green', 'red', 'purple'])
    axs[2].set_title("Execution Time Comparison")
    axs[2].set_ylabel("Time (seconds)")

    # Display the plots
    plt.tight_layout()
    plt.show()
while True:
        print("-------------------MENU-----------------")
        print("[1] Breadth First Search")
        print("[2] Depth First Search")
        print("[3] Greedy Best First Search")
        print("[4] A star")
        print("[5] Compare all algorithms")
        print("[0] Exit")
        choice = int(input("Please choose an option: "))
        start = str(input("Please enter your start location: "))
        goal = str(input("Please enter your goal location: "))  
        if choice == 1:
            pathExists = path_exists(graph,start,goal)
            if pathExists == True:
                newbfsData = bfs_path(graph,start,goal)
                print('Path found: ',newbfsData['path'])
                print('Calcultion time: ',newbfsData['runtime'])
                print("Goal cost: ",newbfsData['gCost'])
            else:
                print("Path not found")
        if choice == 2:
            pathExists = path_exists(graph,start,goal)
            if pathExists == True:
                newdfs = dfs_path(graph,start,goal)
                print('Path found: ',newdfs['path'])
                print('Calculation time: ',newdfs['runtime'])
                print('Goal Cost: ',newdfs['gCost'])
            else:
                print("Path not found")
        elif choice == 3:
            pathExists = path_exists(graph,start,goal)
            if pathExists == True:
                gbfsData = gbfs(graph,start,goal,heuristics)
                print('Path found: ',gbfsData['path'])
                print('Calculation time: ',gbfsData['runtime'])
                print('Goal Cost: ',gbfsData['gCost'])
            else:
                print("Path not found")
        elif choice == 4:
            pathExists = path_exists(graph,start,goal)
            if pathExists == True:
                aStar = a_star(graph,start,goal,heuristics)
                print('Path found: ',aStar['path'])
                print('Calculation time: ',aStar['runtime'])
                print('Goal Cost: ',aStar['gCost'])
                print('Nodes visited: ',aStar['nodesVisited'])
            else:
                print("Path not found")
        elif choice == 5:
            graphs(start,goal,graph,heuristics)
        elif choice == 0:
            break
        else:
            print("Enter valid input.")
# Extract data from results



