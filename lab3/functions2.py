def imdb_above_5_5(movie):
    return movie["imdb"] > 5.5


print(imdb_above_5_5(movies[0])) 

def movies_above_5_5(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]


print(movies_above_5_5(movies))

def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

print(movies_by_category(movies, "Romance"))

def average_imdb_score(movies):
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)


print(average_imdb_score(movies))

def average_imdb_score_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb_score(category_movies)


print(average_imdb_score_by_category(movies, "Romance"))





