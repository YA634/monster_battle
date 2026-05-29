import random

li = ["HP", "MP", "ATK", "DEF", "SPD", "MAG", "Lv"]
li2 = ["スライム", "ベホマスライム", "キングスライム", "はぐれメタル", "スライムベス"]
dc2 = {}
lvli = []
for j in range(len(li2)):
    dc = {li[i]: random.randint(10, 50) for i in range(len(li)-1)}; dc["Lv"] = divmod((dc["HP"] + dc["MP"] + dc["ATK"] + dc["DEF"] + dc["SPD"] + dc["MAG"]), 10)[0]
    lvli.append(dc["Lv"])
    dc2[li2[j]] = dc
lvdc = {li2[k]: lvli[k] for k in range(5)}
lvdc21 = sorted(lvdc.items(), key = lambda x: x[1], reverse = True,)
lvdc3 = {}
lvdc4 = {}
oddsli = []
k = 0
l = 1
while k < 5:
    if k < 4 and (lvdc21[k][1] == lvdc21[k+1][1]):
        l += 1
        oddsli.append(9)
    else:
        lvdc3[lvdc21[k][1]] = l
        oddsli.append(l)
        l = 1
    k += 1
odds = [2, 3, 4, 5, 6]
m = 0
while m < 5:
    if oddsli[m] == 1:
        lvdc4[lvdc21[m][1]] = odds[m]
    elif oddsli[m] == 2:
        lvdc4[lvdc21[m][1]] = (odds[m] + odds[m-1])/2
    elif oddsli[m] == 3:
        lvdc4[lvdc21[m][1]] = (odds[m] + odds[m-1] + odds[m-2])/3
    elif oddsli[m] == 4:
        lvdc4[lvdc21[m][1]] = (odds[m] + odds[m-1] + odds[m-2] + odds[m-3])/4
    elif oddsli[m] == 5:
        lvdc4[lvdc21[m][1]] = 4.0
        m += 5
    m += 1
    

        

# print(lvdc21)
for key, value in lvdc4.items():
    print(f"{key}: {value}")

for key, value in dc2.items():
    print(f"{key}: {value}") #5体全部同じになっちゃう　オッズ書く