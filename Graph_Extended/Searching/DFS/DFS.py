"""

		Поиск в глубину (DFS)

		Поиск в глубину - алгоритм разведования по самой последней обнаруженной вершине
		и с отступление по необходимости.

		DFS можно реализовать через BFS, внеся 2 изменения:
			1) Подставить СТЕК вместо ОЧЕРЕДИ
			2) Отложить проверу того была ли вершина разведана только плсе ее удаления

		ПСЕВДОКОД:
			
			1. Итеративная реализация DFS
				Вход: граф G=(V,E) в виде списка смежности и вершина s->V

				1. Пометить все вершины как неразведанные
				2. S:= стек, инициализированный вершиной s
				3. while S не является пустым do
				3.1		удалить вершину v из головы стека S
				3.2		if v не разведана then
				3.2.1			пометить v как разведанную
				3.2.2			for каждое ребро (v,w) в списке смежности вершины v do
				3.2.2.1				добавить w в голов стека S

			2. Рекурсивная реализация DFS
				Вход: граф G=(V,E) в виде списка смежности и вершина s->V

				function ():
						for каждое ребро (s,v) в списке смежности вершины s do
								if v не разведана then
										DFS(G,v)

				Алгоритм сразу выпоняет рекурсию на первом неразведанном соседе,
				и только потом рассматривает оставшихся соседей.


			Пример работы итеративной реализации:

						a			  e		
					/   \   /  
				s       c   |
					\   /   \
						b 	_		d

				ПЕРВАЯ ИТЕРАЦИЯ (while): 	
					1) Извлекаем s из Q. 
					2) Помещаем a и b в СТЕК
					S = [a,b]
				ВТОРАЯ ИТЕРАЦИЯ (while):
					1) Извлекаем первый элемент стека - a
					2) Помещаем s и с в СТЕК:
					S = [s,c,b]
				ТРЕТЬЯ ИТЕРАЦИЯ (while):
					1) Извлекаем первый элемент стека - s
					2) Он уже помечен как разведанный, выталкиваем его
					S = [c,b]
				ЧЕТВЕРТАЯ ИТЕРАЦИЯ (while):
					1) Извлекаем первый элемент стека - c
					2) Помещаем всех его соседей - a,b,d,e в СТЕК
					S = [a,b,d,e,b]
				ПЯТАЯ ИТЕРАЦИЯ (while)
					1) Извлекаем первый элемент стека - a
					2) Он уже помечен как разведанный, выталкиваем его
					S = [b,d,e,b]
				ШЕТСАЯ ИТЕРАЦИЯ (while)
					1) Извлекаем первый элемент стека - b
					2) Помещаем s, c, d в СТЕК
					S = [s, c, d, b, d, r, b]
				СЕДЬМАЯ, ВОСЬМАЯ ИТЕРАЦИЯ (while)
					1) Выталкиваем s, c из стека
					S = [d, b, d, r, b]
				ДЕВЯТАЯ ИТЕРАЦИЯ (while)
					1) Извлекаем первый элемент стека - d
					2) Помещаем c, d, e в СТЕК
					S = [c, d, e, d, b, d, r, b]
				C, D ,E - уже разведаны - пропускаем их
				Разведаем e
				d, b, d, r, b - уже разведаны, пропускаем их
				СТЕК становится пустым, программа завершается.

"""