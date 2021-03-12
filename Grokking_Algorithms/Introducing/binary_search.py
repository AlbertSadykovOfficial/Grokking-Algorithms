"""
	
	Бинарный поиск - на вход подаем отсортированный массив, 
									 на выходе получаем элемент массива

	Скорость работы алгоритма: O(log(n)) - Логарифмическое время.
"""
data = [1, 2, 5, 8, 11, 32, 77, 99]

to_find  = 2

def binary_search(data_array, search_value):
	low = 0;
	high  = len(data_array) - 1;
	

	while low <= high :
		mid = (low + high) // 2
		if	 data_array[mid] == search_value	: return data_array[mid]
		elif data_array[mid] > search_value		: high = mid - 1
		elif data_array[mid] < search_value		: low  = mid + 1
		print(mid)

	return None

print(binary_search(data, 32))

