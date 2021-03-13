from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
# 
from generic_search import dfs, bfs, node_to_path, Node, astar, manhattan_distance

# Перечисление значений str
class Cell(str, Enum):
	EMPTY = " "
	BLOCKED = "X"
	START = "S"
	FINISH = "F"
	PATH = "*"

# Точка в лабиринте
class MazeLocation(NamedTuple):
		row: int
		column: int

# Создать случайный лабиринт
#
# sparseness - коэффицинт заполнения лабиринта
# (У нас как бы не лабиринт, а минное поле получаестя )
class Maze:
		def __init__(self, \
								 rows: int = 10, columns: int = 10, \
								 sparseness: float = 0.2, \
								 start: MazeLocation = MazeLocation(0,0), \
								 finish: MazeLocation = MazeLocation(9,9) \
								 ) -> None:

				self._rows: int = rows
				self._columns: int = columns
				self.start: int = start
				self.finish: int = finish
				self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
				self._randomly_fill(rows, columns, sparseness)
				# Заполняем ячейки начала и конца спец символами
				self._grid[start.row][start.column] = Cell.START
				self._grid[finish.row][finish.column] = Cell.FINISH

		def _randomly_fill(self, rows: int, columns: int, sparseness: float):
				for row in range(rows):
						for column in range(columns):
								if random.uniform(0, 1.0) < sparseness:
										self._grid[row][column] = Cell.BLOCKED

		# Проверка:
		# ЯЧЕЙКА - финиш ИЛИ НЕТ?
		def finish_test(self, ml: MazeLocation) -> bool:
				return ml == self.finish

		# ПЕРЕДВИЖЕНИЕ:
		# Проверка на корректность следующей ячейки
		def successors(self, ml: MazeLocation) -> List[MazeLocation]:
				locations: List[MazeLocation] = []
				if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
						locations.append(MazeLocation(ml.row + 1, ml.column))
				if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
						locations.append(MazeLocation(ml.row - 1, ml.column))
				if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
						locations.append(MazeLocation(ml.row, ml.column + 1))
				if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1]  != Cell.BLOCKED:
						locations.append(MazeLocation(ml.row, ml.column -1))
				return locations

		# Отмечаем успешный путь
		def mark(self, path: List[MazeLocation]):
				for maze_location in path:
						self._grid[maze_location.row][maze_location.column] = Cell.PATH
				self._grid[self.start.row][self.start.column] = Cell.START
				self._grid[self.finish.row][self.finish.column] = Cell.FINISH

		# Очищаем путь
		def clear(self, path: List[MazeLocation]):
				for maze_location in path:
						self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
				self._grid[self.start.row][self.start.column] = Cell.START
				self._grid[self.finish.row][self.finish.column] = Cell.FINISH

		# Выводим наш лабиринт
		# 
		# Разбор конструкции:
		# join([c.value for c in row])
		#
		# Тут вопреки логике все идет слева направо:
		# c.value <-- c <-- row
		# 
		def __str__(self) -> str:
				output: str = ""
				for row in self._grid:
						output += "".join([c.value for c in row]) + "\n"
				return output


if __name__ == "__main__":
		maze: Maze = Maze()
		print(maze)
		solution1: Optional[Node[MazeLocation]] = dfs(maze.start, maze.finish_test, maze.successors)
		if solution1 is None:
				print("No solution found using DFS")
		else:
				path1: List[MazeLocation] = node_to_path(solution1)
				maze.mark(path1)
				print(maze)
				maze.clear(path1)

		solution2: Optional[Node[MazeLocation]] = bfs(maze.start, maze.finish_test, maze.successors)
		if solution2 is None:
				print("No solution found using BFS")
		else:
				path2: List[MazeLocation] = node_to_path(solution2)
				maze.mark(path2)
				print(maze)
				maze.clear(path2)

		distance: Callable[[MazeLocation], float] = manhattan_distance(maze.finish)
		solution3: Optional[Node[MazeLocation]] = astar(maze.start, maze.finish_test, maze.successors, distance)
		if solution3 is None:
				print("No solution found using BFS")
		else:
				path3: List[MazeLocation] = node_to_path(solution3)
				maze.mark(path3)
				print(maze)
				maze.clear(path3)					
