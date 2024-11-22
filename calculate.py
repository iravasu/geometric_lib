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
    assert fig in figs, f"Invalid figure: {fig}"
    assert func in funcs, f"Invalid function: {func}"

    key = f'{fig}-{func}'
    expected_args = sizes.get(key)
    assert expected_args is not None, f"Unsupported operation: {key}"
    assert len(size) == expected_args, f"Expected {expected_args} arguments, got {len(size)}"

    assert all(s >= 0 for s in size), "Sizes must be non-negative"

    if fig == 'triangle':
        a, b, c = size
        assert a + b > c and a + c > b and b + c > a, "Invalid triangle sides"

    # Вызываем соответствующую функцию напрямую
    if fig == 'circle':
        shape = circle
    elif fig == 'square':
        shape = square
    elif fig == 'triangle':
        shape = triangle

    if func == 'perimeter':
        result = shape.perimeter(*size)
    elif func == 'area':
        result = shape.area(*size)

    return result
