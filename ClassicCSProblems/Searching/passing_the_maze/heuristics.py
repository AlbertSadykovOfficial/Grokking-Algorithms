"""

		
		Эвристика - интуитивноепредставление о том, как решить задачу.


		Евклидово расстояние - расстояние по прямой до объекта,
		находится по теореме пифагора,

		Манхэттенское расстояние - расстояние по горизонтали + вертикали.

"""

def euclidean_distance(finish: MazeLocation) -> Callable[[MazeLocation], float]:
		def distance(ml: MazeLocation) -> float:
				xdist: int = ml.column - ginish.column
				ydist: int = ml.row - finish.row
				return sqrt((xdist*xdist) + (ydist*ydist))
		return distance

def manhattan_distance(finish: MazeLocation) -> Callable[[MazeLocation], float]:
		def distance(ml: MazeLocation) -> float:
				xdist: int = ml.column - ginish.column
				ydist: int = ml.row - finish.row
				return (xdist + ydist)
		return distance