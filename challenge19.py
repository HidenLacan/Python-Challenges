

import random



def dice() -> int:
    
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1,6) 
    result = dice_1 + dice_2
    return print(f' dice_1 = {dice_1} dice_2= {dice_2} result = {result}')
dice()