import random

li = ["HP", "MP", "ATK", "DEF", "SPD", "MAG", "Lv"]
li2 = ["スライム", "ベホマスライム", "キングスライム", "はぐれメタル", "スライムベス"]
def create_mons():
    dc1 = {}
    for j in range(len(li2)):
        dc = {li[i]: random.randint(10, 50) for i in range(len(li)-1)}; dc["Lv"] = divmod((dc["HP"] + dc["MP"] + dc["ATK"] + dc["DEF"] + dc["SPD"] + dc["MAG"]), 10)[0]
        dc1[li2[j]] = dc
    return dc1

dc2 = create_mons()

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
    return lvdc4
lvdc5 = create_odds(dc2)
# m = 0
# while m < 5:
#     n = oddsli[m]
#     o = 0
#     ao = 0
#     while o < n:
#         ao += odds[m-o]
#         o += 1
#     lvdc4[lvdc21[m][1]] = (ao)/n
#     m += 1

def select(available_monsters):
    mli = []
    while len(mli) < 2:
        mons = random.choice(available_monsters)
        if not(mons in mli):
            mli.append(mons)
    mli2 = (mli[0], mli[1])
    return mli2

def d(m1, m2):
    dmg1 = (dc2[m1]["ATK"] - (dc2[m2]["DEF"])//2)//2
    if dmg1 < 2:
        dmg2 = random.randint(0,1)
    elif 2 <= dmg1 < 9:
        dmg2 = random.randint(dmg1-2,dmg1)
    elif 9 <= dmg1:
        dmg2 = (dmg1*7)//8 + ((dmg1//4 + 1)*(random.randint(0,255)))//256
    return dmg2

def cri(m1):
    dmg = dc2[m1]["ATK"]*(random.randint(55,65))//64
    if dmg > 254:
        dmg = 254
    return dmg

def dod(m1, m2):
    m1s = dc2[m1]["SPD"]
    m2s = dc2[m2]["SPD"]
    if m2s > m1s:
        dodge = (m2s-m1s)/(random.randint(1, 3)) - (random.randint(10, 20))/(random.randint(1, 10))
    elif m2s < m1s:
        dodge = (m2s-m1s)/(random.randint(1, 3)) + (random.randint(10, 20))/(random.randint(1, 10))
    else:
        dodge = 1/(random.randint(1, 3)) - (random.randint(10, 20))/(random.randint(1, 10))
    return dodge > 0

for key, value in dc2.items():
    print(f"{key}: {value}")

for key, value in lvdc5.items():
    print(f"{key}: {value}")

pm = input("賭けるモンスター名を入力")
po = int(input("賭ける金額を入力"))
ps = input("スタート")
mc = 0
alive_monsters = ["スライム", "ベホマスライム", "キングスライム", "はぐれメタル", "スライムベス"]
if not(ps == ("no")):
    winner = None
    while mc < 4:
        # while (dc2[mons1]["HP"] > 0) and (dc2[mons2]["HP"] > 0):
        (mons1, mons2) = select(alive_monsters)
        if pm == mons1 or pm == mons2:
            pa = input("コマンド入力(こうげき or かいふく or まじんぎり)")
            if pa == "こうげき":
                af = random.randint(0, 1)
                if af == 0:
                    m1 = mons1; m2 = mons2
                else:
                    m1 = mons2; m2 = mons1
                print(f"{m1}→{m2}")
                dod1 = dod(m1, m2)
                if dod1 == True:
                    print("回避成功")
                    af = random.randint(0, 1)
                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]; shp = dc2["スライム"]["HP"]; bhp = dc2["ベホマスライム"]["HP"]; khp = dc2["キングスライム"]["HP"]; hhp = dc2["はぐれメタル"]["HP"]; sbhp = dc2["スライムベス"]["HP"]
                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　全体のHP...スライム{shp}, ベホマスライム{bhp}, キングスライム{khp}, はぐれメタル{hhp}, スライムベス{sbhp}")
                else:
                    dmg = d(m1, m2)
                    dc2[m2]["HP"] -= dmg
                    print(f"{dmg}damage")
                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                    if dc2[m2]["HP"] <= 0:
                        print(f"{m2}のHPは0になってしまった... out")
                        dc2[m2]["HP"] = 0
                        shp = dc2["スライム"]["HP"]; bhp = dc2["ベホマスライム"]["HP"]; khp = dc2["キングスライム"]["HP"]; hhp = dc2["はぐれメタル"]["HP"]; sbhp = dc2["スライムベス"]["HP"]
                        print(f"全体のHP...スライム{shp}, ベホマスライム{bhp}, キングスライム{khp}, はぐれメタル{hhp}, スライムベス{sbhp}")
                        alive_monsters.remove(m2)
                        mc += 1
                        if mc == 4:
                            winner = m1
                            break
                    else:
                        af = random.randint(0, 1)
            elif pa == "かいふく":#もしかしてコマンド入力って自分が選ばれてしかも攻撃側だった時だけ？
                af = random.randint(0, 1)
                if af == 0:
                    m1 = mons1; m2 = mons2
                else:
                    m1 = mons2; m2 = mons1
                print(f"{m1}→{m2}")
                dod1 = dod(m1, m2)
                if dod1 == True:
                    print("回避成功")
                    af = random.randint(0, 1)
                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]; shp = dc2["スライム"]["HP"]; bhp = dc2["ベホマスライム"]["HP"]; khp = dc2["キングスライム"]["HP"]; hhp = dc2["はぐれメタル"]["HP"]; sbhp = dc2["スライムベス"]["HP"]
                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　全体のHP...スライム{shp}, ベホマスライム{bhp}, キングスライム{khp}, はぐれメタル{hhp}, スライムベス{sbhp}")
                else:
                    dmg = d(m1, m2)
                    dc2[m2]["HP"] -= dmg
                    print(f"{dmg}damage")
                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                    if dc2[m2]["HP"] <= 0:
                        print(f"{m2}のHPは0になってしまった... out")
                        dc2[m2]["HP"] = 0
                        shp = dc2["スライム"]["HP"]; bhp = dc2["ベホマスライム"]["HP"]; khp = dc2["キングスライム"]["HP"]; hhp = dc2["はぐれメタル"]["HP"]; sbhp = dc2["スライムベス"]["HP"]
                        print(f"全体のHP...スライム{shp}, ベホマスライム{bhp}, キングスライム{khp}, はぐれメタル{hhp}, スライムベス{sbhp}")
                        alive_monsters.remove(m2)
                        mc += 1
                        if mc == 4:
                            winner = m1
                            break
                    else:
                        af = random.randint(0, 1)
            elif pa == "まじんぎり":
                af = random.randint(0, 1)
                if af == 0:
                    m1 = mons1; m2 = mons2
                else:
                    m1 = mons2; m2 = mons1
                print(f"{m1}→{m2}")
                dod1 = dod(m1, m2)
                if dod1 == True:
                    print("回避成功")
                    af = random.randint(0, 1)
                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]; shp = dc2["スライム"]["HP"]; bhp = dc2["ベホマスライム"]["HP"]; khp = dc2["キングスライム"]["HP"]; hhp = dc2["はぐれメタル"]["HP"]; sbhp = dc2["スライムベス"]["HP"]
                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　全体のHP...スライム{shp}, ベホマスライム{bhp}, キングスライム{khp}, はぐれメタル{hhp}, スライムベス{sbhp}")
                else:
                    dmg = d(m1, m2)
                    dc2[m2]["HP"] -= dmg
                    print(f"{dmg}damage")
                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                    if dc2[m2]["HP"] <= 0:
                        print(f"{m2}のHPは0になってしまった... out")
                        dc2[m2]["HP"] = 0
                        shp = dc2["スライム"]["HP"]; bhp = dc2["ベホマスライム"]["HP"]; khp = dc2["キングスライム"]["HP"]; hhp = dc2["はぐれメタル"]["HP"]; sbhp = dc2["スライムベス"]["HP"]
                        print(f"全体のHP...スライム{shp}, ベホマスライム{bhp}, キングスライム{khp}, はぐれメタル{hhp}, スライムベス{sbhp}")
                        alive_monsters.remove(m2)
                        mc += 1
                        if mc == 4:
                            winner = m1
                            break
                    else:
                        af = random.randint(0, 1)
        else:
            pa = input("こうげき")
            if not(pa == "no"):
                af = random.randint(0, 1)
                if af == 0:
                    m1 = mons1; m2 = mons2
                else:
                    m1 = mons2; m2 = mons1
                print(f"{m1}→{m2}")
                dod1 = dod(m1, m2)
                if dod1 == True:
                    print("回避成功")
                    af = random.randint(0, 1)
                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]; shp = dc2["スライム"]["HP"]; bhp = dc2["ベホマスライム"]["HP"]; khp = dc2["キングスライム"]["HP"]; hhp = dc2["はぐれメタル"]["HP"]; sbhp = dc2["スライムベス"]["HP"]
                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　全体のHP...スライム{shp}, ベホマスライム{bhp}, キングスライム{khp}, はぐれメタル{hhp}, スライムベス{sbhp}")
                else:
                    dmg = d(m1, m2)
                    dc2[m2]["HP"] -= dmg
                    print(f"{dmg}damage")
                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                    if dc2[m2]["HP"] <= 0:
                        print(f"{m2}のHPは0になってしまった... out")
                        shp = dc2["スライム"]["HP"]; bhp = dc2["ベホマスライム"]["HP"]; khp = dc2["キングスライム"]["HP"]; hhp = dc2["はぐれメタル"]["HP"]; sbhp = dc2["スライムベス"]["HP"]
                        print(f"全体のHP...スライム{shp}, ベホマスライム{bhp}, キングスライム{khp}, はぐれメタル{hhp}, スライムベス{sbhp}")
                        alive_monsters.remove(m2)
                        mc += 1
                        if mc == 4:
                            winner = m1
                            break
                    else:
                        af = random.randint(0, 1)

    if (not(winner == None)) and (winner in dc2):
        wm = po*lvdc5[dc2[winner]["Lv"]]
        print(f"バトロワの勝者は {winner}")
        if pm == winner:
            print(f"あなたの勝ち  {wm}円 got")
        else:
            print(f"あなたの負けです  {po}円 lost")
    else:
        print("error")
else:
    print("see you!")