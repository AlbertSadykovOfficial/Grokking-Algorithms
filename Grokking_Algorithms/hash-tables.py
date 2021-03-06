"""
	Хэш-таблицы (по-другому: словари)
		Скорость: O(1)

	Хэш-функция - функция, которая получает на вход одни данные(строки), возвращает число. (md5, SHA)
		Идеальные свойства (не всегда выполнимы):
			- Последовательность (при передаче одного и того же значение на вход, получаем одно и то же на выходе)
			- Разным словам должны соответствовать разные числа
			- Равномерный закон распределения
		
		Последствия:
			- Функция свзяывает одно название с одним индексом
			- Функция связыввает разные строки с разными индексами
			- Функция должна знать размер массива и возвращать только действительные индексы.
	
	Хэш-функция + Массив = Хэш таблицы.

	Хэш-таблицы очень быстрые (для поиска, вставки и удаления) и вот почему:
		Хэш-таблицы используют для хранения данных массивы, а скорость доступа к определеннму
		элементу массива моментальна. Мы используем Хэш-функцию, чтобы от входного значения
		(строки) получить индекс как раз этого массива, где хранятся нужые нам данные.
		Получается, что скорость доступа зависит от скорости работы хэш-функции и скорости 
		доступа к элементу, т.к. эти скорости явл +-постоянными, то скорость доступа к значению
		Хэш-таблиц: O(1).

		Состав: Ключ + Значение

	Подходять для:
		1) Моделирования отношений между объектами
		2) устранение дуюликатов
		3) кэширование, запоминание данных вместо их рассчета

	Используют:
		1) В Телефонных книгах (Albert Einstein -> 777 777 7777)
		2) В DNS для отображения Названия сайта на его ip (google.com -> 74.125.239.133)
		3) Использование в кэше (чтобы не выполнять повторный пересчет частых запросов, лучше поместить их в кэш)


	Коллизии
		Допустим, Хэш-функция назначает ключи по первой букве строки переданной на вход,
		Тогда, если подать на вход 2 слова, начинающиеся, к примеру, на А (Арбуз, Авокадо),
		То Авакадо запишется поверх Арбуза - это и есть коллизия.

		Простой, но не быстрый способ выхода из этой ситуации создавать связный список на этот
		элемент Хэш-таблицы.

		Если таких совпадений будет не много, то скорость сильно не упадет, но если их будет много,
		то эторавноценно хранению в связном списке и скорость поиска там будет O(n). Это еще раз 
		доказывает важность выбора Хэш-функций.

		Для предотвращения коллизий необходимы:
			- Низкий коэффициент заполнения (<0.7) - Отношение кол-ва (существ. эл-в) к (общему числу) эл-в в таблице
			- Хорошая хэш-функция

"""

# Создать Хэш-функцию (словарь)
	book = dict()
	newspapers = {}

# Добавить элемент
	book['Atlantida'] = 0.67
	book['Tom Soyer'] = 1.49

# Доступ
	print(book['Atlantida'])

"""
	Исключение дубликатов
		
		Используется на выборах, чтоюы человек не проголосовал дважды
"""

voted = {}
def check_voter(name):
	if voted.get(name):
		print "Вы уже голосовали"
	else:
		voted[name] = True
		print "ВЫ можете голосовать"


"""
	Использование в кэше

"""
cache = {}
def get_page(url):
	if cache.get(url):
		return cache[url]
	else:
		# Выполняем поиск страницы, если ее нет в кэше
		data = get_data_from_server(url)
		cache[url] = data
		return data