import random
Imbd_top30_movie = [
    {"title": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994},
    {"title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972},
    {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008},
    {"title": "The Godfather Part II", "director": "Francis Ford Coppola", "year": 1974},
    {"title": "12 Angry Men", "director": "Sidney Lumet", "year": 1957},
    {"title": "Schindler’s List", "director": "Steven Spielberg", "year": 1993},
    {"title": "The Lord of the Rings: The Return of the King", "director": "Peter Jackson", "year": 2003},
    {"title": "Pulp Fiction", "director": "Quentin Tarantino", "year": 1994},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "year": 2001},
    {"title": "The Good, the Bad and the Ugly", "director": "Sergio Leone", "year": 1966},
    {"title": "Forrest Gump", "director": "Robert Zemeckis", "year": 1994},
    {"title": "Fight Club", "director": "David Fincher", "year": 1999},
    {"title": "Inception", "director": "Christopher Nolan", "year": 2010},
    {"title": "The Lord of the Rings: The Two Towers", "director": "Peter Jackson", "year": 2002},
    {"title": "Star Wars: Episode V – The Empire Strikes Back", "director": "Irvin Kershner", "year": 1980},
    {"title": "The Matrix", "director": "The Wachowskis", "year": 1999},
    {"title": "Goodfellas", "director": "Martin Scorsese", "year": 1990},
    {"title": "One Flew Over the Cuckoo’s Nest", "director": "Milos Forman", "year": 1975},
    {"title": "Se7en", "director": "David Fincher", "year": 1995},
    {"title": "Seven Samurai", "director": "Akira Kurosawa", "year": 1954},
    {"title": "City of God", "director": "Fernando Meirelles & Kátia Lund", "year": 2002},
    {"title": "It’s a Wonderful Life", "director": "Frank Capra", "year": 1946},
    {"title": "The Silence of the Lambs", "director": "Jonathan Demme", "year": 1991},
    {"title": "Saving Private Ryan", "director": "Steven Spielberg", "year": 1998},
    {"title": "Spirited Away", "director": "Hayao Miyazaki", "year": 2001},
    {"title": "Life Is Beautiful", "director": "Roberto Benigni", "year": 1997},
    {"title": "The Usual Suspects", "director": "Bryan Singer", "year": 1995},
    {"title": "Léon: The Professional", "director": "Luc Besson", "year": 1994},
    {"title": "Harakiri", "director": "Masaki Kobayashi", "year": 1962},
    {"title": "Parasite", "director": "Bong Joon-ho", "year": 2019},
    
    ]

def movie_night():
    picked_movie = random.choice(Imbd_top30_movie)
    print(f"Todays movie is: {picked_movie["title"]} {picked_movie["year"]} {picked_movie["director"]}.")
movie_night()
