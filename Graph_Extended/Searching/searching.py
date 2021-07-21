"""

	Поиск в графе и его применения

			Зачем нужно выплнять поиск в графе или вяснять содержит ли граф путь из точки A в B илинет?

				1) Проверка связности - проверка моно ли пройти из точки A в точку B
				2) Кратчайшие пути - узнать путь, который использует наименьшее число ребер или длину.
				3) Планирование - Построение пследовательности решений (если сущ. связные компоненты вытек. друг из друга)
				4) Связные компоненты - выделение отдельных групп Графа, которые не связаны между собой.

				Приведенные в этом разделе алгориты по скорости линейны и не будут превышать:
					O(n+m), где m-число связей, n-число вершин.

"""