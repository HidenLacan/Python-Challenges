
'''
Statement of Exercise 24: 
Create a function that takes an array of filenames as an input. 
and return an array with those same files, but if there are any 
Duplicates must be numbered with a (number of repetitions) 
like operating systems do. 
 
Examples: 
renameFiles(["name", "surname", "first name", "first name"]); 
 
Returns: 
[ 'name', 'surname', 'name(1)', 'name(2)' ] 
'''
name_list = ["name", "surname", "first name", "first name"]

def rename_files(words_list:list) ->list: 
    name_refactor_list = []
    counter = {}
    
    for word in words_list:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    for key,value in counter.items():
        if value > 1:
            for num in range(1,value+1):
                name_refactor_list.append(f'{key}({num})')
        else:
            name_refactor_list.append(key)
    return name_refactor_list

print(rename_files(name_list))
