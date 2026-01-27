
'''
Statement of Exercise 13: 
Create a function that calculates the area of ​​a square, a rectangle, or a triangle. 

Examples: 
calculateAreaPolygon({ type: 'triangle', base: 6, height: 9 }); 

Returns: 27 
'''


x = 'rectangle'
b = 3
a = 4

def area(x: str,b: int,a: int):
    match x:
        case 'rectangle':
            result = round(b * a)
            return print(f'result: {result}')
        case 'triangle':
            result = round(b * a / 2)
            return print(f'result: {result}')
        case 'square':
            result = round(b + a * 2)
            return print(f'result: {result}')

