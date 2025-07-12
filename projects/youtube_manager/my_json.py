import json

my_json = {
    "name": "Charles",
    "age": 33,
    "has_hair": False,
    "hobbies": ["photography", "running"],
}


py_dict = dict(
    alive=False,
    name="Toji",
    clan="Xenin",
    age=29,
    power=None,
    enemies=["Sukuna", "Gojo", "Itachi"],
)

# print(type(py_dict))
# print(py_dict)

# print("before encoded {}".format(py_dict))

# the json.dumps fn will convert the python datatypes into the json string formate
encoded_json = json.dumps(py_dict)


decode_json = json.loads(encoded_json)

print(decode_json)
