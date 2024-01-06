# def solution(adj_list, start, end):
#     n = len(adj_list)
#     visited = [False] * n
#     queue = [[start]]

#     while queue:
#         path = queue.pop(0)
#         current_city = path[-1]

#         if current_city == end:
#             return path

#         if not visited[current_city]:
#             visited[current_city] = True
#             neighbors = adj_list[current_city]
#             for neighbor in neighbors:
#                 new_path = path + [neighbor]
#                 queue.append(new_path)

#     return []

from collections import deque

def solution(adj_list, start, end):
    n = len(adj_list)
    
    if start < 0 or start >= n or end < 0 or end >= n:
        return []

    visited = [False] * n
    queue = deque([[start]])

    while queue:
        path = queue.popleft()  # Use popleft for efficient queue operations
        current_city = path[-1]

        if current_city == end:
            return path

        if not visited[current_city]:
            visited[current_city] = True
            neighbors = adj_list[current_city]
            for neighbor in neighbors:
                new_path = path + [neighbor]
                queue.append(new_path)

    return []