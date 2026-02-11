'''
Statement of Exercise 25: 
Create a function that takes an array of filenames as an input. 
and return an array with those same files, but if there are any 
Duplicates must be numbered with a (number of repetitions) 
like operating systems do. 

Examples: 
renameFiles(["name.jpg", "surname.doc", "name.png", "name.png", "name.jpg", "name.jpg"]); 

Returns: 
[ 'name.jpg', 'surname.doc', 'name.png', 'name(1).png', 'name(1).jpg', 'name(2).jpg'] 

'''
name_list = [ 'name.jpg', 'surname.doc', 'name.png', 'name(1).png', 'name(1).jpg', 'name(2).jpg'] 

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






