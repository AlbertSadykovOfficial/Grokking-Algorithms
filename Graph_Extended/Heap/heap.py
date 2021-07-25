"""

		Куча

			Куча - структура данных, которая отслеживает множество объектов с ключами
			и может быстро идентифицировать объект с наименьшим ключом.

-------------------------------------------------------------------------------------
			КОГДА ИСПОЛЬЗОВАТЬ:
					КУЧУ стоит использовать, когда нужно производить 
					ТОЛЬКО операциии вычисления min или max 
					для ДИНАМИЧЕСКИ изменяющихся множеств
-------------------------------------------------------------------------------------

			Куча имеет структура данных типа бинарного дерево (binary heap).
			
			Пример:
				Ключ - ID сотрудника
				Объект - запись о сотруднике

				Так же это может быть ребра графа, где ключи - длины ребер.
				Так же это может быть запланированное на будущее событие, 
				где ключ - указывает на время,в которое событие произойдет.
		
			Самые важные вещи, которые нужно знать о любой структуре данных,
				1) Какие она выполняет операции
				2) Время выполнения операции 


			ПОДДЕРЖИВАЕМЫЕ ОПЕРАЦИИ И ВРЕМЯ их выполнения:
				______________________________________
				| Операция				| Время выполнения	|
				|-------------------------------------|
				| Вставить				|			O(log(n))			|
				| Извлечь min			|			O(log(n))			|
				|-------------------------------------|
				| Найти min				|				O(1)				|
				| Объедин. в кучу	|				O(n)				|
				| Удалить					|			O(log(n))			|
				|_____________________________________|
				
				НАЙТИ МИНИМУМ:
					Операция найти минимум может быть реализована так:
						1й Вариант (на тривиальных функциях) -> O(log(n))
							1) Извлекаем минимум
							2) Втавляем 

						2й Вариант (часто реализация поддреживает сразу эту функцию)
							1) Найти минимум (за время O(1))
				
				Вывод:
					КУЧУ стоит использовать, когда нужно производить операциии вычисления min или max 
					для динамически изменяющихся множеств

			ПРИМЕНЕНИЯ:

				1) Сортировка O(n*log(n))
				2) Событийный менеджер (O(log(n)))
				3) Поддержка медианы (O(log(i)), в каждом раунде i)

					 
"""