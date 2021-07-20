"""

		Задача раскарски карты (Австралии)

				Постановка:

						Можно ли раскрасить карту Автралии всего 3 разными цветами
						при условии, что 2 соседие области не могут иметь одинаковый цвет

				Ответ:

						Да				

"""
"""

		Данная задача относится к классу задач с ограничением
		
		Чтобы решить задачу методом CSP НУЖНО:
				1) Определить переменые
				2) Определить области определния
				3) Определить ограничения

		Тогда:

				1) Переменные - 7 регионов
				2) Область определения - 3 разных цвета
				3) Ограничения - (двоичное ограничение -> каждые 2 области A<=>B не могут иметь одинаковый цвет)


				Ограничение обработаем в конструкторе класс MapColoringConstraint, 
				который будет принимать 2 области, имеющие общую границу.
				Переопределенный метод satisfied проверит присвоены ли областям значения цвета,
				Если цвета не присовены, то ограничение считается выполненным до присовения цвета.

				Класс не универсален с точки зрения аннотации типа,
				но он является подклассом, параметризованным подклассом Constraint, с ипом str.
"""
from csp import Constraint, CSP
from typing import Dict, List, Optional

class MapColoringConstraint(Constraint[str, str]):
		def __init__(self, place1: str, place2: str) -> None:
				super().__init__([place1, place2])
				self.place1: str = place1
				self.place2: str = place2

		# Проверяем есть ли цвет у какого-либо региона, 
		# нет - все ок
		# есть у обоих - проверяем не равны ли они.
		def satisfied(self, assignment: Dict[str, str]) -> bool:
				if self.place1 not in assignment or self.place2 not in assignment:
						return True
				return assignment[self.place1] != assignment[self.place2]


if __name__ == "__main__":
 		variables: List[str] = ["Western Australia", "Northern Territory", 
 														"South Australia", "Queensland",
 														"New South Wales", "Victoria",
 														"Tasmania"]
 		domains: Dict[str, List[str]] = {}
 		for variable in variables:
 				domains[variable] = ["red", "green", "blue"]
 		csp: CSP[str, str] = CSP(variables, domains)

 		csp.add_constraint(MapColoringConstraint("Western Australia", "Northern Territory"))
 		csp.add_constraint(MapColoringConstraint("Western Australia", "South Australia"		))
 		csp.add_constraint(MapColoringConstraint("South Australia",		"Northern Territory"))
 		csp.add_constraint(MapColoringConstraint("Queensland", 				"Northern Territory"))
 		csp.add_constraint(MapColoringConstraint("Queensland", 				"South Australia"		))
 		csp.add_constraint(MapColoringConstraint("Queensland", 				"New South Wales"		))
 		csp.add_constraint(MapColoringConstraint("New South Wales", 	"South Australia"		))
 		csp.add_constraint(MapColoringConstraint("Victoria", 					"South Australia"		))
 		csp.add_constraint(MapColoringConstraint("Victoria", 					"New South Wales"		))
 		csp.add_constraint(MapColoringConstraint("Victoria", 					"Tasmania"					))

 		solution: Optional[Dict[str, str]] = csp.backtracking_search()
 		if solution is None:
 				print("No solution found")
 		else:
 				print(solution)