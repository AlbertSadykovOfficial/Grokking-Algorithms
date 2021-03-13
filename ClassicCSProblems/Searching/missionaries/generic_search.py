from __future__ import annotations # Позволять объектам Node ссылаться на самих себя
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

# Органиуем стек (ДЛЯ DFS)
class Stack(Generic[T]):
		def __init__(self) -> None:
				self._container: List[T] = []

		@property
		def empty(self) -> bool:
				return not self._container # Не равно True для пустого контейнера

		def push(self, item: T) -> None:
				self._container.append(item)

		def pop(self) -> T:
				return self._container.pop() # LIFO

		def __repr__(self) -> str:
				return repr(self._container)

# Органиуем очередь (ДЛЯ BFS)
class Queue(Generic[T]):
		def __init__(self) -> None:
				self._container: Deque[T] = Deque()

		@property
		def empty(self) -> bool:
				return not self._container # Не равно True для пустого контейнера

		def push(self, item: T) -> None:
				self._container.append(item)

		def pop(self) -> T:
				return self._container.popleft() # FIFO

		def __repr__(self) -> str:
				return repr(self._container)


# Приоритетная очередь для алгоритма A*
# 
#	Чтобы определить приоритет одного эл-та относительно другого
# в heappush и heappop выполняется сравнени с помощью </
# Для этого нужен метод __lt__() в Node.

class PriorityQueue(Generic[T]):
		def __init__(self) -> None:
				self._container: List[T] = []

		@property
		def empty(self) -> bool:
				return not self._container # Не равно True для пустого контейнера

		def push(self, item: T) -> None:
				heappush(self._container, item) # Поместить в очеред по приоритету

		def pop(self) -> T:
				return heappop(self._container) # Изввлечь по приоритету

		def __repr__(self) -> str:
				return repr(self._container)

# Тип Optional указывает, что переменная может ссылаться на значение параметризованного типа
class Node(Generic[T]):
		def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
				self.state: T = state
				self.parent: Optional[Node] = parent
				self.cost: float = cost
				self.heuristic: float = heuristic

		def __lt__(self, other: Node) -> bool:
				return (self.cost + self.heuristic) < (other.cost + other.heuristic)


# Поиск в глубину
# При успешном завершении возвращается Node, в котором искомое состояние
def dfs(initial: T, finish_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
		# То, что нужно проверить
		frontier: Stack[Node[T]] = Stack()
		frontier.push(Node(initial, None))
		# Места, где мы уже были
		explored: Set[T] = {initial}

		while not frontier.empty:
				current_node: Node[T] = frontier.pop()
				current_state: T = current_node.state
				# При нахождении искомой точки завершаем
				if finish_test(current_state):
						return current_node
				# Проверям куда дальше идти и что мы еще не исследовали
				for child in successors(current_state):
						if child in explored:
								continue
						explored.add(child)
						frontier.push(Node(child, current_node))
		return None


# Поиск в Ширину
# При успешном завершении возвращается Node, в котором искомое состояние
def bfs(initial: T, finish_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
		# То, что нужно проверить
		frontier: Queue[Node[T]] = Queue()
		frontier.push(Node(initial, None))
		# Места, где мы уже были
		explored: Set[T] = {initial}

		while not frontier.empty:
				current_node: Node[T] = frontier.pop()
				current_state: T = current_node.state
				# При нахождении искомой точки завершаем
				if finish_test(current_state):
						return current_node
				# Проверям куда дальше идти и что мы еще не исследовали
				for child in successors(current_state):
						if child in explored:
								continue
						explored.add(child)
						frontier.push(Node(child, current_node))
		return None

def astar(initial: T, finish_test: Callable[[T], bool], successors: Callable[[T], List[T]], heuristic: Callable[[T], float]) -> Optional[Node[T]]:
		# То, что нужно проверить
		frontier: PriorityQueue[Node[T]] = PriorityQueue()
		frontier.push(Node(initial, None, 0.0, heuristic(initial)))
		# Места, где мы уже были (смотрели)
		explored: Dict[T, float] = {initial: 0.0}

		while not frontier.empty:
				current_node: Node[T] = frontier.pop()
				current_state: T = current_node.state
				# При нахождении искомой точки завершаем
				if finish_test(current_state):
						return current_node
				# Проверям куда дальше идти и что мы еще не исследовали
				for child in successors(current_state):
						# Выставляем - 1 для сетки
						# Для сложных прилоений тут должна быть функция
						new_cost: float = current_node.cost + 1
						
						if child not in explored or explored[child] > new_cost:		
								explored[child] = new_cost
								frontier.push(Node(child, current_node, new_cost, heuristic(child)))
		return None

# Восcтанавливаем путь от начала до целевой точки
# (Двигаемся от Node к его предкам через parent)
def node_to_path(node: Node[T]) -> List[T]:
		path: List[T] = [node.state]
		# Двигаемся назад
		while node.parent is not None:
				node = node.parent
				path.append(node.state)
		path.reverse()
		return path


def euclidean_distance(finish: MazeLocation) -> Callable[[MazeLocation], float]:
		def distance(ml: MazeLocation) -> float:
				xdist: int = ml.column - ginish.column
				ydist: int = ml.row - finish.row
				return sqrt((xdist*xdist) + (ydist*ydist))
		return distance

def manhattan_distance(finish: MazeLocation) -> Callable[[MazeLocation], float]:
		def distance(ml: MazeLocation) -> float:
				xdist: int = ml.column - finish.column
				ydist: int = ml.row - finish.row
				return (xdist + ydist)
		return distance

if __name__ == "__main__":
		print(linear_contains([1, 5, 15, 15, 15, 20], 5))
		print(binary_contains(["a", "d", "e", "f", "z"], "f"))
		print(binary_contains(["Andy", "Enny", "Roland", "Yen", "Zack"], "wolf"))
