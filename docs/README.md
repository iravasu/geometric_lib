
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`




# Functions, description and examples
## `calculate.py`
### 'def calc(fig, func, size):'
- Calculates the value of the specified function for the specified shape based on its dimensions. 
- Example of a call:
```python
>> calc('circle', 'area', [5])
78.53981633974483
```
## `circle.py`
### `def area(r):`
- Calculates the area of a circle by a given radius.
- Example of a call:
```python
>> area(5)
78.53981633974483
```
### `def perimeter(r):`
- Calculates the length of a circle (the perimeter of a circle) by a given radius. 
- Example of a call:
```python
>> perimeter (5)
31.41592653589793
```
## `square.py`
### `def area(a):`
- Calculates the area of a square along a given side length.
- Example of a call:
```python
>> area(5)
25
```
### `def perimeter(a):`
- Calculates the perimeter of a square along a given side length.
- Example of a call:
```python
>> perimeter (5)
20
```
## `triangle.py`
### `def area(a, b, c):`
- Calculates the half-meter (not the area) of a triangle by the specified side lengths. 
- Example of a call:
```python 
>> area (3, 4, 5)
6.0
```
### `def perimeter(a, b, c)`
- Calculate the perimeter of a triangle from given side lengths.
- Example of a call:
```python
>> perimetr (3, 4, 5)
12
```
# The history of changing the project eiyj the hashed of thr comits
1. **8ba9aeb** L-03: Circle and square added
2. **d078c8d** L-03: Docs added
3. **d080c78** L-04: Triangle added
4. **51c40eb** L-04: Doc updated for triangle
5. **d76db2a** L-04: Add calculate.py
6. **b5b0fae** L-04: Update docs for calculate.py