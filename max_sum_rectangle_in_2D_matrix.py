'''
Given a 2D matrix, find a submatrix with max sum
'''

# Kadane's algorithm is used to find maximum sum contigous subarray
from threading import local


def kadanes(arr, start, finish):
    max_so_far  = -float('inf')
    max_ending_here = 0
    finish[0] = -1
    local_start = 0
    for i in range(len(arr)):
        max_ending_here += arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
            local_start = i+1
        elif max_ending_here > max_so_far:
            max_so_far = max_ending_here
            finish[0] = i
            start[0] = local_start
        
        

    # is there is atleast one positive number
    if finish[0] != -1:
        return max_so_far
    
    # Special case: When all elements are negative, return the least negative
    max_sum = arr[0]
    start[0] = 0
    finish[0] = 0
    for i in range(1, len(arr)):
        if arr[i]>max_sum:
            max_sum = arr[i]
            start[0], finish[0] = i, i
    return max_sum

def find_max_submatrix(grid):
    current_sum = 0
    max_sum = -float('inf')
    max_left = 0
    max_right = 0
    max_up = 0
    max_down = 0
    l, r = 0, 0
    start=[0]
    finish=[0]
    m, n = len(grid), len(grid[0])
    for l in range(n):
        temp = [0]*m
        for r in range(l,n):
            for k in range(m):
                temp[k] += grid[k][r]
            current_sum = kadanes(temp, start, finish)
            if current_sum > max_sum:
                max_sum = current_sum
                max_left = l
                max_right = r
                max_up = start[0]
                max_down = finish[0]
    return max_sum, max_left, max_right, max_up, max_down
matrix = [
    [2,1,-3,-4,5],
    [0,6,3,4,1],
    [2,-2,-1,4,-5],
    [-3,3,1,0,3]
]
max_sum, max_left, max_right, max_up, max_down = find_max_submatrix(matrix)
print(f"Max sum is {max_sum}, with left={max_left}, right={max_right}, top={max_up}, down={max_down}")