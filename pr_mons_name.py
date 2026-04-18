# Python
from flask import Flask, request, redirect, render_template, url_for, session
import copy
import cre_mons
import cre_y_pt
import battle
import pt_battle
import random
import pymysql
import pymysql.cursors

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'
# mli = [];# bet_m = [];# odds_dc = {}
def getConnection():
    return pymysql.connect(
        host='localhost',
        db='battle_royal',
        user='root',
        password='rootuser',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route("/")
def get():
    session['mon_error'] = 0
    session["vic_count"] = 0
    return render_template("login.html")

@app.route("/input0", methods=["GET", "POST"])
def input0():
    if request.method == "POST":
        user_name = request.form["name"]
    connection = getConnection()
    sql = "SELECT name FROM user"
    cursor = connection.cursor()
    cursor.execute(sql)
    users = cursor.fetchall()
    # sql = "SELECT COUNT(name) FROM user"
    # cursor = connection.cursor()
    # cursor.execute(sql)
    # user_count = cursor.fetchall()
    sql = "SELECT COUNT(*) as count FROM user"
    cursor.execute(sql)
    count_result = cursor.fetchone()
    name_li = []
    for i in range(count_result['count']):
        for key, value in users[i].items():
            name_li.append(value)
    if user_name in name_li:
        sql = "SELECT money FROM user WHERE name = %s"
        cursor = connection.cursor()
        cursor.execute(sql, user_name)
        money = cursor.fetchone()
        session["money"] = money["money"]
        session["mes0"] = "おかえり"
    else:
        sql = "INSERT INTO user(id,name,money) VALUES(%s,%s,%s)"
        cursor = connection.cursor()
        money = 100
        cursor.execute(sql, (count_result['count']+1,user_name,int(money)))
        session["money"] = int(money)
        session["mes0"] = "ようこそ"
    connection.commit()
    cursor.close()
    connection.close()   
    session['user_name'] = user_name
    return redirect(url_for('create_m'))

@app.route("/create")
def create_m():
    user_name = session.get('user_name')
    money = session.get('money')
    mon_error = session.get('mon_error')
    message0 = session.get('mes0')
    message1 = user_name
    message2 = money
    message3 = "賭けるモンスターと賭け金を入力"
    if mon_error == 1:
        message4 = "所持金が足りません"
        session['mon_error'] = 0
    else:
        message4 = ""
    primitive_dc = cre_mons.create_mons()
    m_dc = copy.deepcopy(primitive_dc)
    odds_dc = cre_mons.create_odds(m_dc)
    session['primitive_dc'] = primitive_dc
    session['odds_dc'] = odds_dc
    m_name_li = []
    for key, value in m_dc.items():
            m_name_li.append(key)
    session['mn_li'] = m_name_li
    session.pop('battle_instance', None)
    battle_instance = battle.Mons_battle(primitive_dc)
    # Pythonオブジェクトをシリアライズして保存
    session['battle_state'] = {
        'dc2': copy.deepcopy(battle_instance.dc2),
        'mc': battle_instance.mc,
        'sc': battle_instance.sc,
        'alive_monsters': list(battle_instance.alive_monsters),
        'btl_turn': battle_instance.btl_turn
    }

    connection = getConnection()
    sql = "SELECT COUNT(winner_id) FROM winners"
    cursor = connection.cursor()
    cursor.execute(sql)
    w_id_count = cursor.fetchall()
    w_l_id = w_id_count[0]['COUNT(winner_id)']
    sql = "SELECT winner_id,name,hp,mp,atk,def,spd,mag,lv,odds FROM winners WHERE winner_id BETWEEN %s AND %s"
    cursor = connection.cursor()
    if w_l_id >= 5:
        cursor.execute(sql,(w_l_id-4,w_l_id))
        winner_infos = cursor.fetchall()
    else:
        cursor.execute(sql,(1,w_l_id))
        winner_infos = cursor.fetchall()

    cursor.close()
    connection.close()
    return render_template("pr_mons.html", m_dc = m_dc, names = m_name_li, odds_dc = odds_dc, message0 = message0, message1 = message1, message2 = message2, message3 = message3, message4 = message4, winner_infos = winner_infos)

@app.route("/input_clear", methods=["GET", "POST"])
def input_clear():
    user_name = session.get('user_name')
    connection = getConnection()
    sql = "UPDATE user SET money = %s WHERE name = %s"
    cursor = connection.cursor()
    mn = 100
    cursor.execute(sql, (int(mn), user_name))
    # sql = "TRUNCATE TABLE winners"
    # cursor = connection.cursor()
    # cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()
    session['money'] = int(mn)
    return redirect(url_for('create_m'))

@app.route("/input", methods=["GET", "POST"])
def input():
    if request.method == "POST":
        mons_select = request.form["mons_select"]
        bet_money = int(request.form["bet"])
    # else:
    user_name = session.get('user_name')
    money = session.get('money')
    if money < bet_money:
        session['mon_error'] = 1
        return redirect(url_for('create_m'))
    money -= bet_money
    session["money"] = money
    connection = getConnection()
    sql = "UPDATE user SET money = %s WHERE name = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (money,user_name))
    connection.commit()
    cursor.close()
    connection.close()
    session['mons_select'] = mons_select
    session['bet_money'] = bet_money
    mn_li = session.get('mn_li')
    mli = []
    while len(mli) < 2:
        mons = random.choice(mn_li)
        if not(mons in mli):
            mli.append(mons)
    session['bm_li'] = mli
    session['pt_c'] = 0
    if mli[0] == mons_select: 
        return redirect(url_for('battle_p_turn'))
    else:
        return redirect(url_for('battle_turn'))

@app.route("/battle")
def battle_turn():
    primitive_dc = session.get('primitive_dc')
    battle_state = session.get('battle_state')
    p_mons = session.get('mons_select')
    battle_instance = battle.Mons_battle(primitive_dc)
    battle_instance.dc2 = copy.deepcopy(battle_state['dc2'])
    battle_instance.mc = battle_state['mc']
    battle_instance.sc = battle_state['sc']
    battle_instance.alive_monsters = list(battle_state['alive_monsters'])
    battle_instance.btl_turn = battle_state['btl_turn']
    b_m_li = session.get('bm_li')
    pt_c = session.get('pt_c')
    m_dc = battle_instance.dc2
    jm1li = list(m_dc[p_mons]['CON'].keys())
    if b_m_li[0] == p_mons and pt_c == 0 and (not('ねむり' in jm1li)):
        return redirect(url_for('battle_p_turn'))
    elif b_m_li[0] == p_mons and pt_c == 1:
        session['pt_c'] = 0
        cmd = session.get('cmd')
        result1 = battle_instance.start(b_m_li, cmd, p_mons)
    elif b_m_li[0] == p_mons and pt_c == 0 and ('ねむり' in jm1li):
        cmd = 'こうげき'
        result1 = battle_instance.start(b_m_li, cmd, p_mons)
    else:
        cmd = 'こうげき'
        result1 = battle_instance.start(b_m_li, cmd, p_mons)
    session['battle_state'] = {
        'dc2': copy.deepcopy(battle_instance.dc2),
        'mc': battle_instance.mc,
        'sc': battle_instance.sc,
        'alive_monsters': list(battle_instance.alive_monsters),
        'btl_turn': battle_instance.btl_turn
    }
    session.modified = True
    if result1["winner"] is None:
        # return redirect(url_for('/battle')), render_template("battle.html", result1)
        names = session.get('mn_li')
        odds_dc = session.get('odds_dc')
        b_m_li = battle_instance.m_s()
        session['bm_li'] = b_m_li
        return render_template("battle.html", result1 = result1, m_dc = m_dc, names = names, odds_dc = odds_dc, primitive_dc = primitive_dc)
    else:
        session['winner'] = result1["winner"]
        session.pop('battle_state', None)
        return redirect(url_for('result'))

@app.route("/battle_p")
def battle_p_turn():
    session['pt_c'] = 1
    primitive_dc = session.get('primitive_dc')
    battle_state = session.get('battle_state')
    p_mons = session.get('mons_select')
    battle_instance = battle.Mons_battle(primitive_dc)
    battle_instance.dc2 = copy.deepcopy(battle_state['dc2'])
    battle_instance.mc = battle_state['mc']
    battle_instance.sc = battle_state['sc']
    battle_instance.alive_monsters = list(battle_state['alive_monsters'])
    battle_instance.btl_turn = battle_state['btl_turn']
    bm_li = session.get('bm_li')
    session['battle_state'] = {
        'dc2': copy.deepcopy(battle_instance.dc2),
        'mc': battle_instance.mc,
        'sc': battle_instance.sc,
        'alive_monsters': list(battle_instance.alive_monsters),
        'btl_turn': battle_instance.btl_turn
    }
    cmds = battle_instance.cmd_li(p_mons)
    session.modified = True
    m_dc = battle_instance.dc2
    names = session.get('mn_li')
    odds_dc = session.get('odds_dc')
    return render_template("battle_p.html", cmds = cmds, bm_li = bm_li, m_dc = m_dc, names = names, odds_dc = odds_dc, primitive_dc = primitive_dc)

@app.route("/skip", methods=["GET", "POST"])
def skip():
    wn = 0
    while wn < 1:
        primitive_dc = session.get('primitive_dc')
        battle_state = session.get('battle_state')
        p_mons = session.get('mons_select')
        battle_instance = battle.Mons_battle(primitive_dc)
        battle_instance.dc2 = copy.deepcopy(battle_state['dc2'])
        battle_instance.mc = battle_state['mc']
        battle_instance.sc = battle_state['sc']
        battle_instance.alive_monsters = list(battle_state['alive_monsters'])
        battle_instance.btl_turn = battle_state['btl_turn']
        b_m_li = session.get('bm_li')
        cmd = 'こうげき'
        result1 = battle_instance.start(b_m_li, cmd, p_mons)
        session['battle_state'] = {
            'dc2': copy.deepcopy(battle_instance.dc2),
            'mc': battle_instance.mc,
            'sc': battle_instance.sc,
            'alive_monsters': list(battle_instance.alive_monsters),
            'btl_turn': battle_instance.btl_turn
        }
        session.modified = True
        if result1["winner"] is not None:
            wn += 1
        else:
            b_m_li = battle_instance.m_s()
            session['bm_li'] = b_m_li
    session['winner'] = result1["winner"]
    session.pop('battle_state', None)
    return redirect(url_for('result'))
        

@app.route("/input2", methods=["GET", "POST"])
def input2():
    if request.method == "POST":
        cmd_select = request.form["battle_cmd"]
    session['cmd'] = cmd_select
    return redirect(url_for('battle_turn'))

@app.route("/result")
def result():
    mons_select = session.get('mons_select')
    bet_money = session.get('bet_money')
    odds_dc = session.get('odds_dc')
    if not mons_select or not bet_money or not odds_dc:
        return redirect(url_for('create_m'))
    winner = session.get('winner')
    wm = int(bet_money * odds_dc[mons_select])
    wc = 0
    message1 = "バトロワの勝者は" + winner
    if mons_select == winner:
        message2 = f"あなたの勝ち  {wm}円 got"
        wc += 1
    else:
        if (mons_select == "スライムLv8") and (winner == "キングスライム"):
            message2 = f"あなたの勝ち  {wm}円 got"
            wc += 1
        else:
            message2 = f"あなたの負けです {bet_money}円 lost"

    primitive_dc = session.get('primitive_dc')
    connection = getConnection()

    try:
        sql = "SELECT COUNT(winner_id) FROM winners"
        cursor = connection.cursor()
        cursor.execute(sql)
        w_id_count = cursor.fetchall()
        w_id = w_id_count[0]['COUNT(winner_id)'] +1
        sql = "INSERT INTO winners(winner_id,name,hp,mp,atk,def,spd,mag,lv,odds) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor = connection.cursor()
        cursor.execute(sql, (w_id,winner,primitive_dc[winner]["HP"],primitive_dc[winner]["MP"],primitive_dc[winner]["ATK"],primitive_dc[winner]["DEF"],primitive_dc[winner]["SPD"],primitive_dc[winner]["MAG"],primitive_dc[winner]["Lv"],odds_dc[winner]))
        if wc == 1:
            user_name = session.get('user_name')
            money = session.get('money')
            money += wm
            session["money"] = money
            sql = "UPDATE user SET money = %s WHERE name = %s"
            cursor = connection.cursor()
            cursor.execute(sql, (money,user_name))
    except Exception as e:
        connection.rollback()
        print(f"データベースエラー: {e}")
    connection.commit()
    cursor.close()
    connection.close()

    return render_template("result.html", message1 = message1, message2 = message2)








@app.route("/pt_battle_home", methods=["GET", "POST"])
def pt_battle_home():
    user_name = session.get('user_name')
    money = session.get('money')
    mon_error = session.get('mon_error')
    message0 = session.get('mes0')
    message1 = user_name
    message2 = money
    if mon_error == 1:
        message4 = "所持金が足りません"
        session['mon_error'] = 0
    else:
        message4 = ""
    vic_count = session.get('vic_count')
    
    if vic_count == 0:
        primitive_m_dc = session.get('primitive_dc')
        primitive_y_dc = cre_y_pt.create_pt()
        y_dc = copy.deepcopy(primitive_y_dc)
        session.pop('battle_state', None)
    else:
        primitive_m_dc = cre_mons.create_mons()
        primitive_y_dc = session.get('primitive_y_dc')
        battle_state = session.get('pt_battle_state')
        y_dc = copy.deepcopy(battle_state['ydc'])
    m_dc = copy.deepcopy(primitive_m_dc)
    session['primitive_m_dc'] = primitive_m_dc
    session['primitive_y_dc'] = primitive_y_dc
    m_name_li = []
    for key, value in m_dc.items():
            m_name_li.append(key)
    yp_name_li = []
    for key, value in y_dc.items():
            yp_name_li.append(key)           
    session['mn_li'] = m_name_li
    session['ypn_li'] = yp_name_li
    session.pop('pt_battle_instance', None)
    battle_instance = pt_battle.Pt_battle(primitive_m_dc,primitive_y_dc,vic_count,y_dc)
    cmds1 = battle_instance.cmds1

    # Pythonオブジェクトをシリアライズして保存
    session['pt_battle_state'] = {
        'mdc': copy.deepcopy(battle_instance.mdc),
        'ydc': copy.deepcopy(battle_instance.ydc),
        'dc2': copy.deepcopy(battle_instance.dc2),
        'sc': battle_instance.sc,
        'alive_monsters': list(battle_instance.alive_monsters),
        'alive_members': list(battle_instance.alive_members),
        'btl_turn': battle_instance.btl_turn
    }
    return render_template("pr_pt_bt_home.html", m_dc = m_dc,y_dc = y_dc, m_names = m_name_li, y_names = yp_name_li, message0 = message0, message1 = message1,message2 = message2, message4 = message4, cmds1 = cmds1, vic_count = vic_count)

@app.route("/input_ptbtl", methods=["GET", "POST"])
def input_ptbtl():
    if request.method == "POST":
        cmdselect1 = request.form["cmdselect1"]
    session["cmd1"] = cmdselect1
    return redirect(url_for('pt_battle_turn'))

@app.route("/pt_battle_turn")
def pt_battle_turn():
    cmd1 = session.get("cmd1")
    primitive_m_dc = session.get('primitive_m_dc')
    primitive_y_dc = session.get('primitive_y_dc')
    battle_state = session.get('pt_battle_state')
    vic_count = session.get('vic_count')
    ydc = copy.deepcopy(battle_state['ydc'])
    battle_instance = pt_battle.Pt_battle(primitive_m_dc, primitive_y_dc,vic_count,ydc)
    battle_instance.dc2 = copy.deepcopy(battle_state['dc2'])
    battle_instance.sc = battle_state['sc']
    battle_instance.alive_monsters = list(battle_state['alive_monsters'])
    battle_instance.alive_members = list(battle_state['alive_members'])
    battle_instance.btl_turn = battle_state['btl_turn']
    cmds = {}
    for i in range(len(battle_instance.alive_members)):
        player = battle_instance.alive_members[i]
        cmds[player] = battle_instance.cmd_li(player)
    dc2 = battle_instance.dc2
    session["cmds"] = cmds
    m_names = session.get('mn_li')
    y_names = session.get('ypn_li')
    alive_mem = battle_instance.alive_members
    alive_m = battle_instance.alive_monsters
    session['pt_battle_state'] = {
        'dc2': copy.deepcopy(battle_instance.dc2),
        'ydc': ydc,
        'sc': battle_instance.sc,
        'alive_monsters': list(battle_instance.alive_monsters),
        'alive_members': list(battle_instance.alive_members),
        'btl_turn': battle_instance.btl_turn
    }
    session.modified = True
    if cmd1 == "たたかう":
        return render_template("pt_battle.html",dc2 = dc2, m_names = m_names, y_names = y_names, alive_mem = alive_mem, cmds = cmds, alive_m = alive_m, pri_y_dc = primitive_y_dc, pri_m_dc = primitive_m_dc, vic_count = vic_count)
    elif cmd1 == "にげる":
        session.pop('pt_battle_state', None)
        return redirect(url_for('pt_battle_home'))

@app.route("/input_pt", methods=["GET", "POST"])
def input_pt():
    cmd_dc = {}
    primitive_m_dc = session.get('primitive_m_dc')
    primitive_y_dc = session.get('primitive_y_dc')
    battle_state = session.get('pt_battle_state')
    vic_count = session.get('vic_count')
    ydc = copy.deepcopy(battle_state['ydc'])
    battle_instance = pt_battle.Pt_battle(primitive_m_dc, primitive_y_dc,vic_count,ydc)
    battle_instance.dc2 = copy.deepcopy(battle_state['dc2'])
    battle_instance.ydc = copy.deepcopy(battle_state['ydc'])
    battle_instance.sc = battle_state['sc']
    battle_instance.alive_monsters = list(battle_state['alive_monsters'])
    battle_instance.alive_members = list(battle_state['alive_members'])
    battle_instance.btl_turn = battle_state['btl_turn']
    alive_mem = battle_instance.alive_members
    if request.method == "POST":
        if "勇者" in alive_mem:
            cmd_dc["勇者"] = [request.form["勇者cmd"],request.form["勇者ag"]]
        if "賢者" in alive_mem:
            cmd_dc["賢者"] = [request.form["賢者cmd"],request.form["賢者ag"]]
        if "パラディン" in alive_mem:
            cmd_dc["パラディン"] = [request.form["パラディンcmd"],request.form["パラディンag"]]
        if "バトルマスター" in alive_mem:
            cmd_dc["バトルマスター"] = [request.form["バトルマスターcmd"],request.form["バトルマスターag"]]
        if "スーパースター" in alive_mem:
            cmd_dc["スーパースター"] = [request.form["スーパースターcmd"],request.form["スーパースターag"]]
    result1 = battle_instance.start(cmd_dc)
    session['pt_battle_state'] = {
        'dc2': copy.deepcopy(battle_instance.dc2),
        'ydc': copy.deepcopy(battle_instance.ydc),
        'sc': battle_instance.sc,
        'alive_monsters': list(battle_instance.alive_monsters),
        'alive_members': list(battle_instance.alive_members),
        'btl_turn': battle_instance.btl_turn
    }
    session.modified = True
    if result1["winner"] is None:
        m_names = session.get('mn_li')
        y_names = session.get('ypn_li')
        alive_mem = battle_instance.alive_members
        alive_m = battle_instance.alive_monsters
        dc2 = battle_instance.dc2
        cmds = session.get('cmds')
        result_len = len(result1["result"])
        return render_template("pt_b_show_re.html",dc2 = dc2, m_names = m_names, y_names = y_names, alive_mem = alive_mem, cmds = cmds, alive_m = alive_m, result1 = result1, pri_y_dc = primitive_y_dc, pri_m_dc = primitive_m_dc, result_len = result_len, vic_count = vic_count)
    else:
        winner = result1["winner"]
        # session.pop('battle_state', None)
        message1 = winner + "の勝利"
        if winner == "勇者パーティー":
            vic_count = session.get("vic_count")
            session["vic_count"] = vic_count+1

            session['pt_battle_state'] = {
                'dc2': copy.deepcopy(battle_instance.dc2),
                'ydc': copy.deepcopy(battle_instance.ydc)
            }
        else:
            session.pop('pt_battle_state', None)
            session['vic_count'] = 0
        result_len = len(result1["result"])
        return render_template("pt_result.html", message1 = message1, result1 = result1, result_len = result_len, vic_count = vic_count+1)
        return redirect(url_for('pt_result'))

# @app.route("/pt_result")
# def pt_result():
#     winner = session.get('winner')
#     result1 = session.get('result1')
#     result_len = len(result1["result"])
#     message1 = winner + "の勝利"

#     return render_template("pt_result.html", message1 = message1, result1 = result1, result_len = result_len)
