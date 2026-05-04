import requests as req
import json

# request = req.get('https://jsonplaceholder.typicode.com/todos?userId=4&completed=true')
request = req.get('https://jsonplaceholder.typicode.com/todos',params={
    "userId":"1",
    "completed":"true"
})

todos = request.json()

print(todos)