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
print(lvdc21)
for k in range(5):
    if k < 1 and (lvdc21[k][1] == lvdc21[k+1][1] == lvdc21[k+2][1] == lvdc21[k+3][1] == lvdc21[k+4][1]):
        lvdc3[lvdc21[k][0]] = lvdc3[lvdc21[k+1][0]] = lvdc3[lvdc21[k+2][0]] = lvdc3[lvdc21[k+3][0]] = lvdc3[lvdc21[k+4][0]] = (k+2 + k+3 + k+4 + k+5 + k+6)/5
        break
    elif 0 < k and (lvdc21[k-1][1] == lvdc21[k][1]):
        if 1 < k and (lvdc21[k-2][1] == lvdc21[k][1]):
            if 2 < k and (lvdc21[k-3][1] == lvdc21[k][1]):
                if (k < 4 and (not(lvdc21[k][1] == lvdc21[k+1][1]))) or k == 4:
                    lvdc3[lvdc21[k-3][0]] = lvdc3[lvdc21[k-2][0]] = lvdc3[lvdc21[k-1][0]] = lvdc3[lvdc21[k][0]] = (k-1 + k + k+1 + k+2)/4 
            elif (k < 4 and (not(lvdc21[k][1] == lvdc21[k+1][1]))) or k == 4:
                lvdc3[lvdc21[k-2][0]] = lvdc3[lvdc21[k-1][0]] = lvdc3[lvdc21[k][0]] = (k + k+1 + k+2)/3
        elif (k < 4 and (not (lvdc21[k][1] == lvdc21[k+1][1]))) or k == 4:
            lvdc3[lvdc21[k-1][0]] = lvdc3[lvdc21[k][0]] = (k+2 + k+1)/2
        else:
            continue
    else:
        lvdc3[lvdc21[k][0]] = k+2

# print(lvdc21)
for key, value in lvdc3.items():
    print(f"{key}: {value}")

for key, value in dc2.items():
    print(f"{key}: {value}") #5体全部同じになっちゃう　オッズ書く