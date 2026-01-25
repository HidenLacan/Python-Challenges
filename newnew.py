
###### First Stage
notes  = {}
points = 0
turn_results = [1,1,1,1,1]

for result in turn_results:
    if result in notes:
        notes[result] += 1
    else:
        notes[result] = 1
''' 
for key, value in notes.items():
    if key == 1 and value >= 3:
        value -= 3
        points += 300
    if key == 2 and value >= 3:
        value -= 3
        points += 200 
    if key == 3 and value >= 3 :
        points += 100
    if key == 4 and value >= 3:
        points += 50
    if key == 5 and value >= 3:
        points += 10
    if key == 1 and value >= 1:
        while value > 0:
            points += 1
            value -= 1
    if key == 2 and value >= 1:
        while value > 0:
            points += 1
            value -= 1
'''
##### Second Stage

for key, value in notes.items():
    match key:
        case 1:
            # triple ones
            if value >= 3:
                triples = value // 3
                points += triples * 300
                value -= 3  # leftovers
            points += value * 1

        case 2:
            if value >= 3:
                triples = value // 3
                points += triples * 200
                value -= 3 # leftovers
            points += value * 1

        case 3:
            if value >= 3:
                triples = value // 3
                points += triples * 100

        case 4:
            if value >= 3:
                triples = value // 3
                points += triples * 50
        case 5:
            points += value * 10
        case _:
            pass
print(points)