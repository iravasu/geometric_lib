import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    'circle-area': 1,
    'circle-perimeter': 1,
    'square-area': 1,
    'square-perimeter': 1,
    'triangle-area': 3,
    'triangle-perimeter': 3
}

def calc(fig, func, size):
    # Проверка на допустимость фигуры и функции
    assert fig in figs, f"Invalid figure: {fig}"
    assert func in funcs, f"Invalid function: {func}"

    # Формируем ключ для поиска в словаре размеров
    key = f'{fig}-{func}'
    expected_args = sizes.get(key)
    assert expected_args is not None, f"Unsupported operation: {key}"
    
    # Проверка на правильное количество аргументов
    assert len(size) == expected_args, f"Expected {expected_args} arguments, got {len(size)}"
    
    # Проверка на корректность размеров
    assert all(s >= 0 for s in size), "Sizes must be non-negative"

    # Дополнительная проверка для треугольников
    if fig == 'triangle':
        a, b, c = size
        assert a + b > c and a + c > b and b + c > a, "Invalid triangle sides"

    # Получаем соответствующий объект фигуры
    shape = globals().get(fig)  # Получаем объект фигуры (circle, square, triangle)
    if shape is None:
        raise ValueError(f"Shape {fig} not found")

    # Вызываем нужную функцию (perimeter или area)
    func_to_call = getattr(shape, func, None)
    if func_to_call is None:
        raise ValueError(f"Function {func} not found for {fig}")

    # Возвращаем результат выполнения функции
    return func_to_call(*size)
