'''
Given an unsorted array, find kth largest element in it.
'''

def findKthLargest(arr, k):
    k = len(arr)-k
    def quickSelect(l, r):
        pivot, p = arr[r], l
        for i in range(l, r):
            if arr[i] <= pivot:
                arr[p], arr[i] = arr[i], arr[p]
                p += 1
        arr[p], arr[r] = arr[r], arr[p]
        if p > k: return quickSelect(l, p-1)
        elif p < k: return quickSelect(p+1, r)
        else:
            return arr[p]
        
    return quickSelect(0, len(arr)-1)

if __name__ == "__main__":
    print(findKthLargest([3,2,1,5,6,4], 2))



# Time Complexity: O(n)