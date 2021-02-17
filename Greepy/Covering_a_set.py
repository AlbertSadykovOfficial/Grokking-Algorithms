"""
	
		Задача о покрытии множества

		Надо, чтобы все шататы (50шт) вещали вашу радио-программу,
		при этом надо использовать минимальное кол-во радиостанций, потому что они стоят денег.
		Разные станции могут иметь смежные площади.

		Найти: Минимальное кол-во станций + эти станции, покрыающие всю нужную территорию

			Вариант решения:
				1)  Составить список всех возможных подмножеств станций (степенное множество)
						В нем содержатся 2^n возможных подмножеств
				2)	Из этого списка выбирается множество с наименьшим набором станций, покрывающих 50 штатов

				!!! Проблема:
					Вычислеие всех подмножеств займет много времени
					Скорость: O(2^n)
					При 5, 10 станциях это +- ок, но 2^50 (35,7 млн вычислений) слишком много   
				
				Решение --> Жадные алгоритмы
			
			Вариант решения через Жадный (приближенный) алгоритм:
				1) Выбрать станцию, покрывающую наибольшее кол-во штатов, еще не вошедших в покрытие,
					 Если станция покрывает штаты, взодящие в покрытие, это ормально
				2) Повторять, пока остаются штаты, не входящие в покрытие

				Алгоритм не совсем точный, но намного быстрее
"""

# Программная реализация

# Множество штатов
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# Составим множества, где ключи-станции, значения-штаты, которые покрываются станцией
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"]= set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# Итоговый набор станций
final_stations = set()


# Множество - структура данных, не содержащая дубликатов
while states_needed:
	best_station = None # Станция, обслуживающая больше всего штатов, не входящих в текущее покрытие
	states_covered = set() # Все штаты, обслуживаемые этой станцией, еоторые еще не входят в текущее покрытие.
	for station, states in stations.items(): # 3 перебирает все станции и находит наилучшую
		covered = states_needed & states 			 # Пересечение множеств (Множество штатов не входящих в покрытие)
		if len(covered) > len(states_covered): # Покрывает ли эта стацния больше штатов, чем текущая
			best_station = station
			states_covered = covered
			states_needed -= states_covered      # Штаты, которые уже обслуживаются станцией не требуются для последующего подбора
			final_stations.add(best_station)

print(final_stations)