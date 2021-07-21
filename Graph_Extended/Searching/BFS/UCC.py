"""

	Вычисление связных компонент (UCC)
		
		Для НЕориентрванных графов.
		Цель: Применение BFS для нахождения связных компонентов. 

		Связный компонент - набор вершин связанных вместе в пределе графа.

		Пример:
						u					           t
					/   \     x----y      / \
				s   |   w 						 /   \
					\   /       				o			j
						v
			Связные компоненты:
			1) {s,u,w,v}
			2) {x,y}
			3) {o,t,j}

		
		Где применяется:
			1) Обнаружение сетевых сбоев
			2) Кластеризация - объединене объектов в классы


		Алгоритм UCC
			В сонове алгоритма UCC лежит BFS и основная идея заключается в том, чтобы 
			поместить в цикл обхода каждой вершины попрограмму BFS, так, каждой вершине
			будет присвоен номер своего класса. В конце, когда последний элемент получит
			номер, этот номер и будет является количеством классов в нашем Графе.

			ПСЕВДОКОД:
					Пометить все вершины как неразвданные
					numCC := 0
					for i:= от 1 до n do 				// Перебрать все вершины
							if i не разведана then  // Избежать избыточности
								numCC:=numCC + 1 			// Новая компонента
					BFS:	Q:= очередь, инициализированная ЗНАЧЕНИЕМ i
								While Q не является пустой do:
										Удалить вершину i из начала очереди, назвать ее v
										сс(v):= numCC
										for каждое ребро (v,w) в списке смежности v do
												if w не разведана then
														пометить w как разведанную
														добавить w в конец Q

			Пример:

				 1	-	 3			            6
					\   /      2----4      / \
				    5     						  /   \
					/   \         			 8		10
				 7		 9
			
			1) Помечаем все вершины как неразвеанные

			ПЕРВАЯ ИТЕРАЦИЯ (внешний for):
				1) Т.к. цикл начинается с 1, то мы вибираем вершину 1.
				2) Вызываем подпрограмму BFS
				3) Получаем {1,3,5,7,9}
				4) Устанавливаем их значение cc = 1
			ВТОРАЯ ИТЕРАЦИЯ (внешний for):
				1) Следующая идет вершина 2.
				2) Вызываем подпрограмму BFS
				3) Получаем {2,4}
				4) Устанавливаем их значение cc = 2
			ТРЕТЬЯ ИТЕРАЦИЯ (внешний for):
				1) Следующая идет вершина 3.
				2) Мы встречали эту вершину (if)
				3) Пропускаем
			ЧЕТВЕРТАЯ ИТЕРАЦИЯ как ТРЕТЬЯ
			ПЯТАЯ ИТЕРАЦИЯ как ТРЕТЬЯ
			ШЕСТАЯ ИТЕРАЦИЯ (внешний for):
				1) Берем вершину 6
				2) Вызывается подпрограмма BFS со стартовой вершиной 6
				3) Получаем {6,8,10}
				4) Устанавливаем их значение cc = 3
			ОСТАЛЬНЫЕ итерации натыкаются на вершины, которы уже разведаны,
			Алгоритм завершается
"""