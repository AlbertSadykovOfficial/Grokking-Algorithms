"""
		
		Шифрование

				Одноразавой шифр - способ шифрования фрагмента данных путем комбинации
													с бессмылсенным случайным фиктивным числом так, что
													оригинал не может быть восстановлен без доступа как
													к результату шифрования, так и к фикивным данным.

													Один ключ - реузльтат шифрования,
													Второй ключ - случайные фиктивные даннык.

					Исходные данные
													 \
													  > Шифрование (XOR) -> РЕЗУЛЬАТ (Ключ №2)
													 /
					Фиктивные данные
						  (Ключ №1)

					Фиктивне данные
						 (Ключ №1)		 \
													  > Дешифрование (XOR) -> Исходные данные (Ключ №2)
													 /
					РЕЗУЛЬАТ (Ключ №2)
						  
			

			Критерии фиктивных данных:

					1) Фиктивные данне должны быть той же длины, что и исходные
					2) Быть случайными (генертор должен иметь равномерный закон распредееления)
					3) Полностью секретный 

					Пункт 2 на обычных компьютерах выполнить не получится,
					случайные значения тут не случайны, а псевдослучайны



			Логика XOR:
				XOR - Искл. ИЛИ 
						( 0 ^ 1 и 1 ^ 0 - False)
						( 1 ^ 1 и 0 ^ 0 - True) 
				
						Свойства:
								A ^ B = C
								C ^ B = A
								C ^ A = B

						Данные свойства говрят нам о том, что если объединить 2 числа,
						выполнив для каждого их бита XOR, то мы можем получить один операнд
						из 2х других.
"""

from secrets import token_bytes
from typing import Tuple


# Создать int - переменную длинной length и заполнить ее случайными байтами
# Использование одного int и упаковка значений в него повыышает скорость.
#
def random_key(length: int) -> int:
		# Сгененрировать случайных байтов в количестве length
		tb: bytes = token_bytes(length)
		# Преобразовать эти байты в битову строку и вернуть ее
		return int.from_bytes(tb, "big")


def enctypt(original: str) -> Tuple[int,int]:
		original_bytes: bytes = original.encode()
		r_key: int = random_key(len(original_bytes))
		# from_bytes(Строка, которую нужно преобразовать в int, "Порядок следования")
		# Порядок следования - (с младшего или старшего разряда) 
		original_key: int = int.from_bytes(original_bytes, "big")
		encrypted: int = original_key ^ r_key
		return r_key, encrypted

# Особенность (temp):
# Прибавляем 7 к длине дешифрованных данных, 
# чтобы гарантировать округление 
# и избежать ошибки смещения на единицу
# при использовании целочисленного деления на 0 

def decrypt(key1:int, key2:int) -> str:
		decrypted: int = key1 ^ key2 # XOR
		temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
		return temp.decode() 


if __name__ == "__main__":
		key1, key2 = enctypt("One Time Pad!")
		print(key1, key2)
		result: str = decrypt(key1, key2)
		print(result)