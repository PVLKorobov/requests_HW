import pip._vendor.requests as requests
import json


def request(name_list):
    list = []
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    data = json.loads(response.content)
    for entry in data:
        name = entry["name"]
        if name in name_list:
            list += [{"name": entry["name"], "id": entry["id"], "intelligence": entry["powerstats"]["intelligence"]}]
    return list

name_list = ["Hulk", "Captain", "America", "Thanos"]
data_list = request(name_list)
sorted_data_list = sorted(data_list, key=lambda dict: dict["intelligence"], reverse=True)
found_name = sorted_data_list[0]["name"]
print(f"{found_name} - самый умный из супергероев")