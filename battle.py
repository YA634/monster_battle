import random
import copy
import cre_mons

class Mons_battle():
    li = ["HP", "MP", "ATK", "DEF", "SPD", "MAG", "Lv", "CON"]
    li2 = ["スライムLv8", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
    li3 = ["キングスライム", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
    li4 = ["勇者","賢者","パラディン","バトルマスター","スーパースター"]

    def __init__(self, m_sta_dc):
        self.primitive_dc = m_sta_dc
        self.dc2 = copy.deepcopy(self.primitive_dc)
        self.dddc = {}
        self.odds_li = cre_mons.create_odds(self.dc2)
        self.mc = 0
        self.sc = 1
        self.btl_turn = 0
        self.alive_monsters = ["スライムLv8", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]


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

    def m_s(self):
        (self.mons1, self.mons2) = self.select(self.alive_monsters)
        self.af = random.randint(0, 1)
        if self.af == 0:
            self.m1 = self.mons1; self.m2 = self.mons2
        else:
            self.m1 = self.mons2; self.m2 = self.mons1
        return [self.m1, self.m2]

    def cmd_li(self, mn):
        if mn == "ベホマスライム":
            self.pa = ['こうげき','ホイミ','メラ','バイキルト','ルカナン','どくの息','ラリホーマ','キアリー','ベホマ','まじんぎり']
        elif mn == "スライムLv8":
            if self.sc == 8:
                self.pa = ['こうげき','ホイミ','メラ','バイキルト','ルカナン','どくの息','ラリホーマ','合体','まじんぎり']
            else:
                self.pa = ['こうげき','ホイミ','メラ','バイキルト','ルカナン','どくの息','ラリホーマ','なかまをよぶ','まじんぎり']
        elif mn == "キングスライム":
            self.pa = ['こうげき','ホイミ','メラ','バイキルト','ルカナン','どくの息','ラリホーマ','まじんぎり']
        elif mn == "ドラゴスライム":
            self.pa = ['こうげき','ホイミ','メラ','バイキルト','ルカナン','どくの息','かえんの息','ラリホーマ','まじんぎり']
        elif mn == "スライムベス":
            self.pa = ['こうげき','ホイミ','バイキルト','ルカナン','どくの息','ラリホーマ','イオナズン','まじんぎり']
        else:
            self.pa = ['こうげき','ホイミ','メラ','バイキルト','ルカナン','どくの息','ラリホーマ','まじんぎり']
        return self.pa


    def start(self, b_m_li, cmd, p_mons):
        self.winner = None
        self.btl_turn += 1
        # (self.mons1, self.mons2) = self.select(self.alive_monsters)
        # self.af = random.randint(0, 1)
        # if self.af == 0:
        #     self.m1 = self.mons1; self.m2 = self.mons2
        # else:
        #     self.m1 = self.mons2; self.m2 = self.mons1
        self.cmd = cmd
        self.p_m = p_mons
        self.m1 = b_m_li[0]; self.m2 = b_m_li[1]
        self.m1hp = self.dc2[self.m1]["HP"]; self.m2hp = self.dc2[self.m2]["HP"]
        self.m1mp = self.dc2[self.m1]["MP"]; self.m2mp = self.dc2[self.m2]["MP"]
        self.crip = 0
        self.dod1 = None
        self.mp_con = 0
        self.liaa = self.aselect(self.m1)
        self.message = ""
        self.show_dmg = ""
        self.show_j = ""
        self.jdmg_m = ""
        self.j_rep = ""
        self.bk_m = ""
        self.rk_m = ""
        self.sleep_m = 0
        
        jm1li = list(self.dc2[self.m1]['CON'].keys())       
        if "ねむり" in jm1li:
            #print(f"{m1}→{m2}")
            self.sleep_m += 1
            self.result = f"{self.m1}はねむっている!"
        else:
            if self.cmd == 'こうげき':
                self.dod1 = self.dod(self.m1, self.m2, 1)
                if self.dod1 == True:
                    self.dmg = 0
                    pass

                else:
                    self.crip = random.randint(1, 32)
                    if self.crip == 1:
                        self.dmg = self.cri(self.m1)
                        self.dc2[self.m2]["HP"] -= self.dmg
                        #print(f"{self.dmg}damage かいしんのいちげき！")
                    else:
                        self.dmg = self.d(self.m1, self.m2)
                        self.dc2[self.m2]["HP"] -= self.dmg
                        #print(f"{self.dmg}damage")
                    #print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                    if self.dc2[self.m2]["HP"] <= 0:
                        self.message += f"{self.m2}のHPは0になってしまった... out"
                        self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}                                                
                        self.alive_monsters.remove(self.m2)
                        self.mc += 1
                        if self.mc == 4:
                            self.winner = self.m1
                self.result = f"{self.m1}は{self.m2}に攻撃した  {self.dmg}ダメージ"

            elif self.cmd == 'まじんぎり':
                self.dod1 = self.dod(self.m1, self.m2, 1)
                if self.dod1 == True:
                    self.dmg = 0
                    pass

                else:
                    self.mpro = random.randint(0, 1)
                    if self.mpro == 0:
                        self.dmg = 0
                        #print("ミス")
                    else:
                        self.crip = random.randint(1, 32)
                        if self.crip == 1:
                            self.dmg = self.cri(self.m1)*2
                            self.dc2[self.m2]["HP"] -= self.dmg
                            #print(f"{self.dmg}damage かいしんのいちげき！")
                        else:
                            self.dmg = self.d(self.m1, self.m2)*2
                            self.dc2[self.m2]["HP"] -= self.dmg
                            #print(f"{self.dmg}damage")
                        #print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                        if self.dc2[self.m2]["HP"] <= 0:
                            self.message += f"{self.m2}のHPは0になってしまった... out"
                            self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}                                                    
                            self.alive_monsters.remove(self.m2)
                            self.mc += 1
                            if self.mc == 4:
                                self.winner = self.m1
                        else:
                            self.af = random.randint(0, 1)
                self.result = f"{self.m1}は{self.m2}にまじんぎりをはなった  {self.dmg}ダメージ"

            elif self.cmd == 'ホイミ':
                #print(f"{self.m1}はホイミをつかった！")
                if self.m1mp >= 4:
                    self.dc2[self.m1]["HP"] += 10
                    if self.dc2[self.m1]["HP"] > self.primitive_dc[self.m1]["HP"]:
                        while self.dc2[self.m1]["HP"] > self.primitive_dc[self.m1]["HP"]:
                            self.dc2[self.m1]["HP"] -= 1
                            if self.dc2[self.m1]["HP"] == self.primitive_dc[self.m1]["HP"]:
                                break
                    self.dc2[self.m1]["MP"] -= 4
                    #print(f"{self.m1}はHPを10回復した")
                else:
                    self.mp_con = -1
                self.result = f"{self.m1}はホイミをつかった！  HPを10回復した"
            
            elif self.cmd == 'ベホマ':
                #print(f"{self.m1}はホイミをつかった！")
                if self.m1mp >= 6:
                    self.dc2[self.m1]["HP"] += 50
                    if self.dc2[self.m1]["HP"] > self.primitive_dc[self.m1]["HP"]:
                        while self.dc2[self.m1]["HP"] > self.primitive_dc[self.m1]["HP"]:
                            self.dc2[self.m1]["HP"] -= 1
                            if self.dc2[self.m1]["HP"] == self.primitive_dc[self.m1]["HP"]:
                                break
                    self.dc2[self.m1]["MP"] -= 6
                    #print(f"{self.m1}はHPを10回復した")
                else:
                    self.mp_con = -1
                self.result = f"{self.m1}はベホマをつかった！  HPを全回復した"
            
            elif self.cmd == 'キアリー':
                #print(f"{self.m1}はホイミをつかった！")
                if self.m1mp >= 4:
                    self.dc2[self.m1]["CON"] = {"げんき": 1}
                    self.dc2[self.m1]["MP"] -= 4
                else:
                    self.mp_con = -1
                self.result = f"{self.m1}は状態異常を全回復した"

            elif self.cmd == 'バイキルト':
                #print(f"{m1}はバイキルトをつかった！")
                if self.m1mp >= 4:
                    self.dc2[self.m1]["MP"] -= 4
                    #print(f"{self.m1}の攻撃力は2倍になった！")
                    if self.dc2[self.m1]["BfDbf"]["bk"] == 0:
                        self.dc2[self.m1]["ATK"] *= 2
                    self.dc2[self.m1]["BfDbf"]["bk"] = 1
                else:
                    #print("MPがたりない！")
                    self.mp_con = -1
                self.result = f"{self.m1}はバイキルトをつかった！ こうげきりょくが2ばいになった!"

            elif self.cmd == 'ルカナン':
                #print(f"{m1}はルカナンをつかった！")
                if self.m1mp >= 4:
                    self.dc2[self.m1]["MP"] -= 4
                    self.lcli = self.aselect(self.m1)
                    self.lcc = 0
                    while self.lcc < len(self.lcli):
                        self.defd = self.primitive_dc[self.lcli[self.lcc]]["DEF"]*2//10
                        if self.dc2[self.lcli[self.lcc]]["BfDbf"]["rk"] == 0:
                            self.dc2[self.lcli[self.lcc]]["DEF"] -= self.defd
                            self.dc2[self.lcli[self.lcc]]["BfDbf"]["rk"] = 1
                            self.show_j += f"{self.lcli[self.lcc]}の守備力が減少した！ "
                        elif (not(self.dc2[self.lcli[self.lcc]]["BfDbf"]["rk"] == 0)) and (not(self.dc2[self.lcli[self.lcc]]["DEF"] == self.primitive_dc[self.lcli[self.lcc]]["DEF"]-2*self.defd)):
                            self.dc2[self.lcli[self.lcc]]["DEF"] -= self.defd
                            self.dc2[self.lcli[self.lcc]]["BfDbf"]["rk"] = 1
                            self.show_j += f"{self.lcli[self.lcc]}の守備力がさらに減少した！ "
                        else:
                            self.dc2[self.lcli[self.lcc]]["BfDbf"]["rk"] = 1
                            self.show_j += f"{self.lcli[self.lcc]}の守備力はこれ以上減少しない！ "
                        self.lcc += 1
                else:
                    #print("MPがたりない！")
                    self.mp_con = -1
                self.result = f"{self.m1}はルカナンをつかった！ {self.show_j}"

            elif self.cmd == 'なかまをよぶ':
                #print(f"{self.m1}はホイミをつかった！")
                self.sc += 1 #確率で失敗
                self.result = f"スライムLv8はなかまをよんだ スライムLv8の数{self.sc}"

            elif self.cmd == '合体':
                #print("スライムLv8たちが合体していく！")
                #print("キングスライムがあらわれた！")
                self.primitive_dc["キングスライム"] = {self.li[i]: random.randint(100, 150) for i in range(len(self.li)-1)}
                self.primitive_dc["キングスライム"]["Lv"] = divmod((self.primitive_dc["キングスライム"]["HP"] + self.primitive_dc["キングスライム"]["MP"] + self.primitive_dc[f"キングスライム"]["ATK"] + self.primitive_dc[f"キングスライム"]["DEF"] + self.primitive_dc[f"キングスライム"]["SPD"] + self.primitive_dc["キングスライム"]["MAG"]), 10)[0]
                self.dc2["キングスライム"] = copy.deepcopy(self.primitive_dc["キングスライム"])
                self.alive_monsters.remove("スライムLv8")
                self.alive_monsters.append("キングスライム")
                self.result = f"スライムLv8たちが合体していく！<br>キングスライムがあらわれた！"

            elif self.cmd == 'メラ':
                #print(f"{m1}はメラをつかった！")
                self.crip = random.randint(1, 32)
                if self.m1mp >= 4:
                    self.dc2[self.m1]["MP"] -= 4
                    self.dod1 = self.dod(self.m1, self.m2, 3/2)
                    if self.dod1 == True:
                        #print("回避成功")
                        #print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　")
                        self.dmg = 0
                        pass

                    else:
                        if self.crip == 1:
                            self.dmg = self.cri(self.m1)*3//2
                            self.dc2[self.m2]["HP"] -= self.dmg
                            #print(f"{dmg}damage かいしんのいちげき！")
                            #print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                        else:                     
                            self.dmg = self.md(self.m1, self.m2, 1)
                            self.dc2[self.m2]["HP"] -= self.dmg
                            #print(f"{dmg}damage")
                            #print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                        if self.dc2[self.m2]["HP"] <= 0:
                            self.message += f"{self.m2}のHPは0になってしまった... out"
                            self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}                      
                            self.alive_monsters.remove(self.m2)
                            self.mc += 1
                            if self.mc == 4:
                                self.winner = self.m1
                else:
                    #print("MPがたりない！")
                    self.dmg = 0
                    self.mp_con = -1
                self.result = f"{self.m1}は{self.m2}にメラをはなった  {self.dmg}ダメージ"

            elif self.cmd == 'かえんの息':
                #print(f"{m1}はかえんの息をつかった！")
                if self.m1mp >= 8:
                    self.dc2[self.m1]["MP"] -= 8
                    self.liaa = self.aselect(self.m1)
                    self.ac = 0
                    while self.ac < len(self.liaa):
                        self.dod1 = self.dod(self.m1, self.liaa[self.ac], 2)
                        if self.dod1 == True:
                            #print(f"{liaa[ac]}はイオナズンをかわした！  ")
                            #print(f"{m2s}の残りHP{m2hp}!  ")
                            self.show_dmg += f"{self.liaa[self.ac]}に0ダメージ "
                        else:
                            self.crip = random.randint(1, 32)
                            if self.crip == 1:
                                self.dmg = self.cri(self.m1)*3//2
                                self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                            else:
                                self.dmg = self.md(self.m1, self.liaa[self.ac], 1)
                                self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                            self.show_dmg += f"{self.liaa[self.ac]}に{self.dmg}ダメージ "
                            if self.dc2[self.liaa[self.ac]]["HP"] <= 0:
                                self.message += f"{self.liaa[self.ac]}のHPは0になってしまった... out"
                                self.dc2[self.liaa[self.ac]]["HP"] = 0; self.dc2[self.liaa[self.ac]]["CON"] = {"ひんし": 1}
                                self.alive_monsters.remove(self.liaa[self.ac])
                                self.mc += 1
                                if self.mc == 4:
                                    self.winner = self.m1
                        self.ac += 1
                else:
                    #print("MPがたりない！")
                    self.mp_con = -1

                self.result = f"{self.m1}はかえんの息をつかった！  {self.show_dmg}"

            elif self.cmd == 'イオナズン':
                #print(f"{m1}はイオナズンをつかった！")
                if self.m1mp >= 25:
                    self.dc2[self.m1]["MP"] -= 25
                    self.liaa = self.aselect(self.m1)
                    self.ac = 0
                    while self.ac < len(self.liaa):
                        self.dod1 = self.dod(self.m1, self.liaa[self.ac], 3)
                        if self.dod1 == True:
                            #print(f"{liaa[ac]}はイオナズンをかわした！  ")
                            #print(f"{m2s}の残りHP{m2hp}!  ")
                            self.show_dmg += f"{self.liaa[self.ac]}に0ダメージ "
                        else:
                            self.crip = random.randint(1, 32)
                            if self.crip == 1:
                                self.dmg = self.cri(self.m1)*3//2
                                self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                            else:
                                self.dmg = self.md(self.m1, self.liaa[self.ac], 4)
                                self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                            self.show_dmg += f"{self.liaa[self.ac]}に{self.dmg}ダメージ "
                            if self.dc2[self.liaa[self.ac]]["HP"] <= 0:
                                self.message += f"{self.liaa[self.ac]}のHPは0になってしまった... out"
                                self.dc2[self.liaa[self.ac]]["HP"] = 0; self.dc2[self.liaa[self.ac]]["CON"] = {"ひんし": 1}
                                self.alive_monsters.remove(self.liaa[self.ac])
                                self.mc += 1
                                if self.mc == 4:
                                    self.winner = self.m1
                        self.ac += 1
                else:
                    #print("MPがたりない！")
                    self.mp_con = -1
                self.result = f"{self.m1}はイオナズンをつかった！  {self.show_dmg}"



            elif self.cmd == 'どくの息':
                #print(f"{m1}はどくの息をつかった！")
                if self.m1mp >= 4:
                    self.dc2[self.m1]["MP"] -= 4
                    self.liaa = self.aselect(self.m1)
                    self.ac = 0
                    while self.ac < len(self.liaa):
                        self.dod1 = self.dod(self.m1, self.liaa[self.ac], 1/3)
                        if self.dod1 == True:
                            self.show_j += f"{self.liaa[self.ac]}はどくの息をかわした！ "       
                        else:
                            self.jli = list(self.dc2[self.liaa[self.ac]]['CON'].keys())
                            if len(self.jli) == 1:
                                if self.jli[0] == "どく" or self.jli[0] == "げんき":
                                    self.dc2[self.liaa[self.ac]]["CON"] = {"どく": 1}
                                else:
                                    self.dc2[self.liaa[self.ac]]["CON"]["どく"] = 1
                            elif len(self.jli) == 2:
                                self.dc2[self.liaa[self.ac]]["CON"]["どく"] = 1
                            self.show_j += f"{self.liaa[self.ac]}はどくにおかされた！ "
                        self.ac += 1
                else:
                    #print("MPがたりない！")
                    self.mp_con = -1
                self.result = f"{self.m1}はどくの息をつかった！  {self.show_j}"
                

            elif self.cmd == 'ラリホーマ':
                #print(f"{m1}はラリホーマをつかった！")
                if self.m1mp >= 4:
                    self.dc2[self.m1]["MP"] -= 4
                    self.ac = 0
                    while self.ac < len(self.liaa):
                        self.dod1 = self.dod(self.m1, self.liaa[self.ac], 1)
                        if self.dod1 == True:
                            self.show_j += f"{self.liaa[self.ac]}はラリホーマをかわした！ "
                        else:
                            self.jli = list(self.dc2[self.liaa[self.ac]]['CON'].keys())
                            if len(self.jli) == 1:
                                if self.jli[0] == "ねむり" or self.jli[0] == "げんき":
                                    self.dc2[self.liaa[self.ac]]["CON"] = {"ねむり": 1}
                                else:
                                    self.dc2[self.liaa[self.ac]]["CON"]["ねむり"] = 1
                            elif len(self.jli) == 2:
                                self.dc2[self.liaa[self.ac]]["CON"]["ねむり"] = 1
                            self.show_j += f"{self.liaa[self.ac]}はねむってしまった！ "
                        self.ac += 1
                else:
                    #print("MPがたりない！")
                    self.mp_con = -1
                self.result = f"{self.m1}はラリホーマをつかった！  {self.show_j}"

        if "キングスライム" in self.alive_monsters:
            self.u_li = self.li3
        else:
            self.u_li = self.li2
        self.dk = 0
        while self.dk < 5:
            self.jli = list(self.dc2[self.u_li[self.dk]]['CON'].keys())
            if len(self.jli) > 0:
                if len(self.jli) > 1:
                    if self.jli[0] == "どく" or self.jli[1] == "どく":
                        self.dc2[self.u_li[self.dk]]["HP"] -= self.primitive_dc[self.u_li[self.dk]]["HP"]//10
                        self.dm = self.u_li[self.dk]; self.dd = self.primitive_dc[self.u_li[self.dk]]["HP"]//10
                        self.jdmg_m += f"{self.dm}はどくで{self.dd}ダメージをうけた "
                        if self.dc2[self.dm]["HP"] <= 0:
                            self.message += f"{self.dm}のHPは0になってしまった... out "
                            self.dc2[self.dm]["HP"] = 0; self.dc2[self.dm]["CON"] = {"ひんし": 1}
                            self.alive_monsters.remove(self.dm)
                            self.mc += 1
                            if self.mc == 4:
                                self.winner = self.alive_monsters[0]
                                break
                        if (not(self.dc2[self.dm]["CON"] == {"ひんし": 1})):
                            self.p = self.dc2[self.dm]["CON"]["どく"]
                            self.kp = random.randint(1, 10)
                            if self.kp <= self.p:
                                self.j_rep += f"{self.dm}はどくからかいふくした "
                                del self.dc2[self.dm]["CON"]["どく"]
                            else:
                                if self.dc2[self.dm]["CON"]["どく"] < 5:
                                    self.dc2[self.dm]["CON"]["どく"] += 1
                        self.dk += 1
                    elif self.jli[0] == "ねむり" or self.jli[1] == "ねむり":
                        self.dm = self.u_li[self.dk]
                        self.sl = self.dc2[self.dm]["CON"]["ねむり"]
                        self.ksl = random.randint(1, 10)
                        if self.ksl <= self.sl:
                            self.j_rep += f"{self.dm}はねむりからかいふくした "
                            del self.dc2[self.dm]["CON"]["ねむり"]
                        else:
                            if self.dc2[self.dm]["CON"]["ねむり"] < 5:
                                self.dc2[self.dm]["CON"]["ねむり"] += 1
                        self.dk += 1
                    else:
                        self.dk += 1
                else:
                    if self.jli[0] == "どく":
                        self.dc2[self.u_li[self.dk]]["HP"] -= self.primitive_dc[self.u_li[self.dk]]["HP"]//10
                        self.dm = self.u_li[self.dk]; self.dd = self.primitive_dc[self.u_li[self.dk]]["HP"]//10
                        self.jdmg_m += f"{self.dm}はどくで{self.dd}ダメージをうけた "
                        if self.dc2[self.dm]["HP"] <= 0:
                            self.message += f"{self.dm}のHPは0になってしまった... out "
                            self.dc2[self.dm]["HP"] = 0; self.dc2[self.dm]["CON"] = {"ひんし": 1}
                            self.alive_monsters.remove(self.dm)
                            self.mc += 1
                            if self.mc == 4:
                                self.winner = self.alive_monsters[0]
                                break
                        if (not(self.dc2[self.dm]["CON"] == {"ひんし": 1})):
                            self.p = self.dc2[self.dm]["CON"]["どく"]
                            self.kp = random.randint(1, 10)
                            if self.kp <= self.p:
                                self.j_rep += f"{self.dm}はどくから回復した "
                                self.dc2[self.dm]["CON"] = {"げんき": 1}
                            else:
                                if self.dc2[self.dm]["CON"]["どく"] < 5:
                                    self.dc2[self.dm]["CON"]["どく"] += 1
                        self.dk += 1
                    elif self.jli[0] == "ねむり":
                        self.dm = self.u_li[self.dk]
                        self.sl = self.dc2[self.dm]["CON"]["ねむり"]
                        self.ksl = random.randint(1, 10)
                        if self.ksl <= self.sl:
                            self.j_rep += f"{self.dm}はねむりから回復した "
                            self.dc2[self.dm]["CON"] = {"げんき": 1}
                        else:
                            if self.dc2[self.dm]["CON"]["ねむり"] < 5:
                                self.dc2[self.dm]["CON"]["ねむり"] += 1
                        self.dk += 1
                    else:
                        self.dk += 1
        self.bd = 0
        while self.bd < len(self.alive_monsters):
            if (self.dc2[self.alive_monsters[self.bd]]["BfDbf"]["bk"] > 0) and (self.m1 == self.alive_monsters[self.bd]):
                self.dc2[self.alive_monsters[self.bd]]["BfDbf"]["bk"] += 1
                if self.dc2[self.alive_monsters[self.bd]]["BfDbf"]["bk"] == 4:
                    self.dc2[self.alive_monsters[self.bd]]["BfDbf"]["bk"] == 0
                    self.dc2[self.m1]["ATK"]//2
                    self.bk_m += "バイキルトの効果がきえた"
            if self.dc2[self.alive_monsters[self.bd]]["BfDbf"]["rk"] > 0:
                self.dc2[self.alive_monsters[self.bd]]["BfDbf"]["rk"] += 1
                if self.dc2[self.alive_monsters[self.bd]]["BfDbf"]["rk"] == 4:
                    self.dc2[self.alive_monsters[self.bd]]["BfDbf"]["rk"] == 0
                    self.drc = self.dc2[self.alive_monsters[self.bd]]["DEF"]
                    while self.drc < self.primitive_dc[self.alive_monsters[self.bd]]["DEF"]:
                        self.drc += 1
                    self.rk_m += "ルカナンの効果がきえた"
            self.bd += 1

        return {"m1": self.m1, "m2": self.m2, "winner": self.winner, "btl_turn": self.btl_turn, "result": self.result, "cri": self.crip, "dod": self.dod1, "mp_con": self.mp_con, "message": self.message, "sl_dit": self.sleep_m, "jdm":self.jdmg_m, "jcm":self.j_rep, "bkm":self.bk_m, "rkm": self.rk_m}

        
