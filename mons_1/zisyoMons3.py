import random

li = ["HP", "MP", "ATK", "DEF", "SPD", "MAG", "Lv"]
li2 = ["スライム", "ベホマスライム", "キングスライム", "はぐれメタル", "スライムベス"]
dc2 = {}
lvli = []
for j in range(len(li2)):
    dc = {li[i]: random.randint(10, 50) for i in range(len(li)-1)}; dc["Lv"] = divmod((dc["HP"] + dc["MP"] + dc["ATK"] + dc["DEF"] + dc["SPD"] + dc["MAG"]), 10)[0]
    lvli.append(dc["Lv"])
    dc2[li2[j]] = dc
odds = [2, 3, 4, 5, 6]

for key, value in dc2.items():
    print(f"{key}: {value}") #5体全部同じになっちゃう　オッズ書く
# print(f"{key}: {value}" for key, value in dc2.items())
# print({li2[j]: dc} for j in range(len(li2)))