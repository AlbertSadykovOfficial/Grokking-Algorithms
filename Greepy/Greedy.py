"""
		
		Жадные алгоритмы

			Жадные алгоритмы просты, на каждом шаге они выбирают оптимальный вариант
				Задача о расписание: 
					Как составить оптимальное расписание, 
					чтобы получилось посетить больше ПОЛНЫХ уроков,
					некоторые уоки накладываются друг на друга
				Решение:
					Берем самый ранний урок, заканчваем его,
					идем снова на самый ранний к нам, закначиваем и т.д.
				Итог:
					Просто, но по другому не работает

			Жадные алгоритмы не всегда хорошо работают и иногда дают неидельное решение
				Задача о рюкзаке:
					У рюкзака есть некий объем, в него не влезет все подряд.
					Мы берем первый самый дорогой товар в магазине (X), он занимает весь рюкзак,
					Но мы можем взять 2 товара по отдельности меньшей стоимости, чем X, 
					но в сумме (Y+Z) дадут большую стоимость,чем X и поместятся в рюкзак
				Вывод:
					Жадные алгоритмы иногда дают приближенное решение 

"""