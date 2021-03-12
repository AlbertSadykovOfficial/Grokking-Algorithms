
"""
Ряд фибоначи - последовательность чисел, 
							 в которой людое число, кроме 1 и 2
							 сумма предыдущих двух

Числа фибоначи(формула):
fib(n) = fib(n - 1) + fib(n - 2))


"""


# Реализация итеративным методом
# (Самый быстрый метод)
#
# Выполняется n-1 раз
# (Рекурсивные функции растут геометрически)

def iter_fib(n: int) -> int:
		if n == 0: return n # Специальный случай
		last: int = 0 # Начальное значение fib (0)
		next: int = 1 # Начальное значение fib (1)

		for _ in range(1, n):
				# Распаковка кортежа (обмен значениями)
				last, next = next, last + next
		return next

print('Итерационный метод (быстрый)')
print(iter_fib(5))
print(iter_fib(50))
print('---------------------------')

# Вывести все значения из последовательности (Генераторы)
# 
#	Цикл выполняется до yield
# 
from typing import Generator

def iter_all_fib(n: int) -> Generator[int, None, None]:
		yield 0 # Специальный случай
		if n > 0: yield 1 # Специальный случай
		last: int = 0 # Начальное значение fib (0)
		next: int = 1 # Начальное значение fib (1)

		for _ in range(1, n):
				# Распаковка кортежа (обмен значениями)
				last, next = next, last + next
				yield next # Главный этап генерации

for i in iter_all_fib(50):
		print(i)
# Реализация чисел фибоначи через рекурсивгую функцию
#
# Если значение не является базовым, то порождается еще 2 вызова функции,
# так, если для вычисления:
#
# 5 значения - 15 вызовов
#	10 значения - 177 вызовов
# 20 значения - 21 891 вызовов

def fib1(n: int) -> int:
	if n < 2: # Базовый случай
		return n
	# Рекурсивный случай
	return fib1(n - 1) + fib1(n - 2)

#if __name__ == "__main__":
print('Fib')
print(fib1(5))
print(fib1(10))
print('---------------------------')

"""

	Решение проблемы большого кол-ва вызовов

	Мемоизация - метод, при котором сохраняются результаты выполненных вычислений,
							 так, что если они снова понадобятся, их можно будет найти, вместо
							 того, чтобы выичлять их очередной раз

	Инструмент: Хэш-таблица

	Теперь можно вызывать и большие числа (50 и подобные)
	Вызов opt_fib(20) сделает 39 вызовово, а не 21 891 как fib1
"""
from typing import Dict
memo: Dict[int, int] = {0:0, 1:1} # Базовые случаи

def opt_fib(n: int) -> int:
		if n not in memo:
				memo[n] = opt_fib(n - 1) + opt_fib(n - 2)
		return memo[n]

#if __name__ == "__main__":
print('Fib + Hash-Tables')
print(opt_fib(5))
print(opt_fib(50))
print('---------------------------')

"""
	
	Автоматическая мемоизация

	В Python есть втроенный декоратор для автоматической мемоизации люой функции.
	Мы можем использовать с функцией feb1(), получив функционал opt_feb()

	Данный декоратор кэширует возвращаемое значение, 
	При последущих вызовах сохраненое значение извлекается из кэша

"""
from functools import lru_cache

@lru_cache(max_size=None) # Снимаем ограничение на кол-во кэшируемых значений
def simple_opt_fib(n: int) -> int:
		if n < 2: # Базовый случай
				return n
		# Рекурсивный случай
		return fib1(n - 1) + fib1(n - 2)

print('Fib + Auto Memize')
print(opt_fib(5))
print(opt_fib(50))
print('---------------------------')