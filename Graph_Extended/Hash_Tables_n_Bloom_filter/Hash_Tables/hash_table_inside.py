"""

	Реализация хэш-таблицы (на высоком уровне)

		Важные понятия раздела:

				U - множество всех взможных ключей (все мозможные IP, сотояния шахматной доски)
				S - подмножество U (IP-адреса ваших серверов или IP тех, кто посещал страницу).


		Самые важные идеи реализации хэш-таблиц:

				1) Хэш-функции
				2) Коллизии и как с ними бороться


		Преимущества Хэш-таблицы над его аппонентами (сравнение):

				1) Массив - Да, доступ к элементу массива моментален O(1),
										Но чтобы хранить данные для каждого возможного ключа из U,
										массиву требуется размер равный пространству U! 
										(потому что массивы не динамичны)
				2) Связный список - Связный список диамичен в отношении пространства,
														для каждых S объектов он будет хранить S ключей,
														но время выполнения операций УДАЛИТЬ И ПРОСМОТРЕТЬ
														масштабируется линейно размеру, т.е O(S).
				3) Хэш-таблицы - объединяют все лучшее у связных списов и массивов,
												 они имеют пропорциональное простарнство и 
												 постоянно-временные операции.  

					__________________________________________________
					| Стуркутра данных	|	Пространство	| Просмотреть	|
					|-----------------------------------|-------------|
					| Массив						|			Q|U|			|			Q(1)		|
					| Связный список		|			Q|S|			|			Q|S|		|
					| Хэш-таблица				|			Q|S|			|			Q(1)*		|			
					|___________________|_______________|_____________|
					
						O()* - с оговоркой, что таблица реализована должны образом,
					 т.е хорошая хэш-функция и размер таблицы 

				Для достижения таких резульаьах хэш-таблица имитирует решение на основе массива,
				но с длиной массива n=|S|, а не |U|. 
				!!! ДА, можество S Периодически меняется со временем, поэтому мы должны периодически
						менять размер массива так, чтобы го длина была пропорциональна S. 


		ЗАГРУЗКА Хэш-таблицы:

											  				Число хранимых объектов
				загрузка хэш-таблицы = --------------------------
											 							Длина n массива

				Так, в таблице со сцеплением загрузка показывает среднюю популяциюв 1 из карзин
				В таблице с открытой адресацией - показывает при умнож. на 100 непосредственно % загрузки

				Управление загрузкой (!):
					
						Одним из самых простых способов является отслеживание уровня 70% загрузки.
						При достижении уровня (70%), следует удвоить число n корзин, после чего все объекты
						хешируются в новую, более крупную хэш-таблицу (с загрузкой уже 35%).

						Если же загрузка понижается, то массив, конечно, следует уменьшить тоже.

		Хэш-функции:

				Хэш-функция - ф-ия, которая транслирует {Имя друзей, состояние доски} в позиции в хэш-таблице.
				Она отображает каждый взможный ключ из U в позицию {0,..,n-1}.
				При этом, если |U|>n, то два разных ключа будут отобрааться в одинаковую ячейку!

				h("Алиса") = 17, значит в позиции массива i=17 содержится информация об АЛИСЕ.
				Или: Строкове значение "Алиса" хэшируется в 17.
				

				ПАТОЛОГИЧЕСКИЕ СОВОКУПНОСТИ ДАННЫХ:
						
						Для каждо хэш-функции h: U->{0,1,...,n-1} 
						существует множество S ключей с размером |U|/n,
						таких что h(k1) = h(k2) для каждого k1,k2 принадлежащих S

				ЖЕЛАЕМЫЕ свойства ХЭШ-функции:
						1) Дешевая при оценивании, в идеале O(1)
						2) Простая при сохраннении, в идеале с пространством O(1)
						3) Имитирует случайную функцию, распределяя НЕпатлогческие наоры данных равномерно по таблице.

				Примеры функций:

						1) h(k) = k mod n 
								(многократное выитане n из k до момента, пока не будет целое число между 0 и n-1)
								Минусы: К примеру, n = 1000, 
									1) Если мы вычисляем оклады, которые кратны 1000, 
										 тогда остаток от деления будет равен 0 и все оклады будут помещены в 1 позицию->0
									2) Если цена автомобилей заканчивается на 999: 13 999$, тогда все остатки будут равны 999,
										 отображение сново произойдет на одну ячейку

						2) h(k) = (ak+b) mod n, где a и b - целые числа в {1,2,...,n-1}.
									Для правильно подобрнных a и b функция будет вполне пригодна и не будет иметь недостатков
									свойственных первой функации

		КАК ВЫБРАТЬ СВОЮ ХЭШ-ФУНКЦИЮ
				
				По ситуации, нужно тестировать, про хэш-функции стоит знать, что они делятся на виды:
						1) НЕкриптографические (MD5, FarmHash, MurmurHash3, SpookyHash)
						2) Криптографические (SHA-1, SHA-256) - предназначены для защиты от атак.
"""