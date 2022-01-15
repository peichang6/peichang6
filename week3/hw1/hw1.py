import urllib.request
import json
import ssl
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
context = ssl._create_unverified_context()
with urllib.request.urlopen(url, context=context) as file:  # 連結網站
    data = json.load(file)  # 讀取json格式的檔案，會回傳dict
attractions_list = data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as csvfile:
    for d in attractions_list:
        dist = d["address"][5:8]
        pic = []
        pic.append(((d["file"]).lower().split("jpg"))[0] + "jpg")
        csvfile.write("{},{},{},{},{}" .format(d["stitle"],
                                               dist, d["longitude"], d["latitude"], pic[0]+"\n"))
