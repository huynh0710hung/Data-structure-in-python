# Bubble Sorting
def bubbleSort(self, arr):
    for x in range(0, len(arr) - 1): # Outer loop to reduce right boundary of inner loop by 1
        end = len(arr)
        for pt in range(1, end): # Inner loop to compare adjacent elements (always checks from beginning)
            if arr[pt - 1] > arr[pt]:
                arr[pt - 1], arr[pt] = arr[pt], arr[pt - 1] # Swapping adjacent elements
            end = end - 1
    return arr

# Selection Sort
def selectionSort(self, arr):
    for pt1 in range(0, len(arr) - 1): # Outer loop to increase left boundary of inner loop by 1
        smallest = pt1 # pt1 starts with 0, then increases until length of array - 1
        for pt2 in range(pt1 + 1, len(arr)): # loop to find the smallest number after arr[pt1] to replace with arr[pt1]
            if arr[pt2] < arr[smallest]: smallest = pt2
        if arr[smallest] < arr[pt1]:
            arr[pt1], arr[smallest] = arr[smallest], arr[pt1]
    return arr

# Insertion Sort
def insertionSort(self, arr):
    for pt1 in range(1, len(arr)):
        for pt2 in range(0, pt1):
            if arr[pt1] < arr[pt2]:
                arr.insert(pt2, arr.pop(pt1))
                break
    return arr

# Merge Sort
def mergeSort(self, arr):
    def merge(lArr, rArr):
        lpt, rpt, result = 0, 0, []
        while (lpt < len(lArr) and rpt < len(rArr)):
            if lArr[lpt] < rArr[rpt]:
                result.append(lArr[lpt]); lpt += 1
            else:
                result.append(rArr[rpt]); rpt += 1
        while (lpt < len(lArr)): result.append(lArr[lpt]); lpt += 1
        while (rpt < len(rArr)): result.append(rArr[rpt]); rpt += 1
        return result
#-----------------------------------------------------------------------------------
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = self.mergeSort(arr[0:mid])
    right = self.mergeSort(arr[mid:])
    return merge(left, right)

# Quick Sort
def quickSort(self, arr):
    if len(arr) <= 1: return arr
    leftArr, rightArr, pivot = [], [], arr.pop()
    for x in arr: leftArr.append(x) if x < pivot else rightArr.append(x)
    return self.quickSort(leftArr) + [pivot] + self.quickSort(rightArr)

# Radix Sort
def radixSort(self, arr):
    maxPos = max([len(str(y)) for y in arr])
    def getDigit(num, pos): # Helper function to get digit of specified position
        return 0 if len(str(num)) < pos else int(str(num)[len(str(num)) - pos])
    for pos in range(1, maxPos + 1):
        resDict = {x: [] for x in range(10)} # Resetting dictionary to empty list for keys (0-9)
######################################
        while arr:
            num = arr.pop(0)
            resDict[getDigit(num, pos)].append(num) # Pop & add array element to dict (arr positional values = dictionary key)
######################################
        for key in resDict: arr = arr + resDict[key] # Re-adding elements to arr as perdict key order
    return arr

# Heap Sort
def heapsort(self, arr):
    n = len(arr)
    hp.heapify(arr)
    return [hp.heappop(arr) for i in range(n)]