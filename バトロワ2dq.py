import random
import copy
li = ["HP", "MP", "ATK", "DEF", "SPD", "MAG", "Lv", "CON"]
li2 = ["スライムLv8", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
li3 = ["キングスライム", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
def create_mons():
    dc1 = {}
    for j in range(len(li2)):
        dc = {li[i]: random.randint(10, 50) for i in range(len(li)-2)}; dc["Lv"] = divmod((dc["HP"] + dc["MP"] + dc["ATK"] + dc["DEF"] + dc["SPD"] + dc["MAG"]), 10)[0]; dc["CON"] = {"げんき": 1}; dc["BfDbf"] = {"bk": 0, "rk": 0}
        dc1[li2[j]] = dc
    return dc1

primitive_dc = create_mons()
primitive_dc["はぐれメタル"]["DEF"] = 100; primitive_dc["はぐれメタル"]["Lv"] = (primitive_dc["はぐれメタル"]["HP"]+primitive_dc["はぐれメタル"]["MP"]+primitive_dc["はぐれメタル"]["ATK"]+(primitive_dc["はぐれメタル"]["DEF"]//3)+primitive_dc["はぐれメタル"]["SPD"]+primitive_dc["はぐれメタル"]["MAG"])//10
dc2 = copy.deepcopy(primitive_dc)
dddc = {}

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

def md(m1, m2, x):
    dmg1 = ((dc2[m1]["MAG"]*3//2)*x - (dc2[m2]["DEF"])//2)//2
    if dmg1 < 2:
        dmg2 = random.randint(0,1)
    elif 2 <= dmg1 < 9:
        dmg2 = random.randint(dmg1-2,dmg1)
    elif 9 <= dmg1:
        dmg2 = (dmg1*7)//8 + ((dmg1//4 + 1)*(random.randint(0,255)))//256
    return dmg2


def aselect(m1):
    ac = alive_monsters.copy()
    ac.remove(m1)
    return ac

def cri(m1):
    dmg = dc2[m1]["ATK"]*(random.randint(55,65))//64
    if dmg > 254:
        dmg = 254
    return dmg

#m1 > m2 dod low  m1 < m2 dod high
def dod(m1, m2, x):
    m1s = dc2[m1]["SPD"]
    m2s = dc2[m2]["SPD"]
    if m1s > m2s:
        dodge = -(m1s-m2s)/(random.randint(1, 3)) + (random.randint(10, 20))/(random.randint(1, 10)) - 3*x
    elif m1s < m2s:
        dodge = -(m1s-m2s)/(random.randint(1, 3)) - (random.randint(10, 20))/(random.randint(1, 10)) - 3*x
    else:
        dodge = 1/(random.randint(1, 3)) - (random.randint(10, 20))/(random.randint(1, 10)) - 3*x
    return dodge > 0

def mhpli():
    result = "全体のHP..."
    for mn in li2:
        hp = dc2[mn]["HP"]
        keys = list(dc2[mn]['CON'].keys())
        result += f"{mn} {hp} {keys}, "   
    return result.rstrip(", ")

def mhplik():
    result = "全体のHP..."
    for mn in li3:
        hp = dc2[mn]["HP"]
        keys = list(dc2[mn]['CON'].keys())
        result += f"{mn} {hp} {keys}, "   
    return result.rstrip(", ")

for key, value in dc2.items():
    filtered_value = {k: v for k, v in value.items() if (not(k == "BfDbf")) and (not(k == "CON"))}
    # print(f"{key}: {value}")
    print(f"{key}: {filtered_value}")

for key, value in lvdc5.items():
    print(f"{key}: {value}")

pm = input("賭けるモンスター名を入力")
po = int(input("賭ける金額を入力"))
ps = input("スタート")
mc = 0
sc = 1
alive_monsters = ["スライムLv8", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
if not(ps == ("no")):
    winner = None
    while mc < 4:
        (mons1, mons2) = select(alive_monsters)
        af = random.randint(0, 1)
        if af == 0:
            m1 = mons1; m2 = mons2
        else:
            m1 = mons2; m2 = mons1
        jm1li = list(dc2[m1]['CON'].keys())        
        if "ねむり" in jm1li:
            print(f"{m1}→{m2}")
            print(f"{m1}はねむっている！")
        else:
            if pm == m1 or m1 == "キングスライム":
                print(f"{m1}→{m2}")
                m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]; m1mp = dc2[m1]["MP"]
                print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　"); print(mhpli())
                if pm == "ベホマスライム":
                    pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or キアリー or ベホマ or まじんぎり) 残りMP{m1mp}")
                elif pm == "スライムLv8":
                    if sc == 8:
                        pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or 合体 or まじんぎり ) 残りMP{m1mp}")
                    else:
                        pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or なかまをよぶ or まじんぎり　) 残りMP{m1mp}")
                elif pm == "キングスライム":
                    pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or ラリホーマ or どくの息 or まじんぎり) 残りMP{m1mp}")
                elif pm == "ドラゴスライム":
                    pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or ラリホーマ or かえんの息 or どくの息 or まじんぎり) 残りMP{m1mp}")
                elif pm == "スライムベス":
                    pa = input(f"入力(こうげき or ホイミ or バイキルト or ルカナン or  どくの息 or ラリホーマ or イオナズン or まじんぎり) 残りMP{m1mp}")
                else:
                    pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or まじんぎり) 残りMP{m1mp}")
                if pa == "こうげき":
                    dod1 = dod(m1, m2, 1)
                    print(f"{m1}のこうげき！")
                    if dod1 == True:
                        print("回避成功")
                        m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                        print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())
                    else:
                        crip = random.randint(1, 32)
                        if crip == 1:
                            dmg = cri(m1)
                            dc2[m2]["HP"] -= dmg
                            print(f"{dmg}damage かいしんのいちげき！")
                            m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                            print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                            if dc2[m2]["HP"] <= 0:
                                print(f"{m2}のHPは0になってしまった... out")
                                dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                if "キングスライム" in alive_monsters:
                                    print(mhplik())
                                else:
                                    print(mhpli())
                                alive_monsters.remove(m2)
                                mc += 1
                                if mc == 4:
                                    winner = m1
                                    break
                            else:
                                af = random.randint(0, 1)
                        else:
                            dmg = d(m1, m2)
                            dc2[m2]["HP"] -= dmg
                            print(f"{dmg}damage")
                            m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                            print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                            if dc2[m2]["HP"] <= 0:
                                print(f"{m2}のHPは0になってしまった... out")
                                dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                if "キングスライム" in alive_monsters:
                                    print(mhplik())
                                else:
                                    print(mhpli())                            
                                alive_monsters.remove(m2)
                                mc += 1
                                if mc == 4:
                                    winner = m1
                                    break
                            else:
                                af = random.randint(0, 1)
                elif pa == "ホイミ":
                    print(f"{m1}はホイミをつかった！")
                    if m1mp >= 4:
                        dc2[m1]["HP"] += 10
                        if dc2[m1]["HP"] > primitive_dc[m1]["HP"]:
                            while dc2[m1]["HP"] > primitive_dc[m1]["HP"]:
                                dc2[m1]["HP"] -= 1
                                if dc2[m1]["HP"] == primitive_dc[m1]["HP"]:
                                    break
                        dc2[m1]["MP"] -= 4
                        print(f"{m1}はHPを10回復した")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())                    
                    else:
                        print("MPがたりない！")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())
                elif pa == "どくの息":
                    print(f"{m1}はどくの息をつかった！")
                    if m1mp >= 4:
                        dc2[m1]["MP"] -= 4
                        liaa = aselect(m1)
                        ac = 0
                        while ac < len(liaa):
                            dod1 = dod(m1, liaa[ac], 1/3)
                            if dod1 == True:
                                print(f"{liaa[ac]}はどくの息をかわした！  ")
                                m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                print(f"{m2s}の残りHP{m2hp}!  ")
                                ac += 1
                                if "キングスライム" in alive_monsters:
                                    print(mhplik())
                                else:
                                    print(mhpli())
                            else:
                                jli = list(dc2[liaa[ac]]['CON'].keys())
                                if len(jli) == 1:
                                    if jli[0] == "どく" or jli[0] == "げんき":
                                        dc2[liaa[ac]]["CON"] = {"どく": 1}
                                    else:
                                        dc2[liaa[ac]]["CON"]["どく"] = 1
                                elif len(jli) == 2:
                                    dc2[liaa[ac]]["CON"]["どく"] = 1
                                print(f"{liaa[ac]}はどくになってしまった  ")
                                m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                print(f"{m2s}の残りHP{m2hp}")
                                ac += 1
                    else:
                        print("MPがたりない！")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())
                elif pa == "ラリホーマ":
                    print(f"{m1}はラリホーマをつかった！")
                    if m1mp >= 4:
                        dc2[m1]["MP"] -= 4
                        liaa = aselect(m1)
                        ac = 0
                        while ac < len(liaa):
                            dod1 = dod(m1, liaa[ac], 1)
                            if dod1 == True:
                                print(f"{liaa[ac]}はラリホーマをかわした！  ")
                                m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                print(f"{m2s}の残りHP{m2hp}!  ")
                                ac += 1
                                if "キングスライム" in alive_monsters:
                                    print(mhplik())
                                else:
                                    print(mhpli())
                            else:
                                jli = list(dc2[liaa[ac]]['CON'].keys())
                                if len(jli) == 1:
                                    if jli[0] == "ねむり" or jli[0] == "げんき":
                                        dc2[liaa[ac]]["CON"] = {"ねむり": 1}
                                    else:
                                        dc2[liaa[ac]]["CON"]["ねむり"] = 1
                                elif len(jli) == 2:
                                    dc2[liaa[ac]]["CON"]["ねむり"] = 1
                                print(f"{liaa[ac]}はねむってしまった  ", end = "")
                                m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                print(f"{m2s}の残りHP{m2hp}")
                                ac += 1
                    else:
                        print("MPがたりない！")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())
                elif pa == "バイキルト":
                    print(f"{m1}はバイキルトをつかった！")
                    if m1mp >= 4:
                        dc2[m1]["MP"] -= 4
                        print(f"{m1}の攻撃力は2倍になった！")
                        if dc2[m1]["BfDbf"]["bk"] == 0:
                            dc2[m1]["ATK"] *= 2
                        dc2[m1]["BfDbf"]["bk"] = 1
                    else:
                        print("MPがたりない！")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())
                elif pa == "ルカナン":
                    print(f"{m1}はルカナンをつかった！")
                    if m1mp >= 4:
                        dc2[m1]["MP"] -= 4
                        lcli = aselect(m1)
                        lcc = 0
                        while lcc < len(lcli):
                            defd = primitive_dc[lcli[lcc]]["DEF"]*2//10
                            print(f"{lcli[lcc]}の守備力が減少した！")
                            if dc2[lcli[lcc]]["BfDbf"]["rk"] == 0:
                                dc2[lcli[lcc]]["DEF"] -= defd
                                dc2[lcli[lcc]]["BfDbf"]["rk"] = 1
                            elif (not(dc2[lcli[lcc]]["BfDbf"]["rk"] == 0)) and (not(dc2[lcli[lcc]]["DEF"] == primitive_dc[lcli[lcc]]["DEF"]-2*defd)):
                                dc2[lcli[lcc]]["DEF"] -= defd
                                dc2[lcli[lcc]]["BfDbf"]["rk"] = 1
                            else:
                                dc2[lcli[lcc]]["BfDbf"]["rk"] = 1
                            lcc += 1
                    else:
                        print("MPがたりない！")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())              
                elif (not(pm == "スライムベス")) and (pa == "メラ"):
                    print(f"{m1}はメラをつかった！")
                    crip = random.randint(1, 32)
                    if m1mp >= 4:
                        dc2[m1]["MP"] -= 4
                        dod1 = dod(m1, m2, 3/2)
                        if dod1 == True:
                            print("回避成功")
                            m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                            print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　")
                            if "キングスライム" in alive_monsters:
                                print(mhplik())
                            else:
                                print(mhpli())
                        else:
                            if crip == 1:
                                dmg = cri(m1)*3//2
                                dc2[m2]["HP"] -= dmg
                                print(f"{dmg}damage かいしんのいちげき！")
                                m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                                print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                if dc2[m2]["HP"] <= 0:
                                    print(f"{m2}のHPは0になってしまった... out")
                                    dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                    if "キングスライム" in alive_monsters:
                                        print(mhplik())
                                    else:
                                        print(mhpli())                        
                                    alive_monsters.remove(m2)
                                    mc += 1
                                    if mc == 4:
                                        winner = m1
                                        break
                                else:
                                    af = random.randint(0, 1)
                            else:                     
                                dmg = md(m1, m2, 1)
                                dc2[m2]["HP"] -= dmg
                                print(f"{dmg}damage")
                                m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                                print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                if dc2[m2]["HP"] <= 0:
                                    print(f"{m2}のHPは0になってしまった... out")
                                    dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                    if "キングスライム" in alive_monsters:
                                        print(mhplik())
                                    else:
                                        print(mhpli())
                                    alive_monsters.remove(m2)
                                    mc += 1
                                    if mc == 4:
                                        winner = m1
                                        break
                                else:
                                    af = random.randint(0, 1)
                    else:
                        print("MPがたりない！")
                    if "キングスライム" in alive_monsters:
                        print(mhplik())
                    else:
                        print(mhpli())
                elif (pa == "ベホマ") and (pm == "ベホマスライム"):
                    print(f"{m1}はベホマをつかった！")
                    if m1mp >= 6:
                        while dc2[m1]["HP"] < primitive_dc[m1]["HP"]:
                            dc2[m1]["HP"] += 1
                            if dc2[m1]["HP"] == primitive_dc[m1]["HP"]:
                                break
                        dc2[m1]["MP"] -= 6
                        print(f"{m1}はHPを全回復した")
                    else:
                        print("MPがたりない！")
                    if "キングスライム" in alive_monsters:
                        print(mhplik())
                    else:
                        print(mhpli())
                elif (pa == "キアリー") and (pm == "ベホマスライム"):
                    print(f"{m1}はキアリーをつかった！")
                    if m1mp >= 4 :
                        dc2[m1]["CON"] = {"げんき": 1}
                        dc2[m1]["MP"] -= 4
                        print(f"{m1}は状態異常を全回復した")
                    else:
                        print("MPがたりない！")
                    if "キングスライム" in alive_monsters:
                        print(mhplik())
                    else:
                        print(mhpli())
                elif (pm == "スライムLv8") and (not(sc == 8)) and (pa == "なかまをよぶ"):
                    sc += 1 #確率で失敗
                    print(f"スライムLv8はなかまをよんだ スライムLv8の数{sc}")
                    # dc2[f"スライムLv8({sc})"] = {li[i] for i in range(len(li)-1)}; dc2[f"スライムLv8{sc}"]["Lv"] = divmod((dc2[f"スライムLv8{sc}"]["HP"] + dc2[f"スライムLv8{sc}"]["MP"] + dc2[f"スライムLv8{sc}"]["ATK"] + dc2[f"スライムLv8{sc}"]["DEF"] + dc2[f"スライムLv8{sc}"]["SPD"] + dc2[f"スライムLv8{sc}"]["MAG"]), 10)[0]
                elif (pm == "スライムLv8") and (sc == 8) and (pa == "合体"):
                    print("スライムLv8たちが合体していく！")
                    print("キングスライムがあらわれた！")
                    primitive_dc["キングスライム"] = {li[i]: random.randint(100, 150) for i in range(len(li)-1)}
                    primitive_dc["キングスライム"]["Lv"] = divmod((primitive_dc["キングスライム"]["HP"] + primitive_dc["キングスライム"]["MP"] + primitive_dc[f"キングスライム"]["ATK"] + primitive_dc[f"キングスライム"]["DEF"] + primitive_dc[f"キングスライム"]["SPD"] + primitive_dc["キングスライム"]["MAG"]), 10)[0]
                    dc2["キングスライム"] = copy.deepcopy(primitive_dc["キングスライム"])
                    alive_monsters.remove("スライムLv8")
                    alive_monsters.append("キングスライム")
                    print(mhplik())
                elif (pm == "ドラゴスライム") and (pa == "かえんの息"):
                    print(f"{m1}はかえんの息をつかった！")
                    liaa = aselect(m1)
                    ac = 0
                    while ac < len(liaa):
                        dod1 = dod(m1, liaa[ac], 2)
                        if dod1 == True:
                            print(f"{liaa[ac]}はかえんの息をかわした！  ")
                            m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                            print(f"{m2s}の残りHP{m2hp}!  ")
                            ac += 1
                            if "キングスライム" in alive_monsters:
                                print(mhplik())
                            else:
                                print(mhpli())
                        else:
                            crip = random.randint(1, 32)
                            if crip == 1:
                                dmg = cri(m1)*3//2
                                dc2[liaa[ac]]["HP"] -= dmg
                                print(f"{liaa[ac]}に{dmg}damage かいしんのいちげき！  ")
                                m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                print(f"{m2s}の残りHP{m2hp}")
                                ac += 1
                                if dc2[m2s]["HP"] <= 0:
                                    print(f"{m2s}のHPは0になってしまった... out")
                                    dc2[m2s]["HP"] = 0; dc2[m2s]["CON"] = {"ひんし": 1}
                                    if "キングスライム" in alive_monsters:
                                        print(mhplik())
                                    else:
                                        print(mhpli())
                                    alive_monsters.remove(m2s)
                                    mc += 1
                                    if mc == 4:
                                        winner = m1
                                        break
                                else:
                                    af = random.randint(0, 1)
                            else:
                                dmg = md(m1, liaa[ac], 1)
                                dc2[liaa[ac]]["HP"] -= dmg
                                print(f"{liaa[ac]}に{dmg}damage  ")
                                m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                print(f"{m2s}の残りHP{m2hp}")
                                ac += 1
                                if dc2[m2s]["HP"] <= 0:
                                    print(f"{m2s}のHPは0になってしまった... out")
                                    dc2[m2s]["HP"] = 0; dc2[m2s]["CON"] = {"ひんし": 1}
                                    if "キングスライム" in alive_monsters:
                                        print(mhplik())
                                    else:
                                        print(mhpli())
                                    alive_monsters.remove(m2s)
                                    mc += 1
                                    if mc == 4:
                                        winner = m1
                                        break
                                else:
                                    af = random.randint(0, 1)
                elif (pm == "スライムベス") and (pa == "イオナズン"):
                    print(f"{m1}はイオナズンをつかった！")
                    if m1mp >= 25:
                        dc2[m1]["MP"] -= 25
                        liaa = aselect(m1)
                        ac = 0
                        while ac < len(liaa):
                            dod1 = dod(m1, liaa[ac], 3)
                            if dod1 == True:
                                print(f"{liaa[ac]}はイオナズンをかわした！  ")
                                m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                print(f"{m2s}の残りHP{m2hp}!  ")
                                ac += 1
                                if "キングスライム" in alive_monsters:
                                    print(mhplik())
                                else:
                                    print(mhpli())
                            else:
                                crip = random.randint(1, 32)
                                if crip == 1:
                                    dmg = cri(m1)*3//2
                                    dc2[liaa[ac]]["HP"] -= dmg
                                    print(f"{liaa[ac]}に{dmg}damage かいしんのいちげき！  ")
                                    m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                    print(f"{m2s}の残りHP{m2hp}")
                                    ac += 1
                                    if dc2[m2s]["HP"] <= 0:
                                        print(f"{m2s}のHPは0になってしまった... out")
                                        dc2[m2s]["HP"] = 0; dc2[m2s]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in alive_monsters:
                                            print(mhplik())
                                        else:
                                            print(mhpli())
                                        alive_monsters.remove(m2s)
                                        mc += 1
                                        if mc == 4:
                                            winner = m1
                                            break
                                    else:
                                        af = random.randint(0, 1)
                                else:
                                    dmg = md(m1, liaa[ac], 3)
                                    dc2[liaa[ac]]["HP"] -= dmg
                                    print(f"{liaa[ac]}に{dmg}damage  ")
                                    m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                    print(f"{m2s}の残りHP{m2hp}")
                                    ac += 1
                                    if dc2[m2s]["HP"] <= 0:
                                        print(f"{m2s}のHPは0になってしまった... out")
                                        dc2[m2s]["HP"] = 0; dc2[m2s]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in alive_monsters:
                                            print(mhplik())
                                        else:
                                            print(mhpli())
                                        alive_monsters.remove(m2s)
                                        mc += 1
                                        if mc == 4:
                                            winner = m1
                                            break
                                    else:
                                        af = random.randint(0, 1)
                    else:
                        print("MPがたりない！")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())
                elif pa == "まじんぎり":
                    print(f"{m1}はまじんぎりをつかった！")
                    dod1 = dod(m1, m2, 1)
                    if dod1 == True:
                        print("回避成功")
                        af = random.randint(0, 1)
                        m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                        print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())                    
                    else:
                        mpro = random.randint(0, 1)
                        if mpro == 0:
                            print("ミス")
                        else:
                            crip = random.randint(1, 32)
                            if crip == 1:
                                dmg = cri(m1)*2
                                dc2[m2]["HP"] -= dmg
                                print(f"{dmg}damage かいしんのいちげき！")
                                m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                                print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                if dc2[m2]["HP"] <= 0:
                                    print(f"{m2}のHPは0になってしまった... out")
                                    dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                    if "キングスライム" in alive_monsters:
                                        print(mhplik())
                                    else:
                                        print(mhpli())
                                    alive_monsters.remove(m2)
                                    mc += 1
                                    if mc == 4:
                                        winner = m1
                                        break
                                else:
                                    af = random.randint(0, 1)
                            else:                     
                                dmg = d(m1, m2)*2
                                dc2[m2]["HP"] -= dmg
                                print(f"{dmg}damage")
                                m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                                print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                if dc2[m2]["HP"] <= 0:
                                    print(f"{m2}のHPは0になってしまった... out")
                                    dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                    if "キングスライム" in alive_monsters:
                                        print(mhplik())
                                    else:
                                        print(mhpli())                                
                                    alive_monsters.remove(m2)
                                    mc += 1
                                    if mc == 4:
                                        winner = m1
                                        break
                                else:
                                    af = random.randint(0, 1)         
                else:
                    print("有効なコマンドを入力してください")
                    if pm == "ベホマスライム":
                        pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or キアリー or ベホマ or まじんぎり) 残りMP{m1mp}")
                    elif pm == "スライムLv8":
                        if sc == 8:
                            pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or 合体 or まじんぎり ) 残りMP{m1mp}")
                        else:
                            pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or なかまをよぶ or まじんぎり　) 残りMP{m1mp}")
                    elif pm == "キングスライム":
                        pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or ラリホーマ or どくの息 or まじんぎり) 残りMP{m1mp}")
                    elif pm == "ドラゴスライム":
                        pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or ラリホーマ or かえんの息 or どくの息 or まじんぎり) 残りMP{m1mp}")
                    elif pm == "スライムベス":
                        pa = input(f"入力(こうげき or ホイミ or バイキルト or ルカナン or  どくの息 or ラリホーマ or イオナズン or まじんぎり) 残りMP{m1mp}")
                    else:
                        pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or まじんぎり) 残りMP{m1mp}")     

            else:
                m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]; m1mp = dc2[m1]["MP"]
                print(f"{m1}→{m2}")
                pa = input("Attack!")
                if not(pa == "no"):
                    if m1 == "ベホマスライム":
                        na = random.randint(0, 9)
                    elif m1 == "スライムLv8" or  m1 == "ドラゴスライム":
                        na = random.randint(0, 8)
                    else:
                        na = random.randint(0, 7)
                    if na == 0:
                        print(f"{m1}のこうげき！")
                        dod1 = dod(m1, m2, 1)
                        if dod1 == True:
                            print("回避成功")
                            m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                            print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　")
                            if "キングスライム" in alive_monsters:
                                print(mhplik())
                            else:
                                print(mhpli())
                        else:
                            crip = random.randint(1, 32)
                            if crip == 1:
                                dmg = cri(m1)
                                dc2[m2]["HP"] -= dmg
                                print(f"{dmg}damage かいしんのいちげき！")
                                m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                                print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                if dc2[m2]["HP"] <= 0:
                                    print(f"{m2}のHPは0になってしまった... out")
                                    dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                    if "キングスライム" in alive_monsters:
                                        print(mhplik())
                                    else:
                                        print(mhpli())
                                    alive_monsters.remove(m2)
                                    mc += 1
                                    if mc == 4:
                                        winner = m1
                                        break
                                else:
                                    af = random.randint(0, 1)
                            else:
                                dmg = d(m1, m2)
                                dc2[m2]["HP"] -= dmg
                                print(f"{dmg}damage")
                                m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                                print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                if dc2[m2]["HP"] <= 0:
                                    print(f"{m2}のHPは0になってしまった... out")
                                    dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                    if "キングスライム" in alive_monsters:
                                        print(mhplik())
                                    else:
                                        print(mhpli())                            
                                    alive_monsters.remove(m2)
                                    mc += 1
                                    if mc == 4:
                                        winner = m1
                                        break
                                else:
                                    af = random.randint(0, 1)
                    elif na == 1:
                        print(f"{m1}はホイミをつかった！")
                        if m1mp >= 10 :
                            dc2[m1]["HP"] += 10
                            if dc2[m1]["HP"] > primitive_dc[m1]["HP"]:
                                while dc2[m1]["HP"] > primitive_dc[m1]["HP"]:
                                    dc2[m1]["HP"] -= 1
                                    if dc2[m1]["HP"] == primitive_dc[m1]["HP"]:
                                        break
                            dc2[m1]["MP"] -= 10
                            print(f"{m1}はHPを10回復した")
                            if "キングスライム" in alive_monsters:
                                print(mhplik())
                            else:
                                print(mhpli())                    
                        else:
                            print("MPがたりない！")
                            if "キングスライム" in alive_monsters:
                                print(mhplik())
                            else:
                                print(mhpli())
                    elif na == 2:
                        print(f"{m1}はどくの息をつかった！")
                        if m1mp >= 4:
                            dc2[m1]["MP"] -= 4
                            liaa = aselect(m1)
                            ac = 0
                            while ac < len(liaa):
                                dod1 = dod(m1, liaa[ac], 1/3)
                                if dod1 == True:
                                    print(f"{liaa[ac]}はどくの息をかわした！  ")
                                    m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                    print(f"{m2s}の残りHP{m2hp}!  ")
                                    ac += 1
                                    if "キングスライム" in alive_monsters:
                                        print(mhplik())
                                    else:
                                        print(mhpli())
                                else:
                                    jli = list(dc2[liaa[ac]]['CON'].keys())
                                    if len(jli) == 1:
                                        if jli[0] == "どく" or jli[0] == "げんき":
                                            dc2[liaa[ac]]["CON"] = {"どく": 1}
                                        else:
                                            dc2[liaa[ac]]["CON"]["どく"] = 1
                                    elif len(jli) == 2:
                                        dc2[liaa[ac]]["CON"]["どく"] = 1
                                    print(f"{liaa[ac]}はどくになってしまった  ")
                                    m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                    print(f"{m2s}の残りHP{m2hp}")
                                    ac += 1
                        else:
                            print("MPがたりない！")
                            if "キングスライム" in alive_monsters:
                                print(mhplik())
                            else:
                                print(mhpli())
                    elif na == 3:
                        print(f"{m1}はラリホーマをつかった！")
                        if m1mp >= 4:
                            dc2[m1]["MP"] -= 4
                            liaa = aselect(m1)
                            ac = 0
                            while ac < len(liaa):
                                dod1 = dod(m1, liaa[ac], 1)
                                if dod1 == True:
                                    print(f"{liaa[ac]}はラリホーマをかわした！  ")
                                    m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                    print(f"{m2s}の残りHP{m2hp}!  ")
                                    ac += 1
                                    if "キングスライム" in alive_monsters:
                                        print(mhplik())
                                    else:
                                        print(mhpli())
                                else:
                                    jli = list(dc2[liaa[ac]]['CON'].keys())
                                    if len(jli) == 1:
                                        if jli[0] == "ねむり" or jli[0] == "げんき":
                                            dc2[liaa[ac]]["CON"] = {"ねむり": 1}
                                        else:
                                            dc2[liaa[ac]]["CON"]["ねむり"] = 1
                                    elif len(jli) == 2:
                                        dc2[liaa[ac]]["CON"]["ねむり"] = 1
                                    print(f"{liaa[ac]}はねむってしまった  ", end = "")
                                    m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                    print(f"{m2s}の残りHP{m2hp}")
                                    ac += 1
                        else:
                            print("MPがたりない！")
                            if "キングスライム" in alive_monsters:
                                print(mhplik())
                            else:
                                print(mhpli())
                    elif na == 4:
                        print(f"{m1}はバイキルトをつかった！")
                        if m1mp >= 4:
                            dc2[m1]["MP"] -= 4
                            print(f"{m1}の攻撃力は2倍になった！")
                            if dc2[m1]["BfDbf"]["bk"] == 0:
                                dc2[m1]["ATK"] *= 2
                            dc2[m1]["BfDbf"]["bk"] = 1
                        else:
                            print("MPがたりない！")
                            if "キングスライム" in alive_monsters:
                                print(mhplik())
                            else:
                                print(mhpli())
                    elif na == 5:
                        print(f"{m1}はルカナンをつかった！")
                        if m1mp >= 4:
                            dc2[m1]["MP"] -= 4
                            lcli = aselect(m1)
                            lcc = 0
                            while lcc < len(lcli):
                                defd = primitive_dc[lcli[lcc]]["DEF"]*2//10
                                print(f"{lcli[lcc]}の守備力が減少した！")
                                if dc2[lcli[lcc]]["BfDbf"]["rk"] == 0:
                                    dc2[lcli[lcc]]["DEF"] -= defd
                                    dc2[lcli[lcc]]["BfDbf"]["rk"] = 1
                                elif (not(dc2[lcli[lcc]]["BfDbf"]["rk"] == 0)) and (not(dc2[lcli[lcc]]["DEF"] == primitive_dc[lcli[lcc]]["DEF"]-2*defd)):
                                    dc2[lcli[lcc]]["DEF"] -= defd
                                    dc2[lcli[lcc]]["BfDbf"]["rk"] = 1
                                else:
                                    dc2[lcli[lcc]]["BfDbf"]["rk"] = 1
                                lcc += 1

                        else:
                            print("MPがたりない！")
                            if "キングスライム" in alive_monsters:
                                print(mhplik())
                            else:
                                print(mhpli())              
                    elif (not(m1 == "スライムベス")) and (na == 6):
                        print(f"{m1}はメラをつかった！")
                        crip = random.randint(1, 32)
                        if m1mp >= 4:
                            dc2[m1]["MP"] -= 4
                            dod1 = dod(m1, m2, 3/2)
                            if dod1 == True:
                                print("回避成功")
                                m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                                print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　")
                                if "キングスライム" in alive_monsters:
                                    print(mhplik())
                                else:
                                    print(mhpli())
                            else:
                                if crip == 1:
                                    dmg = cri(m1)*3//2
                                    dc2[m2]["HP"] -= dmg
                                    print(f"{dmg}damage かいしんのいちげき！")
                                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                    if dc2[m2]["HP"] <= 0:
                                        print(f"{m2}のHPは0になってしまった... out")
                                        dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in alive_monsters:
                                            print(mhplik())
                                        else:
                                            print(mhpli())                        
                                        alive_monsters.remove(m2)
                                        mc += 1
                                        if mc == 4:
                                            winner = m1
                                            break
                                    else:
                                        af = random.randint(0, 1)
                                else:                     
                                    dmg = md(m1, m2, 1)
                                    dc2[m2]["HP"] -= dmg
                                    print(f"{dmg}damage")
                                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                    if dc2[m2]["HP"] <= 0:
                                        print(f"{m2}のHPは0になってしまった... out")
                                        dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in alive_monsters:
                                            print(mhplik())
                                        else:
                                            print(mhpli())
                                        alive_monsters.remove(m2)
                                        mc += 1
                                        if mc == 4:
                                            winner = m1
                                            break
                                    else:
                                        af = random.randint(0, 1)
                        else:
                            print("MPがたりない！")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())
                    elif (na == 9) and (m1 == "ベホマスライム"):
                        print(f"{m1}はベホマをつかった！")
                        if m1mp >= 6 :
                            while dc2[m1]["HP"] < primitive_dc[m1]["HP"]:
                                dc2[m1]["HP"] += 1
                                if dc2[m1]["HP"] == primitive_dc[m1]["HP"]:
                                    break
                            dc2[m1]["MP"] -= 6
                            print(f"{m1}はHPを全回復した")
                        else:
                            print("MPがたりない！")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())
                    elif (na == 8) and (m1 == "ベホマスライム"):
                        print(f"{m1}はキアリーをつかった！")
                        if m1mp >= 4 :
                            dc2[m1]["CON"] = {"げんき": 1}
                            dc2[m1]["MP"] -= 4
                            print(f"{m1}は状態異常を全回復した")
                        else:
                            print("MPがたりない！")
                        if "キングスライム" in alive_monsters:
                            print(mhplik())
                        else:
                            print(mhpli())
                    elif (m1 == "スライムLv8") and (not(sc == 8)) and (na == 8):
                        sc += 1 #確率で失敗
                        print(f"スライムLv8はなかまをよんだ スライムLv8の数{sc}")
                        # dc2[f"スライムLv8({sc})"] = {li[i] for i in range(len(li)-1)}; dc2[f"スライムLv8{sc}"]["Lv"] = divmod((dc2[f"スライムLv8{sc}"]["HP"] + dc2[f"スライムLv8{sc}"]["MP"] + dc2[f"スライムLv8{sc}"]["ATK"] + dc2[f"スライムLv8{sc}"]["DEF"] + dc2[f"スライムLv8{sc}"]["SPD"] + dc2[f"スライムLv8{sc}"]["MAG"]), 10)[0]
                    elif (m1 == "スライムLv8") and (sc == 8) and (na == 8):
                        print("スライムLv8たちが合体していく！")
                        print("キングスライムがあらわれた！")
                        primitive_dc["キングスライム"] = {li[i]: random.randint(100, 150) for i in range(len(li)-1)}
                        primitive_dc["キングスライム"]["Lv"] = divmod((primitive_dc["キングスライム"]["HP"] + primitive_dc["キングスライム"]["MP"] + primitive_dc[f"キングスライム"]["ATK"] + primitive_dc[f"キングスライム"]["DEF"] + primitive_dc[f"キングスライム"]["SPD"] + primitive_dc["キングスライム"]["MAG"]), 10)[0]
                        dc2["キングスライム"] = copy.deepcopy(primitive_dc["キングスライム"])
                        alive_monsters.remove("スライムLv8")
                        alive_monsters.append("キングスライム")
                        print(mhplik())
                    elif (m1 == "ドラゴスライム") and (na == 8):
                        print(f"{m1}はかえんの息をつかった！")
                        liaa = aselect(m1)
                        ac = 0
                        while ac < len(liaa):
                            dod1 = dod(m1, liaa[ac], 2)
                            if dod1 == True:
                                print(f"{liaa[ac]}はかえんの息をかわした！  ")
                                m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                print(f"{m2s}の残りHP{m2hp}!  ")
                                ac += 1
                                if "キングスライム" in alive_monsters:
                                    print(mhplik())
                                else:
                                    print(mhpli())
                            else:
                                crip = random.randint(1, 32)
                                if crip == 1:
                                    dmg = cri(m1)*3//2
                                    dc2[liaa[ac]]["HP"] -= dmg
                                    print(f"{liaa[ac]}に{dmg}damage かいしんのいちげき！  ")
                                    m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                    print(f"{m2s}の残りHP{m2hp}")
                                    ac += 1
                                    if dc2[m2s]["HP"] <= 0:
                                        print(f"{m2s}のHPは0になってしまった... out")
                                        dc2[m2s]["HP"] = 0; dc2[m2s]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in alive_monsters:
                                            print(mhplik())
                                        else:
                                            print(mhpli())
                                        alive_monsters.remove(m2s)
                                        mc += 1
                                        if mc == 4:
                                            winner = m1
                                            break
                                    else:
                                        af = random.randint(0, 1)
                                else:
                                    dmg = md(m1, liaa[ac], 1)
                                    dc2[liaa[ac]]["HP"] -= dmg
                                    print(f"{liaa[ac]}に{dmg}damage  ")
                                    m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                    print(f"{m2s}の残りHP{m2hp}")
                                    ac += 1
                                    if dc2[m2s]["HP"] <= 0:
                                        print(f"{m2s}のHPは0になってしまった... out")
                                        dc2[m2s]["HP"] = 0; dc2[m2s]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in alive_monsters:
                                            print(mhplik())
                                        else:
                                            print(mhpli())
                                        alive_monsters.remove(m2s)
                                        mc += 1
                                        if mc == 4:
                                            winner = m1
                                            break
                                    else:
                                        af = random.randint(0, 1)
                    elif (m1 == "スライムベス") and (na == 6):
                        print(f"{m1}はイオナズンをつかった！")
                        if m1mp >= 25:
                            dc2[m1]["MP"] -= 25
                            liaa = aselect(m1)
                            ac = 0
                            while ac < len(liaa):
                                dod1 = dod(m1, liaa[ac], 3)
                                if dod1 == True:
                                    print(f"{liaa[ac]}はイオナズンをかわした！  ")
                                    m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                    print(f"{m2s}の残りHP{m2hp}!  ")
                                    ac += 1
                                    if "キングスライム" in alive_monsters:
                                        print(mhplik())
                                    else:
                                        print(mhpli())
                                else:
                                    crip = random.randint(1, 32)
                                    if crip == 1:
                                        dmg = cri(m1)*3//2
                                        dc2[liaa[ac]]["HP"] -= dmg
                                        print(f"{liaa[ac]}に{dmg}damage かいしんのいちげき！  ")
                                        m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                        print(f"{m2s}の残りHP{m2hp}")
                                        ac += 1
                                        if dc2[m2s]["HP"] <= 0:
                                            print(f"{m2s}のHPは0になってしまった... out")
                                            dc2[m2s]["HP"] = 0; dc2[m2s]["CON"] = {"ひんし": 1}
                                            if "キングスライム" in alive_monsters:
                                                print(mhplik())
                                            else:
                                                print(mhpli())
                                            alive_monsters.remove(m2s)
                                            mc += 1
                                            if mc == 4:
                                                winner = m1
                                                break
                                        else:
                                            af = random.randint(0, 1)
                                    else:
                                        dmg = md(m1, liaa[ac], 3)
                                        dc2[liaa[ac]]["HP"] -= dmg
                                        print(f"{liaa[ac]}に{dmg}damage  ")
                                        m1hp = dc2[m1]["HP"]; m2s = liaa[ac]; m2hp = dc2[liaa[ac]]["HP"]
                                        print(f"{m2s}の残りHP{m2hp}")
                                        ac += 1
                                        if dc2[m2s]["HP"] <= 0:
                                            print(f"{m2s}のHPは0になってしまった... out")
                                            dc2[m2s]["HP"] = 0; dc2[m2s]["CON"] = {"ひんし": 1}
                                            if "キングスライム" in alive_monsters:
                                                print(mhplik())
                                            else:
                                                print(mhpli())
                                            alive_monsters.remove(m2s)
                                            mc += 1
                                            if mc == 4:
                                                winner = m1
                                                break
                                        else:
                                            af = random.randint(0, 1)
                        else:
                            print("MPがたりない！")
                            if "キングスライム" in alive_monsters:
                                print(mhplik())
                            else:
                                print(mhpli())
                    elif na == 7:
                        print(f"{m1}はまじんぎりをつかった！")
                        dod1 = dod(m1, m2, 1)
                        if dod1 == True:
                            print("回避成功")
                            af = random.randint(0, 1)
                            m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                            print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　")
                            if "キングスライム" in alive_monsters:
                                print(mhplik())
                            else:
                                print(mhpli())                    
                        else:
                            mpro = random.randint(0, 1)
                            if mpro == 0:
                                print("ミス")
                            else:
                                crip = random.randint(1, 32)
                                if crip == 1:
                                    dmg = cri(m1)*2
                                    dc2[m2]["HP"] -= dmg
                                    print(f"{dmg}damage かいしんのいちげき！")
                                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                    if dc2[m2]["HP"] <= 0:
                                        print(f"{m2}のHPは0になってしまった... out")
                                        dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in alive_monsters:
                                            print(mhplik())
                                        else:
                                            print(mhpli())
                                        alive_monsters.remove(m2)
                                        mc += 1
                                        if mc == 4:
                                            winner = m1
                                            break
                                    else:
                                        af = random.randint(0, 1)
                                else:                     
                                    dmg = d(m1, m2)*2
                                    dc2[m2]["HP"] -= dmg
                                    print(f"{dmg}damage")
                                    m1hp = dc2[mons1]["HP"]; m2hp = dc2[mons2]["HP"]
                                    print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                    if dc2[m2]["HP"] <= 0:
                                        print(f"{m2}のHPは0になってしまった... out")
                                        dc2[m2]["HP"] = 0; dc2[m2]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in alive_monsters:
                                            print(mhplik())
                                        else:
                                            print(mhpli())                                
                                        alive_monsters.remove(m2)
                                        mc += 1
                                        if mc == 4:
                                            winner = m1
                                            break
                                    else:
                                        af = random.randint(0, 1)         

        if "キングスライム" in alive_monsters:
            dk = 0
            while dk < 5:
                jli = list(dc2[li3[dk]]['CON'].keys())
                if len(jli) > 0:
                    if len(jli) > 1:
                        if jli[0] == "どく" or jli[1] == "どく":
                            dc2[li3[dk]]["HP"] -= primitive_dc[li3[dk]]["HP"]//10
                            dm = li3[dk]; dd = primitive_dc[li3[dk]]["HP"]//10
                            print(f"{dm}はどくで{dd}ダメージをうけた")
                            if dc2[dm]["HP"] <= 0:
                                print(f"{dm}のHPは0になってしまった... out")
                                dc2[dm]["HP"] = 0; dc2[dm]["CON"] = {"ひんし": 1}
                                print(mhplik())
                                alive_monsters.remove(dm)
                                mc += 1
                                if mc == 4:
                                    winner = alive_monsters[0]
                                    break
                            if (not(dc2[dm]["CON"] == {"ひんし": 1})):
                                p = dc2[dm]["CON"]["どく"]
                                kp = random.randint(1, 10)
                                if kp <= p:
                                    print(f"{dm}はどくからかいふくした")
                                    del dc2[dm]["CON"]["どく"]
                                else:
                                    if dc2[dm]["CON"]["どく"] < 5:
                                        dc2[dm]["CON"]["どく"] += 1
                            dk += 1
                        if jli[0] == "ねむり" or jli[1] == "ねむり":
                            dm = li3[dk]
                            sl = dc2[dm]["CON"]["ねむり"]
                            ksl = random.randint(1, 10)
                            if ksl <= sl:
                                print(f"{dm}はねむりからかいふくした")
                                del dc2[dm]["CON"]["ねむり"]
                            else:
                                if dc2[dm]["CON"]["ねむり"] < 5:
                                    dc2[dm]["CON"]["ねむり"] += 1
                        else:
                            dk += 1
                        
                    else:
                        if jli[0] == "どく":
                            dc2[li3[dk]]["HP"] -= primitive_dc[li3[dk]]["HP"]//10
                            dm = li3[dk]; dd = primitive_dc[li3[dk]]["HP"]//10
                            print(f"{dm}はどくで{dd}ダメージをうけた")
                            if dc2[dm]["HP"] <= 0:
                                print(f"{dm}のHPは0になってしまった... out")
                                dc2[dm]["HP"] = 0; dc2[dm]["CON"] = {"ひんし": 1}
                                print(mhplik())
                                alive_monsters.remove(dm)
                                mc += 1
                                if mc == 4:
                                    winner = alive_monsters[0]
                                    break
                            if (not(dc2[dm]["CON"] == {"ひんし": 1})):
                                p = dc2[dm]["CON"]["どく"]
                                kp = random.randint(1, 10)
                                if kp <= p:
                                    print(f"{dm}はどくからかいふくした")
                                    dc2[dm]["CON"] = {"げんき": 1}
                                else:
                                    if dc2[dm]["CON"]["どく"] < 5:
                                        dc2[dm]["CON"]["どく"] += 1
                            dk += 1
                        elif jli[0] == "ねむり":
                            dm = li3[dk]
                            sl = dc2[dm]["CON"]["ねむり"]
                            ksl = random.randint(1, 10)
                            if ksl <= sl:
                                print(f"{dm}はねむりからかいふくした")
                                dc2[dm]["CON"] = {"げんき": 1}
                            else:
                                if dc2[dm]["CON"]["ねむり"] < 5:
                                    dc2[dm]["CON"]["ねむり"] += 1
                        else:
                            dk += 1
        else:
            dk = 0
            while dk < 5:
                jli = list(dc2[li2[dk]]['CON'].keys())
                if len(jli) > 0:
                    if len(jli) > 1:
                        if jli[0] == "どく" or jli[1] == "どく":
                            dc2[li2[dk]]["HP"] -= primitive_dc[li2[dk]]["HP"]//10
                            dm = li2[dk]; dd = primitive_dc[li2[dk]]["HP"]//10
                            print(f"{dm}はどくで{dd}ダメージをうけた")
                            if dc2[dm]["HP"] <= 0:
                                print(f"{dm}のHPは0になってしまった... out")
                                dc2[dm]["HP"] = 0; dc2[dm]["CON"] = {"ひんし": 1}
                                print(mhpli())
                                alive_monsters.remove(dm)
                                mc += 1
                                if mc == 4:
                                    winner = alive_monsters[0]
                                    break
                            if (not(dc2[dm]["CON"] == {"ひんし": 1})):
                                p = dc2[dm]["CON"]["どく"]
                                kp = random.randint(1, 10)
                                if kp <= p:
                                    print(f"{dm}はどくからかいふくした")
                                    del dc2[dm]["CON"]["どく"]
                                else:
                                    if dc2[dm]["CON"]["どく"] < 5:
                                        dc2[dm]["CON"]["どく"] += 1
                            dk += 1
                        elif jli[0] == "ねむり" or jli[1] == "ねむり":
                            dm = li2[dk]
                            sl = dc2[dm]["CON"]["ねむり"]
                            ksl = random.randint(1, 10)
                            if ksl <= sl:
                                print(f"{dm}はねむりからかいふくした")
                                del dc2[dm]["CON"]["ねむり"]
                            else:
                                if dc2[dm]["CON"]["ねむり"] < 5:
                                    dc2[dm]["CON"]["ねむり"] += 1
                            dk += 1
                        else:
                            dk += 1
                    else:
                        if jli[0] == "どく":
                            dc2[li2[dk]]["HP"] -= primitive_dc[li2[dk]]["HP"]//10
                            dm = li2[dk]; dd = primitive_dc[li2[dk]]["HP"]//10
                            print(f"{dm}はどくで{dd}ダメージをうけた")
                            if dc2[dm]["HP"] <= 0:
                                print(f"{dm}のHPは0になってしまった... out")
                                dc2[dm]["HP"] = 0; dc2[dm]["CON"] = {"ひんし": 1}
                                print(mhpli())
                                alive_monsters.remove(dm)
                                mc += 1
                                if mc == 4:
                                    winner = alive_monsters[0]
                                    break
                            if (not(dc2[dm]["CON"] == {"ひんし": 1})):
                                p = dc2[dm]["CON"]["どく"]
                                kp = random.randint(1, 10)
                                if kp <= p:
                                    print(f"{dm}はどくからかいふくした")
                                    dc2[dm]["CON"] = {"げんき": 1}
                                else:
                                    if dc2[dm]["CON"]["どく"] < 5:
                                        dc2[dm]["CON"]["どく"] += 1
                            dk += 1
                        elif jli[0] == "ねむり":
                            dm = li2[dk]
                            sl = dc2[dm]["CON"]["ねむり"]
                            ksl = random.randint(1, 10)
                            if ksl <= sl:
                                print(f"{dm}はねむりからかいふくした")
                                dc2[dm]["CON"] = {"げんき": 1}
                            else:
                                if dc2[dm]["CON"]["ねむり"] < 5:
                                    dc2[dm]["CON"]["ねむり"] += 1
                            dk += 1
                        else:
                            dk += 1
        bd = 0
        while bd < len(alive_monsters):
            if (dc2[alive_monsters[bd]]["BfDbf"]["bk"] > 0) and (m1 == alive_monsters[bd]):
                dc2[alive_monsters[bd]]["BfDbf"]["bk"] += 1
                if dc2[alive_monsters[bd]]["BfDbf"]["bk"] == 4:
                    dc2[alive_monsters[bd]]["BfDbf"]["bk"] == 0
                    dc2[m1]["ATK"]//2
            if dc2[alive_monsters[bd]]["BfDbf"]["rk"] > 0:
                dc2[alive_monsters[bd]]["BfDbf"]["rk"] += 1
                if dc2[alive_monsters[bd]]["BfDbf"]["rk"] == 4:
                    dc2[alive_monsters[bd]]["BfDbf"]["rk"] == 0
                    drc = dc2[alive_monsters[bd]]["DEF"]
                    while drc < primitive_dc[alive_monsters[bd]]["DEF"]:
                        drc += 1
            bd += 1

    if (not(winner == None)) and (winner in dc2):
        wm = po*lvdc5[dc2[winner]["Lv"]]
        print(f"バトロワの勝者は {winner}")
        if pm == winner:
            print(f"あなたの勝ち  {wm}円 got")
        else:
            if (pm == "スライムLv8") and (winner == "キングスライム"):
                print(f"あなたの勝ち  {wm}円 got")
            else:
                print(f"あなたの負けです  {po}円 lost")
    else:
        print("error")
else:
    print("see you!")