import circle
import square
import triangle


figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
	'circle-area' : 1,
	'circle-perimeter' : 1,
	'square-area' : 1,
	'square-perimeter' : 1,
	'triangle-area': 3,
	'triangle-perimeter' : 3
}

def calc(fig, func, size):
    assert fig in figs
    assert func in funcs

    key = f'{fig}-{func}'
    expected_args = sizes.get(key)
    assert expected_args is not None, f"Unsupported operation: {key}"
    assert len(size) == expected_args, f"Expected {expected_args} arguments, got {len(size)}"

    assert all(s >= 0 for s in size)

    if fig == 'triangle':
        a, b, c = size
        assert a + b > c and a + c > b and b + c > a, "Invalid triangle sides"
        
    result = eval(f'{fig}.{func}(*{size})')
    return result




