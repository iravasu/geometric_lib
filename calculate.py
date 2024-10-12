# Импорт модулей для работы с кругом и квадратом
import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

# Функция для вычисления указанной функции для фигуры
def calc(fig, func, size):
	#Вычисление функции для фигуры на основе ее размера.

	 # Проверка корректности входных данных
	assert fig in figs
	assert func in funcs

	# Выполнение вычисления и вывод результата
	result = eval(f'{fig}.{func}(*{size})')
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	# Ввод фигуры, функции и размеров с проверками
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size) # Вычисление и вывод результата

	  # Пример вызова: вычисление периметра круга с радиусом 5
    # calc('circle', 'perimeter', [5])  # Результат: perimeter of circle is 31.41592653589793

    # Пример вызова: вычисление площади квадрата со стороной 4
    # calc('square', 'area', [4])  # Результат: area of square is 16



