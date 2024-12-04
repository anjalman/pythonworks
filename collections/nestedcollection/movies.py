movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},

]

# total number of movies

print(len(movies))

# print movies title

movies_title=[m.get("title") for m in movies]

print(movies_title)

# print hieghest run_time 

hieghest_run_time=max(movies,key=lambda d:d.get("run_time"))

print(hieghest_run_time)

# which year most number of malayalam movie released

malayalam_movie={m.get("title") for m in movies if m.get("language")=="malayalam"}

print(len(malayalam_movie))