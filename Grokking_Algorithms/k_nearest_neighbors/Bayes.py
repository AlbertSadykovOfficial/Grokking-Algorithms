"""

	Классификатор Байеса

		Классификатор требует предварительную треннировку на данных,

		Пример:

		На почту приходят сообщения, некотоыре из них - SPAM, 
		чтобы опредлить спам и это предложение разбивают на слова,
		затем слова проверяются на наличие совпадений с типичными
		словами - спамами (Миллион, Выиграли, Сообщите пароль)...

		Иногда в спам может улететь и ценная информация, потому что
		эти слова или фразы могут встретится и в нормальном сообщении

"""