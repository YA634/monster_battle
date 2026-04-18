import random
import copy

li = ["HP", "MP", "ATK", "DEF", "SPD", "MAG", "Lv", "CON"]
li2 = ["勇者","賢者","パラディン","バトルマスター","スーパースター"]

def create_pt():
    primitive_dc = {}
    for j in range(len(li2)):
        dc = {li[i]: random.randint(10, 50) for i in range(len(li)-2)}; dc["Lv"] = divmod((dc["HP"] + dc["MP"] + dc["ATK"] + dc["DEF"] + dc["SPD"] + dc["MAG"]), 10)[0]; dc["CON"] = {"げんき": 1}; dc["BfDbf"] = {"bk": 0, "rk": 0}
        primitive_dc[li2[j]] = dc
    primitive_dc["賢者"]["MP"] = random.randint(15, 50); primitive_dc["賢者"]["Lv"] = (primitive_dc["賢者"]["HP"]+primitive_dc["賢者"]["MP"]+primitive_dc["賢者"]["ATK"]+(primitive_dc["賢者"]["DEF"]//3)+primitive_dc["賢者"]["SPD"]+primitive_dc["賢者"]["MAG"])//10
    primitive_dc["勇者"]["MP"] = random.randint(12, 50); primitive_dc["勇者"]["Lv"] = (primitive_dc["勇者"]["HP"]+primitive_dc["勇者"]["MP"]+primitive_dc["勇者"]["ATK"]+(primitive_dc["勇者"]["DEF"]//3)+primitive_dc["勇者"]["SPD"]+primitive_dc["勇者"]["MAG"])//10
    return primitive_dc