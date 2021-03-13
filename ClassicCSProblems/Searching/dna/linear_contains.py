# Линейный поиск
# Время: O(n)
def linear_contains(gene: Gene, key_codon: Codon) -> bool:
		for codon in gene:
				if codon == key_codon:
						return True
		return False