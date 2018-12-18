# This is my first python milestone project

"""
-Enter 'a' to add a movie
       'l' to see your movie
       'f' to find a movie and
       'q' to quit

-Add movies
-See movies
-Find a movies
-Stop ruunnig the program

Tasks:
[x]:Decide where to store movies
[x]:What is the format of a movie?
[x]:Show the user the main interface and get their input
[x]:Allow user to add movies
[x]:Show all their movies
[x]:Find a movie
[x]:Stop running the program when they type 'q'
"""

movies = []

"""
movie = {
    'name': ...(str),
    'director': ...(str),
    'year': ...(int)
}
"""


def menu():
    user_input = input("Enter 'a' to add a movie, 'l' to see your movie,'f' to find a movie and 'q' to quit: ")

    while user_input != 'q':
        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            find_movie()
        elif user_input == 'q':
            print("Stopping program...")
        else:
            print("Unknown command-please try again.")

        user_input = input("\nEnter 'a' to add a movie ,'l' to see your movie, 'f' to find a movie and 'q' to quit: ")


def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie year: ")

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movies_list):
    for movie in movies_list:
        show_movies_details(movie)


def show_movies_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movie():
    find_by = input("What property of a movie are you looking for? ")
    looking_for = input("What are you searching for? ")

    found_movies = find_by_attribute(movies, looking_for, lambda x: x[find_by])

    show_movies(found_movies)


def find_by_attribute(items, expected, finder):
    found = []

    for i in movies:
        if finder(i) == expected:
            found.append(i)

        return found


menu()

print(movies)
