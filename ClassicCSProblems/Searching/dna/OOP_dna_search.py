from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
		for item in iterable:
				if item == key:
						return True
		return False

# Comparable - Тип, реализующий операции сравнения
C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
		def __eq__(self, other: Any) -> bool:
			...

		def __lt__(self: C, other: C) -> bool:
			...

		def __gt__(self: C, other: C) -> bool:
				return (not self < other) and self != other

		def __le__(self: C, other: C) -> bool:
				return self < other or self == other

		def __ge__(self: C, other: C) -> bool:
				return not self < other

		def binary_contains(sequence: Sequence[C], key: C) -> bool:
				left: int = 0
				right: int = len(sequence) - 1
				while left <= right: # Пока есть что искать
						middle: int = (left + right) // 2
						if sequence[middle] < key:
								left = middle + 1
						elif sequence[middle] > key:
								right = middle - 1
						else:
								return True
				return False

if __name__ == "__main__":
		print(linear_contains([1, 5, 15, 15, 15, 20], 5))
		print(binary_contains(["a", "d", "e", "f", "z"], "f"))
		print(binary_contains(["Andy", "Enny", "Roland", "Yen", "Zack"], "wolf"))
