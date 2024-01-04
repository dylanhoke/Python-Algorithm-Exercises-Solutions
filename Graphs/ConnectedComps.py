def solution(adj_list):
    
    def dfs(node):
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    n = len(adj_list)
    visited = [False] * n
    connected_components = 0

    for i in range(n):
        if not visited[i]:
            dfs(i)
            connected_components += 1

    return connected_components