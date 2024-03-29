"""

	Фильтры Блума

			Фильтры Блума - близки родственники хэш-таблиц.

			Их основная особенность в том, что они компактны,
			но при этом могут допускать ошибки.

			Фильтры Блума vs Хэш-таблицы:
				+ Занимает меньше места
				+ Гарантирует выполнени операций за постоянное время
				- Не может хранить указатели на объект
				- Более сложные удаления (в сравнении с хэш-таблицей со сцеплением)
				- Есть вероятность ошибки (ложного утверждения)

-------------------------------------------------------------------------------------
			КОГДА ИСПОЛЬЗОВАТЬ:
				Если требуется быстрый поиск с динамически-изменяющимся множеством объектов,
				пространство ценится на вес золота и является приемлимым малове число ложных 
				утверждений.
-------------------------------------------------------------------------------------

		Применения:
				1) Spellcheckers
				2) Запрещенные пароли
					 (Запрещенные пароли помещаются в фильтр Блума,
					 Если пользователь ввел запрещенный пароль, то фильртр вернет 1,
					 что сообщит пользователю о том, что нужно изменить пароль, 
					 Если он ввел хороший пароль, система вернет 0, 
					 что сообщит о том, что пароль принят)
				3) Интернет-маршрутизаторы
						(Найти содержится ли IP-адрес в стеке заблокированных адресов -> 1-Да, 0-Нет)
						(Вести статистику для обнаружения DDOS атак)

		Реализация:

				Вставить по ключу (k):

					for i=1 to m do
							A[hi(k)] = 1

					Пример:
						Если m = 3 и h1(k) = 23, h2(k) = 17, h3(k) = 5
						ТО биты {5,17,23} устанавливаются в 1.

				Просмотр по ключу (k):

					for i=1 to m do
							if A[hi(k)] = 0 then
									return "нет"
					return "да"

					Пример:
					__________________________________________________
					| Ключи	|	Значение h1	| Значение h2	| Значение h3	|
					|-----------------------------------|-------------|
					| k1		|			 5			|			 48	 		|				12		|
					| k2		|			37			|			  8	 		|				17		|
					| k3		|			32			|			 23	 		|				2	 		|			
					| kx		|			23			|			 17	 		|				5			|		
					|_______|_____________|_____________|_____________|

					Допустим, мы вставили {k1, k2, k3} в фильтр Блума,
					эти 3 вставки установят 9 бит в единицу.
					Как можно заметить эти 9 бит перекрывают и значения kx,
					которые мы не вставляли в фильтр Блума.
					Если мы сейчас обратимся к фильтру с целью проверки kx, 
					то получим положительный ответ, хотя мы его туда не вносили.

					Это и порождает ложные утверждения в фильтрах Блума. 
"""