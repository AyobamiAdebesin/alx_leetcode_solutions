#!/usr/bin/python3
# """ Travelling sales man problem with brute force """
# import itertools

# def tsp_brute_force(graph):
#     # Generate all possible permutations of the cities
#     cities = list(graph.keys())
#     permutations = list(itertools.permutations(cities))

#     # Initialize the minimum distance and path
#     min_distance = float('inf')
#     min_path = None

#     # Iterate through each permutation
#     for path in permutations:
#         distance = 0

#         # Calculate the total distance for the current path
#         for i in range(len(path) - 1):
#             distance += graph[path[i]][path[i+1]]

#         # Check if the current path has a shorter distance
#         if distance < min_distance:
#             min_distance = distance
#             min_path = path

#     return min_path, min_distance

# # Example usage
# graph = {
#     'A': {'B': 10, 'C': 15, 'D': 20},
#     'B': {'A': 10, 'C': 35, 'D': 25},
#     'C': {'A': 15, 'B': 35, 'D': 30},
#     'D': {'A': 20, 'B': 25, 'C': 30}
# }

# min_path, min_distance = tsp_brute_force(graph)
# print("Minimum path:", min_path)
# print("Minimum distance:", min_distance)
# def solution(n):
#     area = 0
#     odd_nums = [1]
#     count = 1
#     odd_no = 1
#     while count < n:
#         odd_no += 2
#         odd_nums.append(odd_no)
#         count += 1
#     odd_nums = odd_nums + odd_nums[0: n-1]
#     print(odd_nums)
#     return sum(odd_nums)
a = "010100101"
a.index()