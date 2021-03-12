"""

		Число PI

				Ряд Лейбница для получения числа PI:
						PI = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11

						Закономерности ряда:

							1) Числитель всегда 4
							2) Знаменатель увеличивается на 2
							3) Знак чередуется с + на -

"""


def calculete_pi(n_terms: int) -> float:
		pi: float = 0
		k : int = 1
		z : int = 1
		for _ in range(n_terms):
				pi += k * 4/z
				k = k * -1
				z = z + 2
		return pi

if __name__ == "__main__":
		result: float = calculete_pi(100000)
		print(result)
