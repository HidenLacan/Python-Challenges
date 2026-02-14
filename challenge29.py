
'''
Statement of Exercise 29: 
Given an array of movie objects from the 80s and 90s. 

Create two functions: 
- One that filters them by gender 
- and another that filters them by decade in this 80s or 90s format 

Array of objects to use: 
const movies = [ 
{ title: "Terminator", genre: "action", release year: 1984 }, 
{ title: "Alien", genre: "science fiction", release year: 1979 }, 
{ title: "Die Hard", genre: "action", release year: 1988 }, 
{ title: "Predator", genre: "action", release year: 1987 }, 
{ title: "Total Recall", genre: "science fiction", release year: 1990 }, 
{ title: "RoboCop", genre: "science fiction", release year: 1987 }, 
{ title: "Starship Troopers", genre: "science fiction", release year: 1997 }, 
{ title: "The Fifth Element", genre: "science fiction", release year: 1997 }, 
{ title: "Armageddon", genre: "action", release year: 1998 }, 
{ title: "Deep Impact", genre: "science fiction", release year: 1998 } 
]; 

Examples: 
filterByGenre(movies, "action") 
filterByDecade(movies, "80s") 

'''

movies_list = [ { "title": "Terminator", "genre": "action", "release year": 1984 }, 
{ "title": "Alien", "genre": "science fiction", "release year": 1979 }, 
{ "title": "Die Hard", "genre": "action", "release year": 1988 }, 
{ "title": "Predator", "genre": "action", "release year": 1987 }, 
{ "title": "Total Recall", "genre": "science fiction", "release year": 1990 }, 
{ "title": "RoboCop", "genre": "science fiction", "release year": 1987 }, 
{ "title": "Starship Troopers", "genre": "science fiction", "release year": 1997 }, 
{ "title": "The Fifth Element", "genre": "science fiction", "release year": 1997 }, 
{ "title": "Armageddon", "genre": "action", "release year": 1998 }, 
{ "title": "Deep Impact", "genre": "science fiction", "release year": 1998 } 
]


genre = "action"
year = "80s"

def filter_by_genre(movies:list,genre:str)-> list:
    user_genre = genre
    movies_by_genre = []
    
    for movie in movies:
        for key,value in movie.items():
            if key == "genre" and value == user_genre:
                movies_by_genre.append(movie)
    return print(movies_by_genre)

def filter_by_year(movies:list,year:str)-> list:
    movies_by_year = []    
    for movie in movies:
        for key,value in movie.items():
            
            if key == "release year":
                value_year = str(value)
                if value_year[2] == year[0]:
                    movies_by_year.append(movie)
    
    return print(movies_by_year)

#filter_by_year(movies_list,year)
#filter_by_genre(movies_list,genre)

##### REFACTOR ########

def filter_by_genre_refactor(movies:list,genre:str)-> list:
    return [movie for movie in movies if movie.get("genre") == genre ]

print(filter_by_genre_refactor(movies_list,genre))

def filter_by_year_refactor(movies:list,year:str)-> list:
    return [
        movie 
        for movie in movies
        if str(movie.get("release year"))[2] == year[0]
    ]

print(filter_by_year_refactor(movies_list, year))