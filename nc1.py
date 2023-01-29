
import requests

response = requests.get("https://jsonplaceholder.typicode.com/")
print(response)
# print(response.json()) # this method is convient when the ai returns json
# # response.context returns raw bytes of data
# #.tex() that returns string represtation
# #response.headers["content-type"] 