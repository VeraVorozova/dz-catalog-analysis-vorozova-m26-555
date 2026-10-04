import math

movies = [
    {
        "title": "The Dune Chronicles", 
        "year": 2021, 
        "genres": {"sci-fi", "drama"}, 
        "rating": 8.6, "duration_min": 155, 
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]
    },
    {
        "title": "Kitchen Stories", 
        "year": 2019, 
        "genres": {"comedy", "drama"}, 
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"]
    },
    {
        "title": "silent hours", 
        "year": 2016, 
        "genres": {"thriller", "drama"}, 
        "rating": 6.4, 
        "duration_min": 112, 
        "actors": ["J. Bloom", "K. Lee"]
    },
    {
        "title": "Comet Racers", 
        "year": 2023, 
        "genres": {"sci-fi", "action"}, 
        "rating": 5.9, 
        "duration_min": 101, 
        "actors": ["O. Isaac", "P. Diaz"]
    },
    {
        "title": "The Last Bakery", 
        "year": 2014, 
        "genres": {"comedy"}, 
        "rating": 7.8, 
        "duration_min": 89, 
        "actors": ["A. Novak", "T. Chalamet"]
    },
    {
        "title": "midnight in oslo", 
        "year": 2020, 
        "genres": {"thriller", "mystery"}, 
        "rating": 8.9, 
        "duration_min": 124, 
        "actors": ["K. Lee", "R. Ferguson"]
    },
    {
        "title": "Garden of Static", 
        "year": 2022, 
        "genres": {"drama"}, 
        "rating": 4.8, 
        "duration_min": 137, 
        "actors": ["P. Diaz", "J. Bloom"]
    },
    {
        "title": "The Quiet Algorithm", 
        "year": 2024, 
        "genres": {"sci-fi", "drama"},
        "rating": 9.2, 
        "duration_min": 118, 
        "actors": ["M. Ferguson", "O. Isaac"]
    },
    {
        "title": "Two Left Shoes", 
        "year": 2011, 
        "genres": {"comedy"}, 
        "rating": 6.0, 
        "duration_min": 95, 
        "actors": ["A. Novak", "K. Lee"]},
    {
        "title": "Red Harbor", 
        "year": 2018, 
        "genres": {"action", "thriller"}, 
        "rating": 7.3, 
        "duration_min": 129, 
        "actors": ["P. Diaz", "T. Chalamet"]
    },
]


# Этап 1. Разминка: переменные, числа, math
def average_rating(movies):
    total = sum(movie["rating"] for movie in movies)
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    avg_age = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, avg_age)


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours}ч {mins}м"


# Этап 2. Условия и match
def rating_tier(rating):
    if rating >= 9.0:
        return "шедевр"
    elif rating >= 7.0:
        return "хорошо"
    else:
        return "средне" if rating >= 5.0 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"


# Этап 3. Циклы
def print_non_comedy_movies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9.0:
            print(f"Найден шедевр: {movies[i]['title']}")
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# Этап 4. Строки
def normalize_title(title):
    words = title.split(" ")
    normalized_words = [
        word[0].upper() + word[1:] if word else "" for word in words
    ]
    return " ".join(normalized_words)


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    norm_title = normalize_title(movie["title"])
    dus_str = duration_in_hours(movie["duration_min"])
    sorted_genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{norm_title}" ({movie["year"]}) {movie["rating"]}/10, '
        f"{dus_str}, жанры: {sorted_genres}"
    )


# Этап 5. Списки
def titles_sorted_by_rating(movies):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [normalize_title(m["title"]) for m in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [
        (normalize_title(m["title"]), m["rating"]) for m in sorted_movies[:n]
    ]


# Этап 6. Словари
def count_by_genre(movies):
    genre_counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = genre_counts.get(genre, 0) + 1
    return genre_counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        title = normalize_title(movie["title"])
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(title)
    return filmography


def movies_above_avg_rating(movies):
    avg = average_rating(movies)

    return{
        normalize_title(movie["title"]): movie["rating"]
        for movie in movies
        if movie["rating"] > avg
    }


# Этап 7. Множества
def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    genres_a = set()
    genres_b = set()

    for m in movies_a:
        genres_a.update(m["genres"])

    for m in movies_b:
        genres_b.update(m["genres"])

    return genres_a - genres_b


# Этап 8. Итераторы и генераторы
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


# Этап 9. Итоговый отчет
def build_report(movies):
    print("ОТЧеТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")

    _, _, avg_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {avg_age} лет")

    print("\nТоп-3 фильма:")
    top_3 = sorted(movies, key=lambda m: m["rating"], reverse=True)[:3]
    for movie in top_3:
        norm_title = normalize_title(movie["title"])
        dur = duration_in_hours(movie["duration_min"])
        genres_str = ", ".join(sorted(movie["genres"]))

        print(
            f'  "{norm_title}" ({movie["year"]}) — {movie["rating"]}/10, '
            f"{dur}, жанры: {genres_str}"
        )

    print("\nФильмов по жанрам:")
    counts = count_by_genre(movies)
    sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for genre, count in sorted_counts:
        print(f"  {genre} — {count}")

    sorted_genres = sorted(all_genres(movies))
    print(f"\nВсе жанры каталога: {', '.join(sorted_genres)}")


if __name__ == "__main__":
    build_report(movies)

    # Этап 8, генераторное выражение
    _ = sum(m["duration_min"] for m in movies if m["rating"] > 7)