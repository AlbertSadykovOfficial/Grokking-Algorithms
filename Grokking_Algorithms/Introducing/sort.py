"""
	
	Медленная Сортировка

	Скорость работы алгоритма: O(0.5*n^2)) - Квадратичное время
														но т.к. коэф. не учитываются, то просто O(n^2)
"""
def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i

	return smallest_index

def selectionSort(arr):
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
		newArr.append(arr.pop(smallest))
	return newArr

print(selectionSort([5,2,3,6,10]))