
# CODSOFT AI Internship - Task 2
# Movie Recommendation System

movies = {
    "Interstellar": ["sci-fi", "adventure", "drama"],
    "Inception": ["sci-fi", "thriller", "action"],
    "Avengers": ["action", "sci-fi", "adventure"],
    "John Wick": ["action", "thriller"],
    "Titanic": ["romance", "drama"],
    "The Notebook": ["romance", "drama"],
    "Jurassic Park": ["sci-fi", "adventure"],
    "The Dark Knight": ["action", "thriller", "drama"]
}


def recommend(movie_name):
    if movie_name not in movies:
        print("Sorry, movie not found.")
        return

    selected_genres = set(movies[movie_name])

    recommendations = []

    for movie, genres in movies.items():
        if movie != movie_name:
            similarity = len(
                selected_genres.intersection(set(genres))
            )

            if similarity > 0:
                recommendations.append((movie, similarity))

    recommendations.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommendations for:", movie_name)
    print("--------------------------------")

    for movie, score in recommendations[:3]:
        print(movie)


print("🎬 Movie Recommendation System")
print("--------------------------------")

print("Available movies:")

for movie in movies:
    print("-", movie)

user_movie = input("\nEnter a movie you like: ")

recommend(user_movie)
