# Бинарный поиск
# Время алгоритма: O(log(n))
#	
# Но помимо алгоритма требуется отсортировать данные6
# Время сортировки: O(n*lob(n)) - В ЛУЧШЕМ СЛУЧАЕ
#
# Вывод:
#	Если нужно найти ОДИН раз, то лучше воспользоваться линейным поиском
# Если нужно будет искать много раз, то пользуемся БИНАРНЫМ поиском
#
def binary_contains(gene: Gene, key_codon: Codon) -> bool:
		left: int = 0
		right: int = len(gene) - 1
		while left <= right: # Пока есть что искать
				middle: int = (left + right) // 2
				if gene[middle] < key_codon:
						left = middle + 1
				elif gene[middle] > key_codon:
						right = middle - 1
				else:
						return True
		return False
