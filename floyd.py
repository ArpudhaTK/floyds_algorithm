# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 23:47:39 2023

@author: arpud
"""

#include <stdio.h>
def floyd(n, C):
    A = [[0 for _ in range(n)] for _ in range(n)]

    # Initialize A matrix with the same values as C matrix
    for i in range(n):
        for j in range(n):
            A[i][j] = C[i][j]

    # Set diagonal elements to 0
    for i in range(n):
        A[i][i] = 0

    # Main Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]

    return A
n = 4  # Replace with your desired value of n
INF = float('inf')  # Replace with your representation of infinity
C = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]  # Replace with your actual graph matrix

result = floyd(n, C)

# Output the result
print("Shortest path distances:")
for row in result:
    print("\t".join(map(lambda x: "{:.2f}".format(x), row)))
