"""

		Сжатие данных

				Сжатие - процесс кодирования данных таким образом, чтобы они аниали меьше места
				Распаковка - возвращениеданных в исходную форму

				Для сжатия нужно время на упаковку и распаковку, 
				соответсвтенно сжатие применяеся не всегда, 
				а только в случаях, когда неьольшой размер важнее быстрого выполнеия

				К примеру: 
					 Для передачи больших файлов через интернет сжатие имеет смысл,
					 поскольку для передачи файлов потребуется больше времени,
					 чем для их распаковки после получения.

				Бывает, что данные занимают меньше места, чем переменные на котороые
				они расчитаны, чилса, которые не превышают 16 бит хранятся в 64 битах.

				В Python из-за простоты существует 1 тип - int, который позволяет хранить
				числа произвольной точности. Но из-за вычислительных издержек,
				свойственных Python этот тип минимум занимает 28 байтов.


				Пример:
						Есть нуклеотиды, которые образуют ген ДНК: A, C, G и T
						Если  ген хранится как тип str, то его можно рассматривать
						как коллекцию Unicode, каждый символ - 8 бит.

						НО! в 2-ом коде можно ограничится только 2 битами для 4х значений:
						00 01 10 11
						Т.е. сжатие в 4 раза.

						Поэтому: 

								Вместо того, чтобы храниить строку как тип str, ее можно хранить
								как строку битов 

"""

class CompressedGene:
		def __init__(self, gene: str) -> None:
				self._compress(gene)

		# Нижнее подчеркивание - скрытый метод (формально)
		def _compress(self, gene: str) -> None:
				self.bit_string: int = 1 # Начальная метка
				for nucleotide in gene.upper():
						# Каждый нуклеотид занимает 2 бита
						# Поэтому мы кадый раз сдвигаем влево на 2 бита
						# И добавляем в строку битов соответсвующее значение
						self.bit_string <<= 2 
						if	nucleotide == "A": # Поменять 2 последних бита на 00
								self.bit_string |= 0b00
						elif	nucleotide == "C": # Поменять 2 последних бита на 01
								self.bit_string |= 0b01
						elif	nucleotide == "G": # Поменять 2 последних бита на 10
								self.bit_string |= 0b10
						elif	nucleotide == "T": # Поменять 2 последних бита на 11
								self.bit_string |= 0b11
						else:
								raise ValueError("Invalid Nucleotide:{}".format(nucleotide))

		def decompress(self) -> str:
				gene: str = ""
				# Считываем из строки битов по 2 бита
				# При этом ставим (-1), чтобы исключить метку
				for i in range(0, self.bit_string.bit_length() - 1, 2):
						bits: int = self.bit_string >> i & 0b11
						if bits == 0b00:
								gene += "A"
						elif bits == 0b01:
								gene += "C"
						elif bits == 0b10:
								gene += "G"
						elif bits == 0b11:
								gene += "T"
						else:
								raise ValueError("Invalid bits:{}".format(bits))
				return gene[::-1] # [::-1] - обращение строки посредством оратных срезов

		# Выводим
		def __str__(self) -> str:
				return self.decompress()


if __name__ == "__main__":
		from sys import getsizeof
		original: str = "TAGGGATTAACCGGTATATATGCCTATATGCAAACGTTTTGCATTGCATTTGAAACCCTGAGGGATTGGCCA" * 100
		print("original is {} bytes".format(getsizeof(original)))
		compressed: CompressedGene = CompressedGene(original) # Сжатие
		print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
		print(compressed)
		print("original and decomressed are the same: {}".format(original == compressed.decompress()))