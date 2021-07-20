"""

		Построение структуры для задач


				Основа для структуры - абстрактный базовый класс Constraint.
				Подклассы будут использовать класс Cnstraint как основу 
				и переопределять его методы.

				Класс - ограничение Constraint состоит из:
						переменных (variables), которое ОН ограничивает 
						метода satisfied(), который проверяет выполняетя ли ограничение
	
				Примечание:

						Абстрактные базовые классы играют роль шабонов, не стоит использовать их
						как иерархию классов для внуреннего примения.
						Их используют, чтобы строить структуры на основе которой будут создаваться
						друге классы.

"""	

from typing import Generic, TypeVar, Dict, List, Optional
#from abc import ABC
#from abc import abstractmethod
import abc

V = TypeVar('T') # тип variable для пременных
D = TypeVar('D') # тип domain для области определения

class Constraint(Generic[V, D], abc.ABC):
		# Переменные для которых существует ограничение
		def __init__(self, variables: List[V]) -> None:
				self.variables = variables

		# Шаблон, который необходимо переопределить
		@abc.abstractmethod
		def satisfied(self, assignment: Dict[V, D]) -> bool:
				...


# Класс CSP - ПЕРЕМЕННЫЕ, ОБЛАСТИ ОПРЕДЕЛЕНИЯ и ОГРАНИЧЕНИЯ
#
# Задача с ограничениями состоит из переменных ТИПА V,
# которые имеют диапазоны значений, известные как области определения ТИПА D
# И огрнаичений, которе оперделяют:
# Является ли допустимым выбор данной обл. опред. для данной переменной
#
# # variables - переменные, которое будут ограничены
# # domains  - домен каждой переменной
#
# Методы __init__() и add_constraint() имеют простейшую проверку ошибок
# Они вызывают иск., если variable отсутствует в обл. опередения
# или не существует constraint для несуществующей переменной.

class CSP(Generic[V, D]):
		def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
				self.variables: List[V] = variables
				self.domains: Dict[V, List[D]] = domains 
				self.constraints: Dict[V, List[Constraint[V,D]]] = {}
				for variable in self.variables:
						self.constraints[variable] = []
						if variable not in domains:
								raise LookupError("Every variable should have a domain assigned to it")

		# Посмотреть все переменные, к которым относится данное ограничение
		# + Добавить себя в cnstraint для каждой такой переменной
		def add_constraint(self, constraint: Constraint[V, D]) -> None:
				for variable in constraint.variables:
						if variable not in self.variables:
								raise LookupError("Variable in constraint not in CSP")
						else:
								self.constraints[variable].append(constraint)

		# Проверка всех ограничений для данной переменной
		def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
				for constraint in self.constraints[variable]:
						if not constraint.satisfied(assignment):
								return False
				return True

		def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V,D]]:
				# Базовый случай
				# Возвращаем первый валидный экземпляр
				if len(assignment) == len(self.variables):
					return assignment

				# Просматриваем все переменные CSP
				# Извлекаем первое значение
				unassigned: List[V] = [v for v in self.variables if v not in assignment]
				first: V = unassigned[0]
				
				# Присваиваем все возможные обл. определения в переменную
				for value in self.domains[first]:
						local_assignment = assignment.copy()
						local_assignment[first] = value
						# Если нновое присваивание в local_assignment согласуется со всеми ограничениями
						# продолжаем поиск для нового присваивания
						if self.consistent(first, local_assignment):
								result: Optional[Dict[V,D]] = self.backtracking_search(local_assignment)
								if result is not None:
									return result
						# Решение отсутствует
						return None
