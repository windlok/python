import requests as req
import json


url = "https://api.themoviedb.org/3/movie/changes"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyNzQxNDk1ZjkxNGQwNWIxZmEwN2ZjYzJmYmY0MDU2MCIsIm5iZiI6MTc3Nzg4MzA3My43NjYsInN1YiI6IjY5Zjg1N2MxM2NlNDczYzZmNzMyNmY5YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.kOFTZ43lXjWGKwmlRluo13i4yQYlcZ4lGr2AQTP-3A0"
}

response = req.get(url, headers=headers ,params={
    "start_date": "2024-06-01"})

print(response.text)