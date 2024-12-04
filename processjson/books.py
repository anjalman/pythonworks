from json import load

f=open("D:\\pythonworks\\Datasets\\books.json")

data=load(f)

# for books in data:

#     print(books)

costly_book_price=max(books.get("price") for books in data)

# print(costly_book_price)

all_title=[books.get("title") for books in data]

# print(all_title)
    
cheapest_book=min(data,key=lambda d:d.get("price"))

# print(cheapest_book)

pages_filter=[books.get("title")for books in data if books.get("pages")<250]

# print(pages_filter)


all_genre=[books.get("genre")for books in data]

# print(set(all_genre))

genre_count={genre:all_genre.count(genre) for genre in all_genre}

# print(genre_count)

costly_books=max(data,key=lambda d:d.get("price"))

# print(costly_books)

all_author=[books.get("author")for books in data]

# print(all_author)

author_count={author:all_author.count(author) for author in all_author}

# print([k for k,v in author_count.items() if v>1])

