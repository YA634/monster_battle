import random
import copy
import cre_mons

class Pt_battle():
    li = ["HP", "MP", "ATK", "DEF", "SPD", "MAG", "Lv", "CON"]
    li2 = ["スライムLv8", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
    li3 = ["キングスライム", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
    li4 = ["勇者","賢者","パラディン","バトルマスター","スーパースター"]
    li5 = ["スライムLv8", "キングスライム", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
    cmds1 = ["たたかう","にげる"]

    def __init__(self, m_sta_dc, yp_sta_dc, vic_count, y_dc):
        self.primitive_m_dc = m_sta_dc
        self.primitive_y_dc = yp_sta_dc
        self.primitive_dc = self.primitive_m_dc|self.primitive_y_dc
        self.mdc = copy.deepcopy(self.primitive_m_dc)
        if vic_count == 0:
            self.ydc = copy.deepcopy(self.primitive_y_dc)
        else:
            self.ydc = y_dc
        self.dddc = {}
        self.sc = 1
        self.btl_turn = 0
        self.alive_monsters = ["スライムLv8", "ベホマスライム", "ドラゴスライム", "はぐれメタル", "スライムベス"]
        self.alive_members = ["勇者","賢者","パラディン","バトルマスター","スーパースター"]
        self.ali_co = 0
        while self.ali_co < len(self.alive_members):
            if self.ydc[self.alive_members[self.ali_co]]["HP"] == 0:
                self.alive_members.remove(self.alive_members[self.ali_co])
                self.ali_co -= 1
            self.ali_co += 1
        self.dead_mon = []
        self.dead_mem = []
        self.dc2 = self.mdc|self.ydc
        self.alive_all = self.alive_members + self.alive_monsters


    def d(self, m1, m2, x):
        self.dmg1 = (self.dc2[m1]["ATK"]*x - (self.dc2[m2]["DEF"])//2)//2
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
        if m1 in self.li4:
            self.ac = self.alive_monsters.copy()
        else:
            self.ac = self.alive_members.copy()
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
        elif mn == "勇者":
            self.pa = ['こうげき','ホイミ','バイキルト','ルカナン','どくの息','ラリホーマ','ミナデイン(一人)','まじんぎり']
        elif mn == "賢者":
            self.pa = ['こうげき','ホイミ','バイキルト','ルカナン','どくの息','ラリホーマ','イオナズン','まじんぎり']
        elif mn == "パラディン":
            self.pa = ['こうげき','ホイミ','メガザル','バイキルト','ルカナン','どくの息','ラリホーマ','まじんぎり']
        elif mn == "バトルマスター":
            self.pa = ['こうげき','ホイミ','バイキルト','ルカナン','どくの息','ラリホーマ','ばくれつけん','まじんぎり']
        elif mn == "スーパースター":
            self.pa = ['こうげき','ホイミ','ハッスルダンス','バイキルト','ルカナン','どくの息','ラリホーマ','まじんぎり']
        else:
            self.pa = ['こうげき','ホイミ','メラ','バイキルト','ルカナン','どくの息','ラリホーマ','まじんぎり']
        return self.pa

    def nmp_cmd_li(self, mn):
        if mn == "ベホマスライム":
            self.pa = ['こうげき','まじんぎり']
        elif mn == "スライムLv8":
            if self.sc == 8:
                self.pa = ['こうげき','合体','まじんぎり']
            else:
                self.pa = ['こうげき','なかまをよぶ','まじんぎり']
        elif mn == "キングスライム":
            self.pa = ['こうげき','まじんぎり']
        elif mn == "ドラゴスライム":
            self.pa = ['こうげき','まじんぎり']
        elif mn == "スライムベス":
            self.pa = ['こうげき','まじんぎり']
        elif mn == "勇者":
            self.pa = ['こうげき','ホイミ','バイキルト','ルカナン','どくの息','ラリホーマ','ミナデイン(一人)','まじんぎり']
        elif mn == "賢者":
            self.pa = ['こうげき','ホイミ','バイキルト','ルカナン','どくの息','ラリホーマ','イオナズン','まじんぎり']
        elif mn == "パラディン":
            self.pa = ['こうげき','ホイミ','メガザル','バイキルト','ルカナン','どくの息','ラリホーマ','まじんぎり']
        elif mn == "バトルマスター":
            self.pa = ['こうげき','ホイミ','バイキルト','ルカナン','どくの息','ラリホーマ','ばくれつけん','まじんぎり']
        elif mn == "スーパースター":
            self.pa = ['こうげき','ホイミ','ハッスルダンス','バイキルト','ルカナン','どくの息','ラリホーマ','まじんぎり']
        else:
            self.pa = ['こうげき','ホイミ','メラ','バイキルト','ルカナン','どくの息','ラリホーマ','まじんぎり']
        return self.pa

    def speed_cul(self, alive_all_li):
        self.sp_li = []
        self.spli = [self.dc2[alive_all_li[i]]["SPD"]+random.randint(0,10) for i in range(len(alive_all_li))]
        self.spdc = {alive_all_li[k]: self.spli[k] for k in range(len(alive_all_li))}
        self.sort_spdc = sorted(self.spdc.items(), key = lambda x: x[1], reverse = True,)
        for i in range(len(alive_all_li)):
            self.sp_li.append(self.sort_spdc[i][0])
        return self.sp_li

    def start(self, cmd_dc):
        self.winner = None
        self.btl_turn += 1
        for i in range(len(self.alive_monsters)):
            if self.dc2[self.alive_monsters[i]]["MP"] > 4:
                cmd_dc[self.alive_monsters[i]] = [random.choice(self.cmd_li(self.alive_monsters[i])), random.choice(self.alive_members)]
            else:
                cmd_dc[self.alive_monsters[i]] = [random.choice(self.nmp_cmd_li(self.alive_monsters[i])), random.choice(self.alive_members)]
        self.sp_li = self.speed_cul(self.alive_all)
        self.crip = 0
        self.dod1 = None
        self.mp_con = 0
        self.message = ""
        self.jdmg_m = ""
        self.j_rep = ""
        self.bk_m = ""
        self.rk_m = ""
        self.sleep_m = 0
        self.action = 0
        self.result = []
        
        while self.action < (len(self.alive_all)):
            self.show_dmg = ""
            self.show_j = ""
            self.m1 = self.sp_li[self.action]

            if self.m1 not in cmd_dc:
                print(f"Warning: {self.m1} not in cmd_dc, skipping")
                self.action += 1
                continue

            self.m2 = cmd_dc[self.m1][1]
            self.cmd = cmd_dc[self.m1][0]
            if self.m1 in self.li4:
                self.alive_ag = self.alive_monsters
                self.alive_co = self.alive_members
                self.dead_co = self.dead_mem
                self.dead_ag = self.dead_mon
            else:
                self.alive_ag = self.alive_members
                self.alive_co = self.alive_monsters
                self.dead_co = self.dead_mon
                self.dead_ag = self.dead_mem
            
            if self.m2 not in self.alive_ag:
                if len(self.alive_ag) > 0:
                    self.m2 = random.choice(self.alive_ag)
                    print(f"{self.m1}'s target is dead, new target: {self.m2}")
                else:
                    # 対象がいない場合は勝利確定
                    self.action += 1
                    continue

            self.liaa = self.aselect(self.m1)
            self.m1hp = self.dc2[self.m1]["HP"]; self.m2hp = self.dc2[self.m2]["HP"]
            self.m1mp = self.dc2[self.m1]["MP"]; self.m2mp = self.dc2[self.m2]["MP"]
            jm1li = list(self.dc2[self.m1]['CON'].keys())
            self.atk_ef = ""
            if "ねむり" in jm1li:
                #print(f"{m1}→{m2}")
                self.sleep_m += 1
                self.result.append(f"{self.m1}はねむっている!")
            else:
                if self.cmd == 'こうげき':
                    self.dod1 = self.dod(self.m1, self.m2, 1)
                    if self.dod1 == True:
                        self.dmg = 0
                        self.atk_ef = "回避！"
                        pass
                    else:
                        self.crip = random.randint(1, 32)
                        if self.crip == 1:
                            self.dmg = self.cri(self.m1)
                            self.dc2[self.m2]["HP"] -= self.dmg
                            #print(f"{self.dmg}damage かいしんのいちげき！")
                            self.atk_ef = "かいしんのいちげき！"
                        else:
                            self.dmg = self.d(self.m1, self.m2, 1)
                            self.dc2[self.m2]["HP"] -= self.dmg
                            #print(f"{self.dmg}damage")
                        #print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                        if self.dc2[self.m2]["HP"] <= 0:
                            self.message += f"{self.m2}のHPは0になってしまった... out "
                            self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}                                                
                            self.alive_ag.remove(self.m2)
                            self.alive_all.remove(self.m2)
                            self.dead_ag.append(self.m2)
                            if self.sp_li.index(self.m2) < self.action:
                                self.action -= 1
                            self.sp_li.remove(self.m2)
                            if (len(self.alive_members) == 0) or  (len(self.alive_monsters) == 0 ):
                                self.winner = self.m1
                    self.result.append(f"{self.m1}は{self.m2}に攻撃した  {self.atk_ef}  {self.dmg}ダメージ")

                elif self.cmd == 'まじんぎり':
                    self.dod1 = self.dod(self.m1, self.m2, 1)
                    if self.dod1 == True:
                        self.dmg = 0
                        self.atk_ef = "回避！"
                        pass

                    else:
                        self.mpro = random.randint(0, 1)
                        if self.mpro == 0:
                            self.dmg = 0
                            self.atk_ef = "ミス！"
                            #print("ミス")
                        else:
                            self.crip = random.randint(1, 32)
                            if self.crip == 1:
                                self.dmg = self.cri(self.m1)*2
                                self.dc2[self.m2]["HP"] -= self.dmg
                                self.atk_ef = "かいしんのいちげき！"
                                #print(f"{self.dmg}damage かいしんのいちげき！")
                            else:
                                self.dmg = self.d(self.m1, self.m2, 2)
                                self.dc2[self.m2]["HP"] -= self.dmg
                                #print(f"{self.dmg}damage")
                            #print(f"{self.mons1}の残りHP{self.m1hp}　{self.mons2}の残りHP{self.m2hp}")
                            if self.dc2[self.m2]["HP"] <= 0:
                                self.message += f"{self.m2}のHPは0になってしまった... out "
                                self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}                                                    
                                self.alive_ag.remove(self.m2)
                                self.alive_all.remove(self.m2)
                                self.dead_ag.append(self.m2)
                                if self.sp_li.index(self.m2) < self.action:
                                    self.action -= 1
                                self.sp_li.remove(self.m2)
                                if (len(self.alive_members) == 0) or  (len(self.alive_monsters) == 0 ):
                                    self.winner = self.m1
                            else:
                                self.af = random.randint(0, 1)
                    self.result.append(f"{self.m1}は{self.m2}にまじんぎりをはなった  {self.atk_ef}  {self.dmg}ダメージ")
 
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
                        self.atk_ef = "HPを10回復した"
                    else:
                        self.atk_ef = "MPが足りない！"
                    self.result.append(f"{self.m1}はホイミを使った  {self.atk_ef}")
                
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
                        self.atk_ef = "HPを10回復した"
                    else:
                        self.atk_ef = "MPが足りない！"
                    self.result.append(f"{self.m1}はベホマを使った  {self.atk_ef}")
                
                elif self.cmd == 'メガザル':
                    if len(self.alive_co) < 5:
                        self.dc2[self.m1]["MP"] = 0
                        self.rec = 0
                        while self.rec < len(self.dead_co):
                            self.dc2[self.dead_co[self.rec]]["HP"] = self.primitive_dc[self.dead_co[self.rec]]["HP"]; self.dc2[self.dead_co[self.rec]]["CON"] = {"げんき": 1} 
                            self.alive_ag.append(self.dead_co[self.rec])
                            self.alive_all.append(self.dead_co[self.rec])
                            self.atk_ef += f"{self.dead_co[self.rec]}のHPとMPが全回復した！"
                            self.dead_co.remove(self.dead_co[self.rec])
                            self.rec += 1
                        self.message += f"{self.m1}のHPは0になってしまった... out "
                        self.dc2[self.m1]["HP"] = 0; self.dc2[self.m1]["CON"] = {"ひんし": 1}                                                    
                        self.alive_co.remove(self.m1)
                        self.alive_all.remove(self.m1)
                        self.dead_co.append(self.m1)  
                        self.action -= 1
                    else:
                        self.atk_ef = "ひんしの仲間はいなかった！"
                    self.result.append(f"{self.m1}はみずからのいのちをなげうってメガザルをつかった！  {self.atk_ef}")    

                elif self.cmd == 'ハッスルダンス':
                    self.liaa = self.alive_co
                    self.ac = 0
                    while self.ac < len(self.liaa):
                        self.dc2[self.liaa[self.ac]]["HP"] += 15
                        self.atk_ef += f"{self.liaa[self.ac]}はHPを15回復した  "
                        if self.dc2[self.liaa[self.ac]]["HP"] > self.primitive_dc[self.liaa[self.ac]]["HP"]:
                            while self.dc2[self.liaa[self.ac]]["HP"] > self.primitive_dc[self.liaa[self.ac]]["HP"]:
                                self.dc2[self.liaa[self.ac]]["HP"] -= 1
                                if self.dc2[self.liaa[self.ac]]["HP"] == self.primitive_dc[self.liaa[self.ac]]["HP"]:
                                    break
                        self.ac += 1
                    self.result.append(f"{self.m1}はハッスルダンスをつかった！  {self.atk_ef}")

                elif self.cmd == 'キアリー':
                    #print(f"{self.m1}はホイミをつかった！")
                    if self.m1mp >= 4:
                        self.dc2[self.m1]["CON"] = {"げんき": 1}
                        self.dc2[self.m1]["MP"] -= 4
                        self.atk_ef = "状態異常を全回復した"
                    else:
                        self.atk_ef = "MPが足りない！"
                    self.result.append(f"{self.m1}はキアリーを使った  {self.atk_ef}")

                elif self.cmd == 'バイキルト':
                    #print(f"{m1}はバイキルトをつかった！")
                    if self.m1mp >= 4:
                        self.dc2[self.m1]["MP"] -= 4
                        #print(f"{self.m1}の攻撃力は2倍になった！")
                        if self.dc2[self.m1]["BfDbf"]["bk"] == 0:
                            self.dc2[self.m1]["ATK"] *= 2
                        self.dc2[self.m1]["BfDbf"]["bk"] = 1
                        self.atk_ef = "攻撃力が2倍になった!"
                    else:
                        #print("MPがたりない！")
                        self.atk_ef = "MPが足りない！"
                    self.result.append(f"{self.m1}はバイキルトを使った  {self.atk_ef}")

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
                        self.atk_ef = self.show_j
                    else:
                        self.atk_ef = "MPが足りない！"
                    self.result.append(f"{self.m1}はルカナンを使った  {self.atk_ef}")

                elif self.cmd == 'なかまをよぶ':
                    #print(f"{self.m1}はホイミをつかった！")
                    self.sc += 1 #確率で失敗
                    self.result.append(f"スライムLv8はなかまをよんだ スライムLv8の数{self.sc}")

                elif self.cmd == '合体':
                    #print("スライムLv8たちが合体していく！")
                    #print("キングスライムがあらわれた！")
                    self.primitive_dc["キングスライム"] = {self.li[i]: random.randint(100, 150) for i in range(len(self.li)-1)}
                    self.primitive_dc["キングスライム"]["Lv"] = divmod((self.primitive_dc["キングスライム"]["HP"] + self.primitive_dc["キングスライム"]["MP"] + self.primitive_dc[f"キングスライム"]["ATK"] + self.primitive_dc[f"キングスライム"]["DEF"] + self.primitive_dc[f"キングスライム"]["SPD"] + self.primitive_dc["キングスライム"]["MAG"]), 10)[0]
                    self.dc2["キングスライム"] = copy.deepcopy(self.primitive_dc["キングスライム"])
                    self.alive_ag.remove("スライムLv8")
                    self.alive_ag.append("キングスライム")
                    self.alive_all.remove("スライムLv8")
                    self.alive_all.append("キングスライム")
                    self.result.append(f"スライムLv8たちが合体していく！<br>キングスライムがあらわれた！")

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
                            self.atk_ef = "回避！"
                            pass

                        else:
                            if self.crip == 1:
                                self.dmg = self.cri(self.m1)*3//2
                                self.dc2[self.m2]["HP"] -= self.dmg
                                #print(f"{dmg}damage かいしんのいちげき！")
                                #print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                self.atk_ef = "かいしんのいちげき！"
                            else:                     
                                self.dmg = self.md(self.m1, self.m2, 1)
                                self.dc2[self.m2]["HP"] -= self.dmg
                                #print(f"{dmg}damage")
                                #print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                            if self.dc2[self.m2]["HP"] <= 0:
                                self.message += f"{self.m2}のHPは0になってしまった... out"
                                self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}                      
                                self.alive_ag.remove(self.m2)
                                self.alive_all.remove(self.m2)
                                self.dead_ag.append(self.m2)
                                if self.sp_li.index(self.m2) < self.action:
                                    self.action -= 1
                                self.sp_li.remove(self.m2)
                                if (len(self.alive_members) == 0) or  (len(self.alive_monsters) == 0 ):
                                    self.winner = self.m1
                    else:
                        self.atk_ef = "MPがたりない！"
                        self.dmg = 0
                    self.result.append(f"{self.m1}は{self.m2}にメラをはなった  {self.atk_ef}  {self.dmg}ダメージ")

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
                                self.atk_ef = "回避！"
                                self.show_dmg += f"{self.atk_ef}  {self.liaa[self.ac]}に0ダメージ  "
                            else:
                                self.crip = random.randint(1, 32)
                                if self.crip == 1:
                                    self.dmg = self.cri(self.m1)*3//2
                                    self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                    self.atk_ef = "かいしんのいちげき！"
                                else:
                                    self.dmg = self.md(self.m1, self.liaa[self.ac], 1)
                                    self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                self.show_dmg += f"{self.atk_ef}  {self.liaa[self.ac]}に{self.dmg}ダメージ  "
                                if self.dc2[self.liaa[self.ac]]["HP"] <= 0:
                                    self.message += f"{self.liaa[self.ac]}のHPは0になってしまった... out"
                                    self.dc2[self.liaa[self.ac]]["HP"] = 0; self.dc2[self.liaa[self.ac]]["CON"] = {"ひんし": 1}
                                    self.alive_ag.remove(self.liaa[self.ac])
                                    self.alive_all.remove(self.liaa[self.ac])
                                    self.dead_ag.append(self.m2)
                                    if self.sp_li.index(self.liaa[self.ac]) < self.action:
                                        self.action -= 1
                                    self.sp_li.remove(self.liaa[self.ac])
                                    if (len(self.alive_members) == 0) or  (len(self.alive_monsters) == 0 ):
                                        self.winner = self.m1
                            self.ac += 1
                            self.atk_ef = ""
                    else:
                        self.atk_ef = "MPがたりない！"
                    self.result.append(f"{self.m1}はかえんの息をつかった！  {self.atk_ef}  {self.show_dmg}")

                elif self.cmd == 'ばくれつけん':
                    self.act = 0
                    while self.act < 4:
                        self.liaa = self.aselect(self.m1)
                        if len(self.liaa) > 0:
                            self.ac = random.randint(0,len(self.liaa)-1)
                        else:
                            continue
                        self.dod1 = self.dod(self.m1, self.liaa[self.ac], 2)
                        if self.dod1 == True:
                            #print(f"{liaa[ac]}はイオナズンをかわした！  ")
                            #print(f"{m2s}の残りHP{m2hp}!  ")
                            self.atk_ef = "回避！"
                            self.show_dmg += f"{self.atk_ef}  {self.liaa[self.ac]}に0ダメージ  "
                        else:
                            self.crip = random.randint(1, 32)
                            if self.crip == 1:
                                self.dmg = self.cri(self.m1)*3//2
                                self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                self.atk_ef = "かいしんのいちげき！"
                            else:
                                self.dmg = self.d(self.m1, self.liaa[self.ac], 2)
                                self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                            self.show_dmg += f"{self.atk_ef}  {self.liaa[self.ac]}に{self.dmg}ダメージ  "
                            if self.dc2[self.liaa[self.ac]]["HP"] <= 0:
                                self.message += f"{self.liaa[self.ac]}のHPは0になってしまった... out"
                                self.dc2[self.liaa[self.ac]]["HP"] = 0; self.dc2[self.liaa[self.ac]]["CON"] = {"ひんし": 1}
                                self.alive_ag.remove(self.liaa[self.ac])
                                self.alive_all.remove(self.liaa[self.ac])
                                self.dead_ag.append(self.m2)
                                if self.sp_li.index(self.liaa[self.ac]) < self.action:
                                    self.action -= 1
                                self.sp_li.remove(self.liaa[self.ac])
                                if (len(self.alive_members) == 0) or  (len(self.alive_monsters) == 0 ):
                                    self.winner = self.m1
                        self.act += 1
                        self.atk_ef = ""
                    self.result.append(f"{self.m1}はばくれつけんをつかった！  {self.show_dmg}")

                elif self.cmd == 'ミナデイン(一人)':
                    #print(f"{m1}はメラをつかった！")
                    self.crip = random.randint(1, 32)
                    if self.m1mp >= 20:
                        self.dc2[self.m1]["MP"] -= 20
                        self.dod1 = self.dod(self.m1, self.m2, 5)
                        if self.dod1 == True:
                            #print("回避成功")
                            #print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}!  　　")
                            self.dmg = 0
                            self.atk_ef = "回避！"
                            pass

                        else:
                            if self.crip == 1:
                                self.dmg = self.cri(self.m1)*3//2
                                self.dc2[self.m2]["HP"] -= self.dmg
                                #print(f"{dmg}damage かいしんのいちげき！")
                                #print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                                self.atk_ef = "かいしんのいちげき！"
                            else:                     
                                self.dmg = self.md(self.m1, self.m2, 10)
                                self.dc2[self.m2]["HP"] -= self.dmg
                                #print(f"{dmg}damage")
                                #print(f"{mons1}の残りHP{m1hp}　{mons2}の残りHP{m2hp}")
                            if self.dc2[self.m2]["HP"] <= 0:
                                self.message += f"{self.m2}のHPは0になってしまった... out"
                                self.dc2[self.m2]["HP"] = 0; self.dc2[self.m2]["CON"] = {"ひんし": 1}                      
                                self.alive_ag.remove(self.m2)
                                self.alive_all.remove(self.m2)
                                self.dead_ag.append(self.m2)
                                if self.sp_li.index(self.m2) < self.action:
                                    self.action -= 1
                                self.sp_li.remove(self.m2)
                                if (len(self.alive_members) == 0) or  (len(self.alive_monsters) == 0 ):
                                    self.winner = self.m1
                    else:
                        self.atk_ef = "MPがたりない！"
                        self.dmg = 0
                    self.result.append(f"{self.m1}は{self.m2}にミナデインをはなった  {self.atk_ef}  {self.dmg}ダメージ")

                elif self.cmd == 'イオナズン':
                    #print(f"{m1}はイオナズンをつかった！")
                    if self.m1mp >= 25:
                        self.dc2[self.m1]["MP"] -= 25
                        self.liaa = self.aselect(self.m1)
                        self.ac = 0
                        while self.ac < len(self.liaa):
                            self.dod1 = self.dod(self.m1, self.liaa[self.ac], 3)
                            if self.dod1 == True:
                                self.atk_ef = "回避！"
                                self.show_dmg += f"{self.atk_ef}  {self.liaa[self.ac]}に0ダメージ  "
                            else:
                                self.crip = random.randint(1, 32)
                                if self.crip == 1:
                                    self.dmg = self.cri(self.m1)*3//2
                                    self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                    self.atk_ef = "かいしんのいちげき！"
                                else:
                                    self.dmg = self.md(self.m1, self.liaa[self.ac], 4)
                                    self.dc2[self.liaa[self.ac]]["HP"] -= self.dmg
                                self.show_dmg += f"{self.atk_ef}  {self.liaa[self.ac]}に{self.dmg}ダメージ  "
                                if self.dc2[self.liaa[self.ac]]["HP"] <= 0:
                                    self.message += f"{self.liaa[self.ac]}のHPは0になってしまった... out"
                                    self.dc2[self.liaa[self.ac]]["HP"] = 0; self.dc2[self.liaa[self.ac]]["CON"] = {"ひんし": 1}
                                    self.alive_ag.remove(self.liaa[self.ac])
                                    self.alive_all.remove(self.liaa[self.ac])
                                    self.dead_ag.append(self.m2)
                                    if self.sp_li.index(self.liaa[self.ac]) < self.action:
                                        self.action -= 1
                                    self.sp_li.remove(self.liaa[self.ac])
                                    if (len(self.alive_members) == 0) or  (len(self.alive_monsters) == 0 ):
                                        self.winner = self.m1
                            self.ac += 1
                            self.atk_ef = ""
                    else:
                        self.atk_ef = "MPがたりない！"
                    self.result.append(f"{self.m1}はイオナズンを使った  {self.atk_ef}  {self.show_dmg}")



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
                        self.atk_ef = ""
                    else:
                        self.atk_ef = "MPがたりない！"
                    self.result.append(f"{self.m1}はどくの息を使った  {self.atk_ef}  {self.show_j}")
                    

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
                        self.atk_ef = ""
                    else:
                        self.atk_ef = "MPがたりない！"
                    self.result.append(f"{self.m1}はラリホーマをつかった！  {self.atk_ef}  {self.show_j}")
            self.action += 1


        # if "キングスライム" in self.alive_monsters:
        #     self.u_li = self.li3 + self.li4
        # else:
        #     self.u_li = self.li2 + self.li4
        self.u_li = self.alive_all
        self.dk = 0
        while self.dk < len(self.alive_all):
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
                            if self.dm in self.li4:
                                self.alive_members.remove(self.dm)
                                self.dead_mem.append(self.dm)
                            else:
                                self.alive_monsters.remove(self.dm)
                                self.dead_mon.append(self.dm)
                            self.alive_all.remove(self.dm)
                            if (len(self.alive_members) == 0) or (len(self.alive_monsters) == 0 ):
                                self.winner = self.alive_all[0]
                            self.dk -= 1
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
                            if self.dm in self.li4:
                                self.alive_members.remove(self.dm)
                                self.dead_mem.append(self.dm)
                            else:
                                self.alive_monsters.remove(self.dm)
                                self.dead_mon.append(self.dm)
                            self.alive_all.remove(self.dm)
                            if (len(self.alive_members) == 0) or  (len(self.alive_monsters) == 0 ):
                                self.winner = self.alive_all[0]
                            self.dk -= 1
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
                    self.dc2[self.alive_monsters[self.bd]]["ATK"]//2
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

        if self.winner in self.li4:
            self.winner = "勇者パーティー"
        elif self.winner in self.li5:
            self.winner = "モンスターの集団"
        return {"winner": self.winner, "btl_turn": self.btl_turn, "result": self.result, "cri": self.crip, "dod": self.dod1, "mp_con": self.mp_con, "message": self.message, "sl_dit": self.sleep_m, "jdm":self.jdmg_m, "jcm":self.j_rep, "bkm":self.bk_m, "rkm": self.rk_m}
