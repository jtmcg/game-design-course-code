swordsmanAttacks = ("slash", "thrust", "feint", "swing", "chop")
archerAttacks = ("single shot", "poison shot", "snap shot", "double shot", "aim")
wizardAttacks = ("fireball", "ice lance", "lightning bolt", "meditate", "cripple")

fighter = {"swordsman" : swordsmanAttacks, "archer" : archerAttacks, "wizard" : wizardAttacks}

swordAttackDictionary = {"slash" : 8, "thrust" : 15, "feint" : 0, "swing" : 10, "chop" : 5}
bowAttackDictionary = {"single shot": 8, "poison shot" : 3, "snap shot" : 6, "double shot" : 15, "aim" : 0}
spellAttackDictionary = {"fireball" : 12, "ice lance" : 8, "lightning bolt" : 8, "meditate" : 0, "cripple" : 2}
                
def PracticeDummy(combo):
    
    validAttacks = True
    if not(isinstance(combo, list)):
        validAttacks = False
        print("Input must be a list!")       
    elif len(combo) > 5:
        print("Combo is too long!")
        validAttacks = False
        return
    else:
        if combo[0] in swordsmanAttacks:
            active = "swordsman"
        elif combo[0] in archerAttacks:
            active = "archer"
        elif combo[0] in wizardAttacks:
            active = "wizard"
        else:
            print("You must use a sword, bow, or spell!!")
            return
        
        for attack in combo:
            if not (attack in fighter[active]):
                print(attack+" is not a valid "+active+" attack!!")
                validAttacks = False
                return
    
    if validAttacks:
        if active == "swordsman":
            damage = SwordDamage(combo)
            print("Your sword combo did "+ str(damage)+" damage!")
        elif active == "archer":
            damage = BowDamage(combo)
            print("Your bow combo did "+ str(damage)+" damage!")
        else:
            damage = SpellDamage(combo)
            print("Your spell combo did "+ str(damage)+" damage!")
    else:
        print("Try a different combo")
        
def SwordDamage(combo):
    damage = 0
    
    for x in range(len(combo)):
        if x != 0:
            if combo[x-1] == "feint":
                damage += swordAttackDictionary[combo[x]]*2
            elif combo[x-1] == "thrust" and combo[x] != "feint":
                damage += swordAttackDictionary[combo[x]]//2
            else:
                damage += swordAttackDictionary[combo[x]]
        else:
            damage += swordAttackDictionary[combo[x]]
    
    return damage

def BowDamage(combo):
    damage = 0
    poisoned = False
    
    for x in range(len(combo)):
        if combo[x] == "poison shot":
            poisoned = True
            
        if x != 0:
            if combo[x-1] == "aim" and combo[x] != "double shot":
                damage += bowAttackDictionary[combo[x]]*2
            elif combo[x-1] == "snap shot" and combo[x] == "double shot":
                aimed = 1
                if x > 1:
                    if combo[x-2] == "aim":
                        aimed = 2
                damage += (bowAttackDictionary[combo[x]]+bowAttackDictionary["snap shot"])*aimed
            elif combo[x-1] == "double shot" and combo[x] == "snap shot":
                damage += bowAttackDictionary[combo[x]]//2
            else:
                damage += bowAttackDictionary[combo[x]]
        else:
            damage += bowAttackDictionary[combo[x]]
            
        if poisoned:
            damage += bowAttackDictionary["poison shot"]
    
    return damage

def SpellDamage(combo):
    damage = 0
    crippled = 0
    
    for x in range(len(combo)):
        if combo[x] == "cripple":
            crippled += 1
            
        if x != 0:
            if combo[x-1] == "meditate":
                damage += spellAttackDictionary[combo[x]]*2
            elif (combo[x-1] == "ice lance" and combo[x] == "lightning bolt") or (combo[x] == "ice lance" and combo[x-1] == "lightning bolt"):
                damage += spellAttackDictionary[combo[x]]+5
            elif combo[x-1] == "ice lance" and combo[x] == "fireball":
                damage += spellAttackDictionary[combo[x]]//2
            else:
                damage += spellAttackDictionary[combo[x]]
        else:
            damage += spellAttackDictionary[combo[x]]
        
        if crippled != 0:
            damage += spellAttackDictionary["cripple"]*crippled
            crippled += 1
    
    if combo == ["meditate", "meditate", "meditate", "meditate", "fireball"]:
        damage = spellAttackDictionary["fireball"]*10
    
    return damage