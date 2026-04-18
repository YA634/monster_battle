import random
import copy

li = ["HP", "MP", "ATK", "DEF", "SPD", "MAG", "Lv", "CON"]
li2 = ["スライムLv8", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]

def create_mons():
    primitive_dc = {}
    for j in range(len(li2)):
        dc = {li[i]: random.randint(10, 50) for i in range(len(li)-2)}; dc["Lv"] = divmod((dc["HP"] + dc["MP"] + dc["ATK"] + dc["DEF"] + dc["SPD"] + dc["MAG"]), 10)[0]; dc["CON"] = {"げんき": 1}; dc["BfDbf"] = {"bk": 0, "rk": 0}
        primitive_dc[li2[j]] = dc
    primitive_dc["はぐれメタル"]["DEF"] = 99; primitive_dc["はぐれメタル"]["Lv"] = (primitive_dc["はぐれメタル"]["HP"]+primitive_dc["はぐれメタル"]["MP"]+primitive_dc["はぐれメタル"]["ATK"]+(primitive_dc["はぐれメタル"]["DEF"]//3)+primitive_dc["はぐれメタル"]["SPD"]+primitive_dc["はぐれメタル"]["MAG"])//10
    primitive_dc["スライムベス"]["MP"] = random.randint(25, 50); primitive_dc["スライムベス"]["Lv"] = (primitive_dc["スライムベス"]["HP"]+primitive_dc["スライムベス"]["MP"]+primitive_dc["スライムベス"]["ATK"]+(primitive_dc["スライムベス"]["DEF"]//3)+primitive_dc["スライムベス"]["SPD"]+primitive_dc["スライムベス"]["MAG"])//10
    return primitive_dc
    # primitive_dc = create_mons()
    # primitive_dc["はぐれメタル"]["DEF"] = 100; primitive_dc["はぐれメタル"]["Lv"] = (primitive_dc["はぐれメタル"]["HP"]+primitive_dc["はぐれメタル"]["MP"]+primitive_dc["はぐれメタル"]["ATK"]+(primitive_dc["はぐれメタル"]["DEF"]//3)+primitive_dc["はぐれメタル"]["SPD"]+primitive_dc["はぐれメタル"]["MAG"])//10
    # m_dc = copy.deepcopy(primitive_dc)
    # return m_dc

def create_odds(dct):
    lvli = [dct[li2[i]]["Lv"] for i in range(len(li2))]
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
            lvdc4[lvdc21[m][0]] = odds[m]
        elif oddsli[m] == 2:
            lvdc4[lvdc21[m][0]] = lvdc4[lvdc21[m-1][0]] = (odds[m] + odds[m-1])/2
        elif oddsli[m] == 3:
            lvdc4[lvdc21[m][0]] = lvdc4[lvdc21[m-1][0]] = lvdc4[lvdc21[m-2][0]] = (odds[m] + odds[m-1] + odds[m-2])/3
        elif oddsli[m] == 4:
            lvdc4[lvdc21[m][0]] = lvdc4[lvdc21[m-1][0]] = lvdc4[lvdc21[m-2][0]] = lvdc4[lvdc21[m-3][0]] = (odds[m] + odds[m-1] + odds[m-2] + odds[m-3])/4
        elif oddsli[m] == 5:
            lvdc4[lvdc21[m][0]] = lvdc4[lvdc21[m-1][0]] = lvdc4[lvdc21[m-2][0]] = lvdc4[lvdc21[m-3][0]] = lvdc4[lvdc21[m-4][0]]= odds[m]= 4.0
            m += 5
        m += 1
    return lvdc4
    odds_dc = create_odds(m_dc)