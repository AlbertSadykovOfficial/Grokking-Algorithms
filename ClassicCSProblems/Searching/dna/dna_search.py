# IntEnum позволяет использовать операторы сравнение, в отличие от Enum
from enum import IntEnum 
from typing import Tuple, List # Для аннотаций типа


# Нуклеотид - атомарная единица Гена 
# Кодон - кобинация 3х нуклеотидов.
# Ген - список Кодонов

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

# Преобразовать строку Нуклеотидов в Ген
# Функция проходит строку и преоразует каждые 3 символа в объекты Codon,
# затем добавляет их в конец каждого объекта Gene

def string_to_gene(s: str) -> Gene:
		gene: Gene = []
		for i in range(0, len(s), 3):
				if (i + 2) >= len(s): # Если не полный Кодон, забиваем на него и отсылоем то, что есть
						return gene
				codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
				gene.append(codon)
		return gene

# Линейный поиск
# Время: O(n)
def linear_contains(gene: Gene, key_codon: Codon) -> bool:
		for codon in gene:
				if codon == key_codon:
						return True
		return False

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


#
# Проверка работы
#
gene_str: str = "TAGGGATTAACCGGTATATATGCCTATATGCAAACGTTTTGCATTGCATTTGAAACCCTGAGGATGTGGCCA"

my_gene: Gene = string_to_gene(gene_str)
acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

# Линейный поиск
print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))

# Бинарный поиск (требуется предварительная сортировка данных)
my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_gene, acg))
print(binary_contains(my_gene, gat))

