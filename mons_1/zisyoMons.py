import random
# li = ["HP", "MP", "ATK", "DEF", "SPD", "MAG", "Lv"]
# i = 0
# dc = {}
# while i < len(li)-1:
#     dc[li[i]] = random.randint(10, 51)
#     i += 1
#     if i == len(li)-1:
#         dc["Lv"] = (dc["HP"] + dc["MP"] + dc["ATK"] + dc["DEF"] + dc["SPD"] + dc["MAG"])//10
# print(dc)

# dc = {}
# dc = {"HP": random.randint(10, 51)}
# dc["HP"] = random.randint(10, 51)
# dc["MP"] = random.randint(10, 51)
# dc["ATK"] = random.randint(10, 51)
# dc["DEF"] = random.randint(10, 51)
# dc["SPD"] = random.randint(10, 51)
# dc["MAG"] = random.randint(10, 51)

li = ["HP", "MP", "ATK", "DEF", "SPD", "MAG", "Lv"]
li2 = ["スライム", "ベホマスライム", "キングスライム", "はぐれメタル", "スライムベス"]

# dc = {li[i]: random.randint(10, 51) for i in range(len(li)-1)}; dc["Lv"] = divmod((dc["HP"] + dc["MP"] + dc["ATK"] + dc["DEF"] + dc["SPD"] + dc["MAG"]), 10)[0]
# for i in range(len(li)-1):
#     for dc in range(len(li2)):
#         for j in range(len(li2)):
#             dc = {li[i]: random.randint(10, 50)}
# dc["Lv"] = (dc["HP"] + dc["MP"] + dc["ATK"] + dc["DEF"] + dc["SPD"] + dc["MAG"])//10
dc2 = {}
lvli = []
for j in range(len(li2)):
    dc = {li[i]: random.randint(10, 50) for i in range(len(li)-1)}; dc["Lv"] = divmod((dc["HP"] + dc["MP"] + dc["ATK"] + dc["DEF"] + dc["SPD"] + dc["MAG"]), 10)[0]
    lvli.append(dc["Lv"])
    dc2[li2[j]] = dc
# odds = [2, 3, 4, 5, 6]
# odds = {2, 3, 4, 5, 6}
lvdc = {li2[k]: lvli[k] for k in range(5)}
# lvtp = lvdc.items()
# def key_value(x):
#     return x[1]
# lvdc2 = sorted(lvtp, key = key_value(lvtp))
lvdc21 = sorted(lvdc.items(), key = lambda x: x[1], reverse = True,)
lvdc2 = {lvdc21[k][0]: lvdc21[k][1] for k in range(5)}
v = 0
while v < 5:
    lvdc2[v][1] = 2+v
    if v < 4 and lvdc2[v][1] == lvdc2[v+1][1]:
        if v < 3 and lvdc2[v][1] == lvdc2[v+1][1] == lvdc[v+2][1]:
            lvdc2[v][1] = lvdc2[v+1][1] = lvdc2[v+2][1] = (4+v)/2
        lvdc2[v][1] = lvdc2[v+1][1] = (3+v)/2

    v += 1

# lvli.append(dc["Lv"])
# lvli.sort()
# if lvli[0] == dc["Lv"]:
#     dc
# for k in range(len(li2)):
#     dc3 = {dc["Lv"]: od }
# dc2 = {li2[j]: dc for j in range(len(li2))}
for key, value in dc2.items():
    print(f"{key}: {value}") #5体全部同じになっちゃう　オッズ書く
# print(f"{key}: {value}" for key, value in dc2.items())
# print({li2[j]: dc} for j in range(len(li2)))


