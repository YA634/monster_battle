import random
import copy
import cre_mons

class Mons_battle():
    li = ["HP", "MP", "ATK", "DEF", "SPD", "MAG", "Lv", "CON"]
    li2 = ["スライムLv8", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
    li3 = ["キングスライム", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
    mc = 0
    sc = 1
    alive_monsters = ["スライムLv8", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
    def __init__(self, m_sta_dc):
        self.primitive_dc = m_sta_dc
        self.dc2 = copy.deepcopy(self.primitive_dc)
        self.dddc = {}
        self.odds_li = cre_mons.create_odds(self.dc2)


    def select(self, available_monsters):
        self.mli = []
        while len(self.mli) < 2:
            self.mons = random.choice(available_monsters)
            if not(self.mons in self.mli):
                self.mli.append(self.mons)
        self.mli2 = (self.mli[0], self.mli[1])
        return self.mli2

    def d(self, m1, m2):
        self.dmg1 = (self.dc2[m1]["ATK"] - (self.dc2[m2]["DEF"])//2)//2
        if self.dmg1 < 2:
            self.dmg2 = random.randint(0,1)
        elif 2 <= self.dmg1 < 9:
            self.dmg2 = random.randint(self.dmg1-2,self.dmg1)
        elif 9 <= self.dmg1:
            self.dmg2 = (self.dmg1*7)//8 + ((self.dmg1//4 + 1)*(random.randint(0,255)))//256
        return self.dmg2

    def md(self, m1, m2, x):
        self.dmg1 = ((self.dc2[m1]["MAG"]*3//2)*x - (self.dc2[m2]["DEF"])//2)//2
        if self.dmg1 < 2:
            self.dmg2 = random.randint(0,1)
        elif 2 <= self.dmg1 < 9:
            self.dmg2 = random.randint(self.dmg1-2,self.dmg1)
        elif 9 <= self.dmg1:
            self.dmg2 = (self.dmg1*7)//8 + ((self.dmg1//4 + 1)*(random.randint(0,255)))//256
        return self.dmg2

    def aselect(self, m1):
        self.ac = self.alive_monsters.copy()
        self.ac.remove(m1)
        return self.ac

    def cri(self, m1):
        self.dmg = self.dc2[m1]["ATK"]*(random.randint(55,65))//64
        if self.dmg > 254:
            self.dmg = 254
        return self.dmg

    #m1 > m2 dod low  m1 < m2 dod high
    def dod(self, m1, m2, x):
        self.m1s = self.dc2[m1]["SPD"]
        self.m2s = self.dc2[m2]["SPD"]
        if self.m1s > self.m2s:
            self.dodge = -(self.m1s-self.m2s)/(random.randint(1, 3)) + (random.randint(10, 20))/(random.randint(1, 10)) - 3*x
        elif self.m1s < self.m2s:
            self.dodge = -(self.m1s-self.m2s)/(random.randint(1, 3)) - (random.randint(10, 20))/(random.randint(1, 10)) - 3*x
        else:
            self.dodge = 1/(random.randint(1, 3)) - (random.randint(10, 20))/(random.randint(1, 10)) - 3*x
        return self.dodge > 0

    def mhpli(self):
        self.result = "全体のHP..."
        for self.mn in self.li2:
            self.hp = self.dc2[self.mn]["HP"]
            self.keys = list(self.dc2[self.mn]['CON'].keys())
            self.result += f"{self.mn} {self.hp} {self.keys}, "   
        return self.result.rstrip(", ")

    def mhplik(self):
        self.result = "全体のHP..."
        for self.mn in self.li3:
            self.hp = self.dc2[self.mn]["HP"]
            self.keys = list(self.dc2[self.mn]['CON'].keys())
            self.result += f"{self.mn} {self.hp} {self.keys}, "   
        return self.result.rstrip(", ")


    def start(self, po, ps_mons):
        self.pm = ps_mons
        self.winner = None
        while self.mc < 4:
            (self.mons1, self.mons2) = self.select(self.alive_monsters)
            self.af = random.randint(0, 1)
            if self.af == 0:
                self.m1 = self.mons1; self.m2 = self.mons2
            else:
                self.m1 = self.mons2; self.m2 = self.mons1
            self.j_player_name_li = list(self.dc2[self.m1]['CON'].keys())        
            if "ねむり" in self.j_player_name_li:
                print(f"{self.m1}→{self.m2}")
                print(f"{self.m1}はねむっている！")
            else:
                # if self.pm == self.m1 or self.m1 == "キングスライム":
                if self.pm == "No":
                    print(f"{self.m1}→{self.m2}")
                    self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]; self.m1mp = self.dc2[self.m1]["MP"]
                    print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}!  　　"); print(self.mhpli())
                    # if self.pm == "ベホマスライム":
                    #     self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or キアリー or ベホマ or まじんぎり) 残りMP{self.m1mp}")
                    # elif self.pm == "スライムLv8":
                    #     if self.sc == 8:
                    #         self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or 合体 or まじんぎり ) 残りMP{self.m1mp}")
                    #     else:
                    #         self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or なかまをよぶ or まじんぎり　) 残りMP{self.m1mp}")
                    # elif self.pm == "キングスライム":
                    #     self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or ラリホーマ or どくの息 or まじんぎり) 残りMP{self.m1mp}")
                    # elif self.pm == "ドラゴスライム":
                    #     self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or ラリホーマ or かえんの息 or どくの息 or まじんぎり) 残りMP{self.m1mp}")
                    # elif self.pm == "スライムベス":
                    #     self.pa = input(f"入力(こうげき or ホイミ or バイキルト or ルカナン or  どくの息 or ラリホーマ or イオナズン or まじんぎり) 残りMP{self.m1mp}")
                    # else:
                    #     self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or まじんぎり) 残りMP{self.m1mp}")

                    if self.pa == "こうげき":
                        self.dod1 = self.dod(self.m1, self.m2, 1)
                        print(f"{self.m1}のこうげき！")
                        if self.dod1 == True:
                            print("回避成功")
                            self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                            print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}!  　　")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())
                        else:
                            self.crip = random.randint(1, 32)
                            if self.crip == 1:
                                self.dmg = self.cri(self.m1)
                                self.dc2[self.m2]["HP"] -= self.dmg
                                print(f"{self.dmg}damage かいしんのいちげき！")
                                self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                if self.dc2[self.m2]["HP"] <= 0:
                                    print(f"{self.m2}のHPは0になってしまった... out")
                                    self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                    if "キングスライム" in self.alive_monsters:
                                        print(self.mhplik())
                                    else:
                                        print(self.mhpli())
                                    self.alive_monsters.remove(self.m2)
                                    self.mc += 1
                                    if self.mc == 4:
                                        self.winner = self.m1
                                        break
                                else:
                                    self.af = random.randint(0, 1)
                            else:
                                self.dmg = self.d(self.m1, self.m2)
                                self.dc2[self.m2]["HP"] -= self.dmg
                                print(f"{self.dmg}damage")
                                self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                if self.dc2[self.m2]["HP"] <= 0:
                                    print(f"{self.m2}のHPは0になってしまった... out")
                                    self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                    if "キングスライム" in self.alive_monsters:
                                        print(self.mhplik())
                                    else:
                                        print(self.mhpli())                            
                                    self.alive_monsters.remove(self.m2)
                                    self.mc += 1
                                    if self.mc == 4:
                                        self.winner = self.m1
                                        break
                                else:
                                    self.af = random.randint(0, 1)
                    elif self.pa == "ホイミ":
                        print(f"{self.m1}はホイミをつかった！")
                        if self.m1mp >= 4:
                            self.dc2[self.m1]["HP"] += 10
                            if self.dc2[self.m1]["HP"] > self.primitive_dc[self.m1]["HP"]:
                                while self.dc2[self.m1]["HP"] > self.primitive_dc[self.m1]["HP"]:
                                    self.dc2[self.m1]["HP"] -= 1
                                    if self.dc2[self.m1]["HP"] == self.primitive_dc[self.m1]["HP"]:
                                        break
                            self.dc2[self.m1]["MP"] -= 4
                            print(f"{self.m1}はHPを10回復した")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())                    
                        else:
                            print("MPがたりない！")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())
                    elif self.pa == "どくの息":
                        print(f"{self.m1}はどくの息をつかった！")
                        if self.m1mp >= 4:
                            self.dc2[self.m1]["MP"] -= 4
                            self.liaa = self.aselect(self.m1)
                            self.ac = 0
                            while self.ac < len(self.liaa):
                                self.dod1 = self.dod(self.m1, self.liaa[self.ac], 1/3)
                                if self.dod1 == True:
                                    print(f"{self.liaa[self.ac]}はどくの息をかわした！  ")
                                    self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                    print(f"{self.m2s}の残りHP{self.m2hp}!  ")
                                    self.ac += 1
                                    if "キングスライム" in self.alive_monsters:
                                        print(self.mhplik())
                                    else:
                                        print(self.mhpli())
                                else:
                                    self.jli = list(self.dc2[self.liaa[self.ac]]['CON'].keys())
                                    if len(self.jli) == 1:
                                        if self.jli[0] == "どく" or self.jli[0] == "げんき":
                                            self.dc2[self.liaa[self.ac]]["CON"] = {"どく": 1}
                                        else:
                                            self.dc2[self.liaa[self.ac]]["CON"]["どく"] = 1
                                    elif len(self.jli) == 2:
                                        self.dc2[self.liaa[self.ac]]["CON"]["どく"] = 1
                                    print(f"{self.liaa[self.ac]}はどくになってしまった  ")
                                    self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                    print(f"{self.m2s}の残りHP{self.m2hp}")
                                    self.ac += 1
                        else:
                            print("MPがたりない！")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())
                    elif self.pa == "ラリホーマ":
                        print(f"{self.m1}はラリホーマをつかった！")
                        if self.m1mp >= 4:
                            self.dc2[self.m1]["MP"] -= 4
                            self.liaa = self.aselect(self.m1)
                            self.ac = 0
                            while self.ac < len(self.liaa):
                                self.dod1 = self.dod(self.m1, self.liaa[self.ac], 1)
                                if self.dod1 == True:
                                    print(f"{self.liaa[self.ac]}はラリホーマをかわした！  ")
                                    self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                    print(f"{self.m2s}の残りHP{self.m2hp}!  ")
                                    self.ac += 1
                                    if "キングスライム" in self.alive_monsters:
                                        print(self.mhplik())
                                    else:
                                        print(self.mhpli())
                                else:
                                    self.jli = list(self.dc2[self.liaa[self.ac]]['CON'].keys())
                                    if len(self.jli) == 1:
                                        if self.jli[0] == "ねむり" or self.jli[0] == "げんき":
                                            self.dc2[self.liaa[self.ac]]["CON"] = {"ねむり": 1}
                                        else:
                                            self.dc2[self.liaa[self.ac]]["CON"]["ねむり"] = 1
                                    elif len(self.jli) == 2:
                                        self.dc2[self.liaa[self.ac]]["CON"]["ねむり"] = 1
                                    print(f"{self.liaa[self.ac]}はねむってしまった  ", end = "")
                                    self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                    print(f"{self.m2s}の残りHP{self.m2hp}")
                                    self.ac += 1
                        else:
                            print("MPがたりない！")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())
                    elif self.pa == "バイキルト":
                        print(f"{self.m1}はバイキルトをつかった！")
                        if self.m1mp >= 4:
                            self.dc2[self.m1]["MP"] -= 4
                            print(f"{self.m1}の攻撃力は2倍になった！")
                            if self.dc2[self.m1]["BfDbf"]["bk"] == 0:
                                self.dc2[self.m1]["ATK"] *= 2
                            self.dc2[self.m1]["BfDbf"]["bk"] = 1
                        else:
                            print("MPがたりない！")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())
                    elif self.pa == "ルカナン":
                        print(f"{self.m1}はルカナンをつかった！")
                        if self.m1mp >= 4:
                            self.dc2[self.m1]["MP"] -= 4
                            lcli = self.aselect(self.m1)
                            self.lcc = 0
                            while self.lcc < len(lcli):
                                defd = self.primitive_dc[lcli[self.lcc]]["DEF"]*2//10
                                print(f"{lcli[self.lcc]}の守備力が減少した！")
                                if self.dc2[lcli[self.lcc]]["BfDbf"]["rk"] == 0:
                                    self.dc2[lcli[self.lcc]]["DEF"] -= defd
                                    self.dc2[lcli[self.lcc]]["BfDbf"]["rk"] = 1
                                elif (not(self.dc2[lcli[self.lcc]]["BfDbf"]["rk"] == 0)) and (not(self.dc2[lcli[self.lcc]]["DEF"] == self.primitive_dc[lcli[self.lcc]]["DEF"]-2*defd)):
                                    self.dc2[lcli[self.lcc]]["DEF"] -= defd
                                    self.dc2[lcli[self.lcc]]["BfDbf"]["rk"] = 1
                                else:
                                    self.dc2[lcli[self.lcc]]["BfDbf"]["rk"] = 1
                                self.lcc += 1

                        else:
                            print("MPがたりない！")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())              
                    elif (not(self.pm == "スライムベス")) and (self.pa == "メラ"):
                        print(f"{self.m1}はメラをつかった！")
                        self.crip = random.randint(1, 32)
                        if self.m1mp >= 4:
                            self.dc2[self.m1]["MP"] -= 4
                            self.dod1 = self.dod(self.m1, self.m2, 3/2)
                            if self.dod1 == True:
                                print("回避成功")
                                self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}!  　　")
                                if "キングスライム" in self.alive_monsters:
                                    print(self.mhplik())
                                else:
                                    print(self.mhpli())
                            else:
                                if self.crip == 1:
                                    self.dmg = self.cri(self.m1)*3//2
                                    self.dc2[self.m2]["HP"] -= self.dmg
                                    print(f"{self.dmg}damage かいしんのいちげき！")
                                    self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                    print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                    if self.dc2[self.m2]["HP"] <= 0:
                                        print(f"{self.m2}のHPは0になってしまった... out")
                                        self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in self.alive_monsters:
                                            print(self.mhplik())
                                        else:
                                            print(self.mhpli())                        
                                        self.alive_monsters.remove(self.m2)
                                        self.mc += 1
                                        if self.mc == 4:
                                            self.winner = self.m1
                                            break
                                    else:
                                        self.af = random.randint(0, 1)
                                else:                     
                                    self.dmg = self.md(self.m1, self.m2, 1)
                                    self.dc2[self.m2]["HP"] -= self.dmg
                                    print(f"{self.dmg}damage")
                                    self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                    print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                    if self.dc2[self.m2]["HP"] <= 0:
                                        print(f"{self.m2}のHPは0になってしまった... out")
                                        self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in self.alive_monsters:
                                            print(self.mhplik())
                                        else:
                                            print(self.mhpli())
                                        self.alive_monsters.remove(self.m2)
                                        self.mc += 1
                                        if self.mc == 4:
                                            self.winner = self.m1
                                            break
                                    else:
                                        self.af = random.randint(0, 1)
                        else:
                            print("MPがたりない！")
                        if "キングスライム" in self.alive_monsters:
                            print(self.mhplik())
                        else:
                            print(self.mhpli())
                    elif (self.pa == "ベホマ") and (self.pm == "ベホマスライム"):
                        print(f"{self.m1}はベホマをつかった！")
                        if self.m1mp >= 4 :
                            while self.dc2[self.m1]["HP"] < self.primitive_dc[self.m1]["HP"]:
                                self.dc2[self.m1]["HP"] += 1
                                if self.dc2[self.m1]["HP"] == self.primitive_dc[self.m1]["HP"]:
                                    break
                            self.dc2[self.m1]["MP"] -= 6
                            print(f"{self.m1}はHPを全回復した")
                        else:
                            print("MPがたりない！")
                        if "キングスライム" in self.alive_monsters:
                            print(self.mhplik())
                        else:
                            print(self.mhpli())
                    elif (self.pa == "キアリー") and (self.pm == "ベホマスライム"):
                        print(f"{self.m1}はキアリーをつかった！")
                        if self.m1mp >= 4 :
                            self.dc2[self.m1]["CON"] = {"げんき": 1}
                            self.dc2[self.m1]["MP"] -= 4
                            print(f"{self.m1}は状態異常を全回復した")
                        else:
                            print("MPがたりない！")
                        if "キングスライム" in self.alive_monsters:
                            print(self.mhplik())
                        else:
                            print(self.mhpli())
                    elif (self.pm == "スライムLv8") and (not(self.sc == 8)) and (self.pa == "なかまをよぶ"):
                        self.sc += 1 #確率で失敗
                        print(f"スライムLv8はなかまをよんだ スライムLv8の数{self.sc}")
                        # self.dc2[f"スライムLv8({self.sc})"] = {li[i] for i in range(len(li)-1)}; self.dc2[f"スライムLv8{self.sc}"]["Lv"] = divmod((self.dc2[f"スライムLv8{self.sc}"]["HP"] + self.dc2[f"スライムLv8{self.sc}"]["MP"] + self.dc2[f"スライムLv8{self.sc}"]["ATK"] + self.dc2[f"スライムLv8{self.sc}"]["DEF"] + self.dc2[f"スライムLv8{self.sc}"]["SPD"] + self.dc2[f"スライムLv8{self.sc}"]["MAG"]), 10)[0]
                    elif (self.pm == "スライムLv8") and (self.sc == 8) and (self.pa == "合体"):
                        print("スライムLv8たちが合体していく！")
                        print("キングスライムがあらわれた！")
                        self.primitive_dc["キングスライム"] = {self.li[i]: random.randint(100, 150) for i in range(len(self.li)-1)}
                        self.primitive_dc["キングスライム"]["Lv"] = divmod((self.primitive_dc["キングスライム"]["HP"] + self.primitive_dc["キングスライム"]["MP"] + self.primitive_dc[f"キングスライム"]["ATK"] + self.primitive_dc[f"キングスライム"]["DEF"] + self.primitive_dc[f"キングスライム"]["SPD"] + self.primitive_dc["キングスライム"]["MAG"]), 10)[0]
                        self.dc2["キングスライム"] = copy.deepcopy(self.primitive_dc["キングスライム"])
                        self.alive_monsters.remove("スライムLv8")
                        self.alive_monsters.append("キングスライム")
                        print(self.mhplik())
                    elif (self.pm == "ドラゴスライム") and (self.pa == "かえんの息"):
                        print(f"{self.m1}はかえんの息をつかった！")
                        self.liaa = self.aselect(self.m1)
                        self.ac = 0
                        while self.ac < len(self.liaa):
                            self.dod1 = self.dod(self.m1, self.liaa[self.ac], 2)
                            if self.dod1 == True:
                                print(f"{self.liaa[self.ac]}はかえんの息をかわした！  ")
                                self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                print(f"{self.m2s}の残りHP{self.m2hp}!  ")
                                self.ac += 1
                                if "キングスライム" in self.alive_monsters:
                                    print(self.mhplik())
                                else:
                                    print(self.mhpli())
                            else:
                                self.crip = random.randint(1, 32)
                                if self.crip == 1:
                                    self.dmg = self.cri(self.m1)*3//2
                                    self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                    print(f"{self.liaa[self.ac]}に{self.dmg}damage かいしんのいちげき！  ")
                                    self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                    print(f"{self.m2s}の残りHP{self.m2hp}")
                                    self.ac += 1
                                    if self.dc2[self.m2s]["HP"] <= 0:
                                        print(f"{self.m2s}のHPは0になってしまった... out")
                                        self.dc2[self.m2s]["HP"] = 0; self.dc2[self.m2s]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in self.alive_monsters:
                                            print(self.mhplik())
                                        else:
                                            print(self.mhpli())
                                        self.alive_monsters.remove(self.m2s)
                                        self.mc += 1
                                        if self.mc == 4:
                                            self.winner = self.m1
                                            break
                                    else:
                                        self.af = random.randint(0, 1)
                                else:
                                    self.dmg = self.md(self.m1, self.liaa[self.ac], 1)
                                    self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                    print(f"{self.liaa[self.ac]}に{self.dmg}damage  ")
                                    self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                    print(f"{self.m2s}の残りHP{self.m2hp}")
                                    self.ac += 1
                                    if self.dc2[self.m2s]["HP"] <= 0:
                                        print(f"{self.m2s}のHPは0になってしまった... out")
                                        self.dc2[self.m2s]["HP"] = 0; self.dc2[self.m2s]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in self.alive_monsters:
                                            print(self.mhplik())
                                        else:
                                            print(self.mhpli())
                                        self.alive_monsters.remove(self.m2s)
                                        self.mc += 1
                                        if self.mc == 4:
                                            self.winner = self.m1
                                            break
                                    else:
                                        self.af = random.randint(0, 1)
                    elif (self.pm == "スライムベス") and (self.pa == "イオナズン"):
                        print(f"{self.m1}はイオナズンをつかった！")
                        if self.m1mp >= 25:
                            self.dc2[self.m1]["MP"] -= 25
                            self.liaa = self.aselect(self.m1)
                            self.ac = 0
                            while self.ac < len(self.liaa):
                                self.dod1 = self.dod(self.m1, self.liaa[self.ac], 3)
                                if self.dod1 == True:
                                    print(f"{self.liaa[self.ac]}はイオナズンをかわした！  ")
                                    self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                    print(f"{self.m2s}の残りHP{self.m2hp}!  ")
                                    self.ac += 1
                                    if "キングスライム" in self.alive_monsters:
                                        print(self.mhplik())
                                    else:
                                        print(self.mhpli())
                                else:
                                    self.crip = random.randint(1, 32)
                                    if self.crip == 1:
                                        self.dmg = self.cri(self.m1)*3//2
                                        self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                        print(f"{self.liaa[self.ac]}に{self.dmg}damage かいしんのいちげき！  ")
                                        self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                        print(f"{self.m2s}の残りHP{self.m2hp}")
                                        self.ac += 1
                                        if self.dc2[self.m2s]["HP"] <= 0:
                                            print(f"{self.m2s}のHPは0になってしまった... out")
                                            self.dc2[self.m2s]["HP"] = 0; self.dc2[self.m2s]["CON"] = {"ひんし": 1}
                                            if "キングスライム" in self.alive_monsters:
                                                print(self.mhplik())
                                            else:
                                                print(self.mhpli())
                                            self.alive_monsters.remove(self.m2s)
                                            self.mc += 1
                                            if self.mc == 4:
                                                self.winner = self.m1
                                                break
                                        else:
                                            self.af = random.randint(0, 1)
                                    else:
                                        self.dmg = self.md(self.m1, self.liaa[self.ac], 3)
                                        self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                        print(f"{self.liaa[self.ac]}に{self.dmg}damage  ")
                                        self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                        print(f"{self.m2s}の残りHP{self.m2hp}")
                                        self.ac += 1
                                        if self.dc2[self.m2s]["HP"] <= 0:
                                            print(f"{self.m2s}のHPは0になってしまった... out")
                                            self.dc2[self.m2s]["HP"] = 0; self.dc2[self.m2s]["CON"] = {"ひんし": 1}
                                            if "キングスライム" in self.alive_monsters:
                                                print(self.mhplik())
                                            else:
                                                print(self.mhpli())
                                            self.alive_monsters.remove(self.m2s)
                                            self.mc += 1
                                            if self.mc == 4:
                                                self.winner = self.m1
                                                break
                                        else:
                                            self.af = random.randint(0, 1)
                        else:
                            print("MPがたりない！")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())
                    elif self.pa == "まじんぎり":
                        print(f"{self.m1}はまじんぎりをつかった！")
                        self.dod1 = self.dod(self.m1, self.m2, 1)
                        if self.dod1 == True:
                            print("回避成功")
                            self.af = random.randint(0, 1)
                            self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                            print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}!  　　")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())                    
                        else:
                            self.mpro = random.randint(0, 1)
                            if self.mpro == 0:
                                print("ミス")
                            else:
                                self.crip = random.randint(1, 32)
                                if self.crip == 1:
                                    self.dmg = self.cri(self.m1)*2
                                    self.dc2[self.m2]["HP"] -= self.dmg
                                    print(f"{self.dmg}damage かいしんのいちげき！")
                                    self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                    print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                    if self.dc2[self.m2]["HP"] <= 0:
                                        print(f"{self.m2}のHPは0になってしまった... out")
                                        self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in self.alive_monsters:
                                            print(self.mhplik())
                                        else:
                                            print(self.mhpli())
                                        self.alive_monsters.remove(self.m2)
                                        self.mc += 1
                                        if self.mc == 4:
                                            self.winner = self.m1
                                            break
                                    else:
                                        self.af = random.randint(0, 1)
                                else:                     
                                    self.dmg = self.d(self.m1, self.m2)*2
                                    self.dc2[self.m2]["HP"] -= self.dmg
                                    print(f"{self.dmg}damage")
                                    self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                    print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                    if self.dc2[self.m2]["HP"] <= 0:
                                        print(f"{self.m2}のHPは0になってしまった... out")
                                        self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in self.alive_monsters:
                                            print(self.mhplik())
                                        else:
                                            print(self.mhpli())                                
                                        self.alive_monsters.remove(self.m2)
                                        self.mc += 1
                                        if self.mc == 4:
                                            self.winner = self.m1
                                            break
                                    else:
                                        self.af = random.randint(0, 1)         
                    else:
                        print("有効なコマンドを入力してください")
                        if self.pm == "ベホマスライム":
                            self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or キアリー or ベホマ or まじんぎり) 残りMP{self.m1mp}")
                        elif self.pm == "スライムLv8":
                            if self.sc == 8:
                                self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or 合体 or まじんぎり ) 残りMP{self.m1mp}")
                            else:
                                self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or なかまをよぶ or まじんぎり　) 残りMP{self.m1mp}")
                        elif self.pm == "キングスライム":
                            self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or ラリホーマ or どくの息 or まじんぎり) 残りMP{self.m1mp}")
                        elif self.pm == "ドラゴスライム":
                            self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or ラリホーマ or かえんの息 or どくの息 or まじんぎり) 残りMP{self.m1mp}")
                        elif self.pm == "スライムベス":
                            self.pa = input(f"入力(こうげき or ホイミ or バイキルト or ルカナン or  どくの息 or ラリホーマ or イオナズン or まじんぎり) 残りMP{self.m1mp}")
                        else:
                            self.pa = input(f"入力(こうげき or ホイミ or メラ or バイキルト or ルカナン or どくの息 or ラリホーマ or まじんぎり) 残りMP{self.m1mp}")     

                else:
                    self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]; self.m1mp = self.dc2[self.m1]["MP"]
                    print(f"{self.m1}→{self.m2}")
                    # self.pa = input("Attack!")
                    self.pa = "yes"
                    if not(self.pa == "no"):
                        if self.m1 == "ベホマスライム":
                            na = random.randint(0, 9)
                        elif self.m1 == "スライムLv8" or  self.m1 == "ドラゴスライム":
                            na = random.randint(0, 8)
                        else:
                            na = random.randint(0, 7)
                        if na == 0:
                            print(f"{self.m1}のこうげき！")
                            self.dod1 = self.dod(self.m1, self.m2, 1)
                            if self.dod1 == True:
                                print("回避成功")
                                self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}!  　　")
                                if "キングスライム" in self.alive_monsters:
                                    print(self.mhplik())
                                else:
                                    print(self.mhpli())
                            else:
                                self.crip = random.randint(1, 32)
                                if self.crip == 1:
                                    self.dmg = self.cri(self.m1)
                                    self.dc2[self.m2]["HP"] -= self.dmg
                                    print(f"{self.dmg}damage かいしんのいちげき！")
                                    self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                    print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                    if self.dc2[self.m2]["HP"] <= 0:
                                        print(f"{self.m2}のHPは0になってしまった... out")
                                        self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in self.alive_monsters:
                                            print(self.mhplik())
                                        else:
                                            print(self.mhpli())
                                        self.alive_monsters.remove(self.m2)
                                        self.mc += 1
                                        if self.mc == 4:
                                            self.winner = self.m1
                                            break
                                    else:
                                        self.af = random.randint(0, 1)
                                else:
                                    self.dmg = self.d(self.m1, self.m2)
                                    self.dc2[self.m2]["HP"] -= self.dmg
                                    print(f"{self.dmg}damage")
                                    self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                    print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                    if self.dc2[self.m2]["HP"] <= 0:
                                        print(f"{self.m2}のHPは0になってしまった... out")
                                        self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                        if "キングスライム" in self.alive_monsters:
                                            print(self.mhplik())
                                        else:
                                            print(self.mhpli())                            
                                        self.alive_monsters.remove(self.m2)
                                        self.mc += 1
                                        if self.mc == 4:
                                            self.winner = self.m1
                                            break
                                    else:
                                        self.af = random.randint(0, 1)
                        elif na == 1:
                            print(f"{self.m1}はホイミをつかった！")
                            if self.m1mp >= 10 :
                                self.dc2[self.m1]["HP"] += 10
                                if self.dc2[self.m1]["HP"] > self.primitive_dc[self.m1]["HP"]:
                                    while self.dc2[self.m1]["HP"] > self.primitive_dc[self.m1]["HP"]:
                                        self.dc2[self.m1]["HP"] -= 1
                                        if self.dc2[self.m1]["HP"] == self.primitive_dc[self.m1]["HP"]:
                                            break
                                self.dc2[self.m1]["MP"] -= 10
                                print(f"{self.m1}はHPを10回復した")
                                if "キングスライム" in self.alive_monsters:
                                    print(self.mhplik())
                                else:
                                    print(self.mhpli())                    
                            else:
                                print("MPがたりない！")
                                if "キングスライム" in self.alive_monsters:
                                    print(self.mhplik())
                                else:
                                    print(self.mhpli())
                        elif na == 2:
                            print(f"{self.m1}はどくの息をつかった！")
                            if self.m1mp >= 4:
                                self.dc2[self.m1]["MP"] -= 4
                                self.liaa = self.aselect(self.m1)
                                self.ac = 0
                                while self.ac < len(self.liaa):
                                    self.dod1 = self.dod(self.m1, self.liaa[self.ac], 1/3)
                                    if self.dod1 == True:
                                        print(f"{self.liaa[self.ac]}はどくの息をかわした！  ")
                                        self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                        print(f"{self.m2s}の残りHP{self.m2hp}!  ")
                                        self.ac += 1
                                        if "キングスライム" in self.alive_monsters:
                                            print(self.mhplik())
                                        else:
                                            print(self.mhpli())
                                    else:
                                        self.jli = list(self.dc2[self.liaa[self.ac]]['CON'].keys())
                                        if len(self.jli) == 1:
                                            if self.jli[0] == "どく" or self.jli[0] == "げんき":
                                                self.dc2[self.liaa[self.ac]]["CON"] = {"どく": 1}
                                            else:
                                                self.dc2[self.liaa[self.ac]]["CON"]["どく"] = 1
                                        elif len(self.jli) == 2:
                                            self.dc2[self.liaa[self.ac]]["CON"]["どく"] = 1
                                        print(f"{self.liaa[self.ac]}はどくになってしまった  ")
                                        self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                        print(f"{self.m2s}の残りHP{self.m2hp}")
                                        self.ac += 1
                            else:
                                print("MPがたりない！")
                                if "キングスライム" in self.alive_monsters:
                                    print(self.mhplik())
                                else:
                                    print(self.mhpli())
                        elif na == 3:
                            print(f"{self.m1}はラリホーマをつかった！")
                            if self.m1mp >= 4:
                                self.dc2[self.m1]["MP"] -= 4
                                self.liaa = self.aselect(self.m1)
                                self.ac = 0
                                while self.ac < len(self.liaa):
                                    self.dod1 = self.dod(self.m1, self.liaa[self.ac], 1)
                                    if self.dod1 == True:
                                        print(f"{self.liaa[self.ac]}はラリホーマをかわした！  ")
                                        self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                        print(f"{self.m2s}の残りHP{self.m2hp}!  ")
                                        self.ac += 1
                                        if "キングスライム" in self.alive_monsters:
                                            print(self.mhplik())
                                        else:
                                            print(self.mhpli())
                                    else:
                                        self.jli = list(self.dc2[self.liaa[self.ac]]['CON'].keys())
                                        if len(self.jli) == 1:
                                            if self.jli[0] == "ねむり" or self.jli[0] == "げんき":
                                                self.dc2[self.liaa[self.ac]]["CON"] = {"ねむり": 1}
                                            else:
                                                self.dc2[self.liaa[self.ac]]["CON"]["ねむり"] = 1
                                        elif len(self.jli) == 2:
                                            self.dc2[self.liaa[self.ac]]["CON"]["ねむり"] = 1
                                        print(f"{self.liaa[self.ac]}はねむってしまった  ", end = "")
                                        self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                        print(f"{self.m2s}の残りHP{self.m2hp}")
                                        self.ac += 1
                            else:
                                print("MPがたりない！")
                                if "キングスライム" in self.alive_monsters:
                                    print(self.mhplik())
                                else:
                                    print(self.mhpli())
                        elif na == 4:
                            print(f"{self.m1}はバイキルトをつかった！")
                            if self.m1mp >= 4:
                                self.dc2[self.m1]["MP"] -= 4
                                print(f"{self.m1}の攻撃力は2倍になった！")
                                if self.dc2[self.m1]["BfDbf"]["bk"] == 0:
                                    self.dc2[self.m1]["ATK"] *= 2
                                self.dc2[self.m1]["BfDbf"]["bk"] = 1
                            else:
                                print("MPがたりない！")
                                if "キングスライム" in self.alive_monsters:
                                    print(self.mhplik())
                                else:
                                    print(self.mhpli())
                        elif na == 5:
                            print(f"{self.m1}はルカナンをつかった！")
                            if self.m1mp >= 4:
                                self.dc2[self.m1]["MP"] -= 4
                                lcli = self.aselect(self.m1)
                                self.lcc = 0
                                while self.lcc < len(lcli):
                                    defd = self.primitive_dc[lcli[self.lcc]]["DEF"]*2//10
                                    print(f"{lcli[self.lcc]}の守備力が減少した！")
                                    if self.dc2[lcli[self.lcc]]["BfDbf"]["rk"] == 0:
                                        self.dc2[lcli[self.lcc]]["DEF"] -= defd
                                        self.dc2[lcli[self.lcc]]["BfDbf"]["rk"] = 1
                                    elif (not(self.dc2[lcli[self.lcc]]["BfDbf"]["rk"] == 0)) and (not(self.dc2[lcli[self.lcc]]["DEF"] == self.primitive_dc[lcli[self.lcc]]["DEF"]-2*defd)):
                                        self.dc2[lcli[self.lcc]]["DEF"] -= defd
                                        self.dc2[lcli[self.lcc]]["BfDbf"]["rk"] = 1
                                    else:
                                        self.dc2[lcli[self.lcc]]["BfDbf"]["rk"] = 1
                                    self.lcc += 1

                            else:
                                print("MPがたりない！")
                                if "キングスライム" in self.alive_monsters:
                                    print(self.mhplik())
                                else:
                                    print(self.mhpli())              
                        elif (not(self.m1 == "スライムベス")) and (na == 6):
                            print(f"{self.m1}はメラをつかった！")
                            self.crip = random.randint(1, 32)
                            if self.m1mp >= 4:
                                self.dc2[self.m1]["MP"] -= 4
                                self.dod1 = self.dod(self.m1, self.m2, 3/2)
                                if self.dod1 == True:
                                    print("回避成功")
                                    self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                    print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}!  　　")
                                    if "キングスライム" in self.alive_monsters:
                                        print(self.mhplik())
                                    else:
                                        print(self.mhpli())
                                else:
                                    if self.crip == 1:
                                        self.dmg = self.cri(self.m1)*3//2
                                        self.dc2[self.m2]["HP"] -= self.dmg
                                        print(f"{self.dmg}damage かいしんのいちげき！")
                                        self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                        print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                        if self.dc2[self.m2]["HP"] <= 0:
                                            print(f"{self.m2}のHPは0になってしまった... out")
                                            self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                            if "キングスライム" in self.alive_monsters:
                                                print(self.mhplik())
                                            else:
                                                print(self.mhpli())                        
                                            self.alive_monsters.remove(self.m2)
                                            self.mc += 1
                                            if self.mc == 4:
                                                self.winner = self.m1
                                                break
                                        else:
                                            self.af = random.randint(0, 1)
                                    else:                     
                                        self.dmg = self.md(self.m1, self.m2, 1)
                                        self.dc2[self.m2]["HP"] -= self.dmg
                                        print(f"{self.dmg}damage")
                                        self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                        print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                        if self.dc2[self.m2]["HP"] <= 0:
                                            print(f"{self.m2}のHPは0になってしまった... out")
                                            self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                            if "キングスライム" in self.alive_monsters:
                                                print(self.mhplik())
                                            else:
                                                print(self.mhpli())
                                            self.alive_monsters.remove(self.m2)
                                            self.mc += 1
                                            if self.mc == 4:
                                                self.winner = self.m1
                                                break
                                        else:
                                            self.af = random.randint(0, 1)
                            else:
                                print("MPがたりない！")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())
                        elif (na == 9) and (self.m1 == "ベホマスライム"):
                            print(f"{self.m1}はベホマをつかった！")
                            if self.m1mp >= 6 :
                                while self.dc2[self.m1]["HP"] < self.primitive_dc[self.m1]["HP"]:
                                    self.dc2[self.m1]["HP"] += 1
                                    if self.dc2[self.m1]["HP"] == self.primitive_dc[self.m1]["HP"]:
                                        break
                                self.dc2[self.m1]["MP"] -= 6
                                print(f"{self.m1}はHPを全回復した")
                            else:
                                print("MPがたりない！")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())
                        elif (na == 8) and (self.m1 == "ベホマスライム"):
                            print(f"{self.m1}はキアリーをつかった！")
                            if self.m1mp >= 4 :
                                self.dc2[self.m1]["CON"] = {"げんき": 1}
                                self.dc2[self.m1]["MP"] -= 4
                                print(f"{self.m1}は状態異常を全回復した")
                            else:
                                print("MPがたりない！")
                            if "キングスライム" in self.alive_monsters:
                                print(self.mhplik())
                            else:
                                print(self.mhpli())
                        elif (self.m1 == "スライムLv8") and (not(self.sc == 8)) and (na == 8):
                            self.sc += 1 #確率で失敗
                            print(f"スライムLv8はなかまをよんだ スライムLv8の数{self.sc}")
                            # self.dc2[f"スライムLv8({self.sc})"] = {li[i] for i in range(len(li)-1)}; self.dc2[f"スライムLv8{self.sc}"]["Lv"] = divmod((self.dc2[f"スライムLv8{self.sc}"]["HP"] + self.dc2[f"スライムLv8{self.sc}"]["MP"] + self.dc2[f"スライムLv8{self.sc}"]["ATK"] + self.dc2[f"スライムLv8{self.sc}"]["DEF"] + self.dc2[f"スライムLv8{self.sc}"]["SPD"] + self.dc2[f"スライムLv8{self.sc}"]["MAG"]), 10)[0]
                        elif (self.m1 == "スライムLv8") and (self.sc == 8) and (na == 8):
                            print("スライムLv8たちが合体していく！")
                            print("キングスライムがあらわれた！")
                            self.primitive_dc["キングスライム"] = {self.li[i]: random.randint(100, 150) for i in range(len(self.li)-1)}
                            self.primitive_dc["キングスライム"]["Lv"] = divmod((self.primitive_dc["キングスライム"]["HP"] + self.primitive_dc["キングスライム"]["MP"] + self.primitive_dc[f"キングスライム"]["ATK"] + self.primitive_dc[f"キングスライム"]["DEF"] + self.primitive_dc[f"キングスライム"]["SPD"] + self.primitive_dc["キングスライム"]["MAG"]), 10)[0]
                            self.dc2["キングスライム"] = copy.deepcopy(self.primitive_dc["キングスライム"])
                            self.alive_monsters.remove("スライムLv8")
                            self.alive_monsters.append("キングスライム")
                            print(self.mhplik())
                        elif (self.m1 == "ドラゴスライム") and (na == 8):
                            print(f"{self.m1}はかえんの息をつかった！")
                            self.liaa = self.aselect(self.m1)
                            self.ac = 0
                            while self.ac < len(self.liaa):
                                self.dod1 = self.dod(self.m1, self.liaa[self.ac], 2)
                                if self.dod1 == True:
                                    print(f"{self.liaa[self.ac]}はかえんの息をかわした！  ")
                                    self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                    print(f"{self.m2s}の残りHP{self.m2hp}!  ")
                                    self.ac += 1
                                    if "キングスライム" in self.alive_monsters:
                                        print(self.mhplik())
                                    else:
                                        print(self.mhpli())
                                else:
                                    self.crip = random.randint(1, 32)
                                    if self.crip == 1:
                                        self.dmg = self.cri(self.m1)*3//2
                                        self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                        print(f"{self.liaa[self.ac]}に{self.dmg}damage かいしんのいちげき！  ")
                                        self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                        print(f"{self.m2s}の残りHP{self.m2hp}")
                                        self.ac += 1
                                        if self.dc2[self.m2s]["HP"] <= 0:
                                            print(f"{self.m2s}のHPは0になってしまった... out")
                                            self.dc2[self.m2s]["HP"] = 0; self.dc2[self.m2s]["CON"] = {"ひんし": 1}
                                            if "キングスライム" in self.alive_monsters:
                                                print(self.mhplik())
                                            else:
                                                print(self.mhpli())
                                            self.alive_monsters.remove(self.m2s)
                                            self.mc += 1
                                            if self.mc == 4:
                                                self.winner = self.m1
                                                break
                                        else:
                                            self.af = random.randint(0, 1)
                                    else:
                                        self.dmg = self.md(self.m1, self.liaa[self.ac], 1)
                                        self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                        print(f"{self.liaa[self.ac]}に{self.dmg}damage  ")
                                        self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                        print(f"{self.m2s}の残りHP{self.m2hp}")
                                        self.ac += 1
                                        if self.dc2[self.m2s]["HP"] <= 0:
                                            print(f"{self.m2s}のHPは0になってしまった... out")
                                            self.dc2[self.m2s]["HP"] = 0; self.dc2[self.m2s]["CON"] = {"ひんし": 1}
                                            if "キングスライム" in self.alive_monsters:
                                                print(self.mhplik())
                                            else:
                                                print(self.mhpli())
                                            self.alive_monsters.remove(self.m2s)
                                            self.mc += 1
                                            if self.mc == 4:
                                                self.winner = self.m1
                                                break
                                        else:
                                            self.af = random.randint(0, 1)
                        elif (self.m1 == "スライムベス") and (na == 6):
                            print(f"{self.m1}はイオナズンをつかった！")
                            if self.m1mp >= 25:
                                self.dc2[self.m1]["MP"] -= 25
                                self.liaa = self.aselect(self.m1)
                                self.ac = 0
                                while self.ac < len(self.liaa):
                                    self.dod1 = self.dod(self.m1, self.liaa[self.ac], 3)
                                    if self.dod1 == True:
                                        print(f"{self.liaa[self.ac]}はイオナズンをかわした！  ")
                                        self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                        print(f"{self.m2s}の残りHP{self.m2hp}!  ")
                                        self.ac += 1
                                        if "キングスライム" in self.alive_monsters:
                                            print(self.mhplik())
                                        else:
                                            print(self.mhpli())
                                    else:
                                        self.crip = random.randint(1, 32)
                                        if self.crip == 1:
                                            self.dmg = self.cri(self.m1)*3//2
                                            self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                            print(f"{self.liaa[self.ac]}に{self.dmg}damage かいしんのいちげき！  ")
                                            self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                            print(f"{self.m2s}の残りHP{self.m2hp}")
                                            self.ac += 1
                                            if self.dc2[self.m2s]["HP"] <= 0:
                                                print(f"{self.m2s}のHPは0になってしまった... out")
                                                self.dc2[self.m2s]["HP"] = 0; self.dc2[self.m2s]["CON"] = {"ひんし": 1}
                                                if "キングスライム" in self.alive_monsters:
                                                    print(self.mhplik())
                                                else:
                                                    print(self.mhpli())
                                                self.alive_monsters.remove(self.m2s)
                                                self.mc += 1
                                                if self.mc == 4:
                                                    self.winner = self.m1
                                                    break
                                            else:
                                                self.af = random.randint(0, 1)
                                        else:
                                            self.dmg = self.md(self.m1, self.liaa[self.ac], 3)
                                            self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                            print(f"{self.liaa[self.ac]}に{self.dmg}damage  ")
                                            self.m1hp = self.dc2[self.m1]["HP"]; self.m2s = self.liaa[self.ac]; self.m2hp = self.dc2[self.liaa[self.ac]]["HP"]
                                            print(f"{self.m2s}の残りHP{self.m2hp}")
                                            self.ac += 1
                                            if self.dc2[self.m2s]["HP"] <= 0:
                                                print(f"{self.m2s}のHPは0になってしまった... out")
                                                self.dc2[self.m2s]["HP"] = 0; self.dc2[self.m2s]["CON"] = {"ひんし": 1}
                                                if "キングスライム" in self.alive_monsters:
                                                    print(self.mhplik())
                                                else:
                                                    print(self.mhpli())
                                                self.alive_monsters.remove(self.m2s)
                                                self.mc += 1
                                                if self.mc == 4:
                                                    self.winner = self.m1
                                                    break
                                            else:
                                                self.af = random.randint(0, 1)
                            else:
                                print("MPがたりない！")
                                if "キングスライム" in self.alive_monsters:
                                    print(self.mhplik())
                                else:
                                    print(self.mhpli())
                        elif na == 7:
                            print(f"{self.m1}はまじんぎりをつかった！")
                            self.dod1 = self.dod(self.m1, self.m2, 1)
                            if self.dod1 == True:
                                print("回避成功")
                                self.af = random.randint(0, 1)
                                self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}!  　　")
                                if "キングスライム" in self.alive_monsters:
                                    print(self.mhplik())
                                else:
                                    print(self.mhpli())                    
                            else:
                                self.mpro = random.randint(0, 1)
                                if self.mpro == 0:
                                    print("ミス")
                                else:
                                    self.crip = random.randint(1, 32)
                                    if self.crip == 1:
                                        self.dmg = self.cri(self.m1)*2
                                        self.dc2[self.m2]["HP"] -= self.dmg
                                        print(f"{self.dmg}damage かいしんのいちげき！")
                                        self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                        print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                        if self.dc2[self.m2]["HP"] <= 0:
                                            print(f"{self.m2}のHPは0になってしまった... out")
                                            self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                            if "キングスライム" in self.alive_monsters:
                                                print(self.mhplik())
                                            else:
                                                print(self.mhpli())
                                            self.alive_monsters.remove(self.m2)
                                            self.mc += 1
                                            if self.mc == 4:
                                                self.winner = self.m1
                                                break
                                        else:
                                            self.af = random.randint(0, 1)
                                    else:                     
                                        self.dmg = self.d(self.m1, self.m2)*2
                                        self.dc2[self.m2]["HP"] -= self.dmg
                                        print(f"{self.dmg}damage")
                                        self.m1hp = self.dc2[self.mons1]["HP"]; self.m2hp = self.dc2[self.mons2]["HP"]
                                        print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                                        if self.dc2[self.m2]["HP"] <= 0:
                                            print(f"{self.m2}のHPは0になってしまった... out")
                                            self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}
                                            if "キングスライム" in self.alive_monsters:
                                                print(self.mhplik())
                                            else:
                                                print(self.mhpli())                                
                                            self.alive_monsters.remove(self.m2)
                                            self.mc += 1
                                            if self.mc == 4:
                                                self.winner = self.m1
                                                break
                                        else:
                                            self.af = random.randint(0, 1)         

            if "キングスライム" in self.alive_monsters:
                self.dk = 0
                while self.dk < 5:
                    self.jli = list(self.dc2[self.li3[self.dk]]['CON'].keys())
                    if len(self.jli) > 0:
                        if len(self.jli) > 1:
                            if self.jli[0] == "どく" or self.jli[1] == "どく":
                                self.dc2[self.li3[self.dk]]["HP"] -= self.primitive_dc[self.li3[self.dk]]["HP"]//10
                                self.dm = self.li3[self.dk]; self.dd = self.primitive_dc[self.li3[self.dk]]["HP"]//10
                                print(f"{self.dm}はどくで{self.dd}ダメージをうけた")
                                if self.dc2[self.dm]["HP"] <= 0:
                                    print(f"{self.dm}のHPは0になってしまった... out")
                                    self.dc2[self.dm]["HP"] = 0; self.dc2[self.dm]["CON"] = {"ひんし": 1}
                                    print(self.mhplik())
                                    self.alive_monsters.remove(self.dm)
                                    self.mc += 1
                                    if self.mc == 4:
                                        self.winner = self.alive_monsters[0]
                                        break
                                if (not(self.dc2[self.dm]["CON"] == {"ひんし": 1})):
                                    self.p = self.dc2[self.dm]["CON"]["どく"]
                                    self.kp = random.randint(1, 10)
                                    if self.kp <= self.p:
                                        print(f"{self.dm}はどくからかいふくした")
                                        del self.dc2[self.dm]["CON"]["どく"]
                                    else:
                                        if self.dc2[self.dm]["CON"]["どく"] < 5:
                                            self.dc2[self.dm]["CON"]["どく"] += 1
                                self.dk += 1
                            if self.jli[0] == "ねむり" or self.jli[1] == "ねむり":
                                self.dm = self.li3[self.dk]
                                self.sl = self.dc2[self.dm]["CON"]["ねむり"]
                                self.ksl = random.randint(1, 10)
                                if self.ksl <= self.sl:
                                    print(f"{self.dm}はねむりからかいふくした")
                                    del self.dc2[self.dm]["CON"]["ねむり"]
                                else:
                                    if self.dc2[self.dm]["CON"]["ねむり"] < 5:
                                        self.dc2[self.dm]["CON"]["ねむり"] += 1
                            else:
                                self.dk += 1
                            
                        else:
                            if self.jli[0] == "どく":
                                self.dc2[self.li3[self.dk]]["HP"] -= self.primitive_dc[self.li3[self.dk]]["HP"]//10
                                self.dm = self.li3[self.dk]; self.dd = self.primitive_dc[self.li3[self.dk]]["HP"]//10
                                print(f"{self.dm}はどくで{self.dd}ダメージをうけた")
                                if self.dc2[self.dm]["HP"] <= 0:
                                    print(f"{self.dm}のHPは0になってしまった... out")
                                    self.dc2[self.dm]["HP"] = 0; self.dc2[self.dm]["CON"] = {"ひんし": 1}
                                    print(self.mhplik())
                                    self.alive_monsters.remove(self.dm)
                                    self.mc += 1
                                    if self.mc == 4:
                                        self.winner = self.alive_monsters[0]
                                        break
                                if (not(self.dc2[self.dm]["CON"] == {"ひんし": 1})):
                                    self.p = self.dc2[self.dm]["CON"]["どく"]
                                    self.kp = random.randint(1, 10)
                                    if self.kp <= self.p:
                                        print(f"{self.dm}はどくからかいふくした")
                                        self.dc2[self.dm]["CON"] = {"げんき": 1}
                                    else:
                                        if self.dc2[self.dm]["CON"]["どく"] < 5:
                                            self.dc2[self.dm]["CON"]["どく"] += 1
                                self.dk += 1
                            elif self.jli[0] == "ねむり":
                                self.dm = self.li3[self.dk]
                                self.sl = self.dc2[self.dm]["CON"]["ねむり"]
                                self.ksl = random.randint(1, 10)
                                if self.ksl <= self.sl:
                                    print(f"{self.dm}はねむりからかいふくした")
                                    self.dc2[self.dm]["CON"] = {"げんき": 1}
                                else:
                                    if self.dc2[self.dm]["CON"]["ねむり"] < 5:
                                        self.dc2[self.dm]["CON"]["ねむり"] += 1
                            else:
                                self.dk += 1
            else:
                self.dk = 0
                while self.dk < 5:
                    self.jli = list(self.dc2[self.li2[self.dk]]['CON'].keys())
                    if len(self.jli) > 0:
                        if len(self.jli) > 1:
                            if self.jli[0] == "どく" or self.jli[1] == "どく":
                                self.dc2[self.li2[self.dk]]["HP"] -= self.primitive_dc[self.li2[self.dk]]["HP"]//10
                                self.dm = self.li2[self.dk]; self.dd = self.primitive_dc[self.li2[self.dk]]["HP"]//10
                                print(f"{self.dm}はどくで{self.dd}ダメージをうけた")
                                if self.dc2[self.dm]["HP"] <= 0:
                                    print(f"{self.dm}のHPは0になってしまった... out")
                                    self.dc2[self.dm]["HP"] = 0; self.dc2[self.dm]["CON"] = {"ひんし": 1}
                                    print(self.mhpli())
                                    self.alive_monsters.remove(self.dm)
                                    self.mc += 1
                                    if self.mc == 4:
                                        self.winner = self.alive_monsters[0]
                                        break
                                if (not(self.dc2[self.dm]["CON"] == {"ひんし": 1})):
                                    self.p = self.dc2[self.dm]["CON"]["どく"]
                                    self.kp = random.randint(1, 10)
                                    if self.kp <= self.p:
                                        print(f"{self.dm}はどくからかいふくした")
                                        del self.dc2[self.dm]["CON"]["どく"]
                                    else:
                                        if self.dc2[self.dm]["CON"]["どく"] < 5:
                                            self.dc2[self.dm]["CON"]["どく"] += 1
                                self.dk += 1
                            elif self.jli[0] == "ねむり" or self.jli[1] == "ねむり":
                                self.dm = self.li2[self.dk]
                                self.sl = self.dc2[self.dm]["CON"]["ねむり"]
                                self.ksl = random.randint(1, 10)
                                if self.ksl <= self.sl:
                                    print(f"{self.dm}はねむりからかいふくした")
                                    del self.dc2[self.dm]["CON"]["ねむり"]
                                else:
                                    if self.dc2[self.dm]["CON"]["ねむり"] < 5:
                                        self.dc2[self.dm]["CON"]["ねむり"] += 1
                                self.dk += 1
                            else:
                                self.dk += 1
                        else:
                            if self.jli[0] == "どく":
                                self.dc2[self.li2[self.dk]]["HP"] -= self.primitive_dc[self.li2[self.dk]]["HP"]//10
                                self.dm = self.li2[self.dk]; self.dd = self.primitive_dc[self.li2[self.dk]]["HP"]//10
                                print(f"{self.dm}はどくで{self.dd}ダメージをうけた")
                                if self.dc2[self.dm]["HP"] <= 0:
                                    print(f"{self.dm}のHPは0になってしまった... out")
                                    self.dc2[self.dm]["HP"] = 0; self.dc2[self.dm]["CON"] = {"ひんし": 1}
                                    print(self.mhpli())
                                    self.alive_monsters.remove(self.dm)
                                    self.mc += 1
                                    if self.mc == 4:
                                        self.winner = self.alive_monsters[0]
                                        break
                                if (not(self.dc2[self.dm]["CON"] == {"ひんし": 1})):
                                    self.p = self.dc2[self.dm]["CON"]["どく"]
                                    self.kp = random.randint(1, 10)
                                    if self.kp <= self.p:
                                        print(f"{self.dm}はどくからかいふくした")
                                        self.dc2[self.dm]["CON"] = {"げんき": 1}
                                    else:
                                        if self.dc2[self.dm]["CON"]["どく"] < 5:
                                            self.dc2[self.dm]["CON"]["どく"] += 1
                                self.dk += 1
                            elif self.jli[0] == "ねむり":
                                self.dm = self.li2[self.dk]
                                self.sl = self.dc2[self.dm]["CON"]["ねむり"]
                                self.ksl = random.randint(1, 10)
                                if self.ksl <= self.sl:
                                    print(f"{self.dm}はねむりからかいふくした")
                                    self.dc2[self.dm]["CON"] = {"げんき": 1}
                                else:
                                    if self.dc2[self.dm]["CON"]["ねむり"] < 5:
                                        self.dc2[self.dm]["CON"]["ねむり"] += 1
                                self.dk += 1
                            else:
                                self.dk += 1
            bd = 0
            while bd < len(self.alive_monsters):
                if (self.dc2[self.alive_monsters[bd]]["BfDbf"]["bk"] > 0) and (self.m1 == self.alive_monsters[bd]):
                    self.dc2[self.alive_monsters[bd]]["BfDbf"]["bk"] += 1
                    if self.dc2[self.alive_monsters[bd]]["BfDbf"]["bk"] == 4:
                        self.dc2[self.alive_monsters[bd]]["BfDbf"]["bk"] == 0
                        self.dc2[self.m1]["ATK"]//2
                if self.dc2[self.alive_monsters[bd]]["BfDbf"]["rk"] > 0:
                    self.dc2[self.alive_monsters[bd]]["BfDbf"]["rk"] += 1
                    if self.dc2[self.alive_monsters[bd]]["BfDbf"]["rk"] == 4:
                        self.dc2[self.alive_monsters[bd]]["BfDbf"]["rk"] == 0
                        drc = self.dc2[self.alive_monsters[bd]]["DEF"]
                        while drc < self.primitive_dc[self.alive_monsters[bd]]["DEF"]:
                            drc += 1
                bd += 1

        if (not(self.winner == None)) and (self.winner in self.dc2):
            # self.wm = po*lvdc5[self.dc2[self.winner]["Lv"]]
            self.wm = 0
            print(f"バトロワの勝者は {self.winner}")
            if self.pm == self.winner:
                print(f"あなたの勝ち  {self.wm}円 got")
            else:
                if (self.pm == "スライムLv8") and (self.winner == "キングスライム"):
                    print(f"あなたの勝ち  {self.wm}円 got")
                else:
                    print(f"あなたの負けです  {po}円 lost")
        else:
            print("error")

        return self.winner
