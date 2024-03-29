"""
		
		Сильно связные копмпоненты (strongly connected component, SCC)

			Связный компонент (в ориент. случае) - макисмальная область в пределах которой
			мы можем добраться из какого-либо места в другое.
			
			Сильно связная компонента (ориент. графа) - максимальное подмножество S->V вершин,
			так что существует ориентированнй путь из любой вершины S в любую другую вершину S.

			Пример:

			Не связная компонента:					Связная компонента:
					 -> v ->												<- v <-
					/ 	 		\											 / 	 		 \
				 s         t 										s         t
					\ 			/ 										 \ 			 /
					 -> w -> 												-> w ->
			
			Утверждение:
				Метаграф сильно связных компонент является ориентированным ациклическим графом.
"""