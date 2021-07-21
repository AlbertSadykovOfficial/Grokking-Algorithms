"""

	Поиск в ширину (BFS)

		Поиск в ширину равзведывает граф слоями, в сторону от стартовой веришины.
		Для реализации алгоритма используется такая структура данных как очередь.

		Очередь -> "Первым вошел/первым вышел"

		Вход: граф G=(V,E) в виде списков смежности и вершина s->V.
		
		ПСЕВДОКОД:

			1) Пометить s как разведанную вершину, все остальные как неразведанные
			2) Q:= очередь, инициализированная вершиной s
			3) While Q не является пустой do:
			3.1		Удалить вершину v из начала очереди
			3.2		for каждое ребро (v,w) в списке смежности v do
			3.2.1 		if w не разведана then
			3.2.1.1				пометить w как разведанную
			3.2.1.2				добавить w в конец Q


			Пример:

						a			  e		
					/   \   /  
				s       c   |
					\   /   \
						b 	_		d

			Стартовая вершина - s.
			ПЕРВАЯ ИТЕРАЦИЯ (while): 	
				1) Извлекаем s из Q. 
				2) for проверяет ребра (s,a) и (s,b). 
				3) a и b не помечены как разведанные (if)
				4) Помечаем a и b как разведанные
				5) Добавляем их в очередь
				Q = [a,b]; (s - вышла из очереди)
			ВТОРАЯ ИТЕРАЦИЯ (while)
				1) Извлекаем a из Q. 
				2) for проверяет ребра (s,a) и (a,c). 
				3) Пропускаем (s)-оно помечено, (c) не помечено как разведанное (if)
				4) Помечаем (c) как разведанное
				5) Добавляем (c) в очередь
				Q = [b,c]; (a - вышла из очереди)
			ТРЕТЬЯ ИТЕРАЦИЯ (while)
				1) Извлекаем b из Q. 
				2) for проверяет ребра (s,b) и (b,c). 
				3) Пропускаем (s и c)-они помечены, (d) не помечено как разведанное (if)
				4) Помечаем (d) как разведанное
				5) Добавляем (d) в очередь
				Q = [c,d]; (b - вышла из очереди)
			ЧЕТВЕРТАЯ ИТЕРАЦИЯ (while):
				1) Извлекаем с из Q. 
				2) for проверяет ребра (a,c), (b,c), (c, d) 
				3) (e) не помечена как разведанная (if)
				4) Помечаем (e) как разведанную
				5) Добавляем (e) в очередь
				Q = [d,e]; (c - вышла из очереди)
			ПЯТАЯ И ШЕТСАЯ итерации извлекают d и e, все их соседи уже разведаны.
			Очередь становится пустой, агоритм останавливается.
"""