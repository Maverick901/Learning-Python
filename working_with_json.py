import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "IP man", "year": 2008},
#     {"id": 2, "title": "IP man 2", "year": 2009}
# ]
# data = json.dumps(movies)
# Path("movies.json").write_text(data)

data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies[0])
print(movies[0]["title"])
