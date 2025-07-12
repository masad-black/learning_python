import requests


headers = {"accept": "application/json"}

# get method
res = requests.get("https://api.freeapi.app/api/v1/public/randomproducts")
# print("response: ", res.url)


#  get method and query string
get_res = requests.get(
    "https://api.freeapi.app/api/v1/public/randomproducts/",
    params={"productId": 30},
    headers=headers,
)


# print("text: ", get_res.text)  # this will automatically convert the contenet
# print("content: ", get_res.content)  # this is the raw data that i comming form api
# print(
#     "encoding: ", get_res.encoding
# )  # this tell us about, what type of encoding we are using

# this will convert the data into json formate
# print(get_res.json())

# print(get_res.json()["data"])

# for item in get_res.json():
#     print(item)
