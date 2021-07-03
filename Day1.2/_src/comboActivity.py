'''
Who Can Make the Biggest Combo? - Logic

author: J. Tyler McGoffin
'''
sword_attack_default_values = {"slash" : 8, "thrust" : 15, "feint" : 0, "swing" : 10, "chop" : 5}
bow_attack_default_values = {"single shot": 8, "poison shot" : 3, "snap shot" : 6, "double shot" : 15, "aim" : 0}
spell_attack_default_values = {"fireball" : 12, "ice lance" : 8, "lightning bolt" : 8, "meditate" : 0, "cripple" : 2}


class ComboActivity:

    def __init__(self, sword_attack_values = sword_attack_default_values, bow_attack_values = bow_attack_default_values, spell_attack_values = spell_attack_default_values):
        self.sword_attack_dictionary = sword_attack_values
        self.bow_attack_dictionary = bow_attack_values
        self.spell_attack_dictionary = spell_attack_values

        self.swordsman_attacks = list(self.sword_attack_dictionary.keys())
        self.archer_attacks = list(self.bow_attack_dictionary.keys())
        self.wizard_attacks = list(self.spell_attack_dictionary.keys())

        self.fighter = {"swordsman" : self.swordsman_attacks, "archer" : self.archer_attacks, "wizard" : self.wizard_attacks}
                    
    def practice_dummy(self, combo):
        
        validAttacks = True
        if not(isinstance(combo, list)):
            validAttacks = False
            print("Input must be a list!")       
        elif len(combo) > 5:
            print("Combo is too long!")
            validAttacks = False
            return
        else:
            if combo[0] in self.swordsman_attacks:
                active = "swordsman"
            elif combo[0] in self.archer_attacks:
                active = "archer"
            elif combo[0] in self.wizard_attacks:
                active = "wizard"
            else:
                print("You must use a sword, bow, or spell!!")
                return
            
            for attack in combo:
                if not (attack in self.fighter[active]):
                    print(attack+" is not a valid "+active+" attack!!")
                    validAttacks = False
                    return
        
        if validAttacks:
            if active == "swordsman":
                damage = self.sword_damage(combo)
                print("Your sword combo did "+ str(damage)+" damage!")
            elif active == "archer":
                damage = self.bow_damage(combo)
                print("Your bow combo did "+ str(damage)+" damage!")
            else:
                damage = self.spell_damage(combo)
                print("Your spell combo did "+ str(damage)+" damage!")
        else:
            print("Try a different combo")
            
    def sword_damage(self, combo):
        damage = 0
        
        for x in range(len(combo)):
            if x != 0:
                if combo[x-1] == "feint":
                    damage += self.sword_attack_dictionary[combo[x]]*2
                elif combo[x-1] == "thrust" and combo[x] != "feint":
                    damage += self.sword_attack_dictionary[combo[x]]//2
                else:
                    damage += self.sword_attack_dictionary[combo[x]]
            else:
                damage += self.sword_attack_dictionary[combo[x]]
        
        return damage

    def bow_damage(self, combo):
        damage = 0
        poisoned = False
        
        for x in range(len(combo)):
            if combo[x] == "poison shot":
                poisoned = True
                
            if x != 0:
                if combo[x-1] == "aim" and combo[x] != "double shot":
                    damage += self.bow_attack_dictionary[combo[x]]*2
                elif combo[x-1] == "snap shot" and combo[x] == "double shot":
                    aimed = 1
                    if x > 1:
                        if combo[x-2] == "aim":
                            aimed = 2
                    damage += (self.bow_attack_dictionary[combo[x]]+self.bow_attack_dictionary["snap shot"])*aimed
                elif combo[x-1] == "double shot" and combo[x] == "snap shot":
                    damage += self.bow_attack_dictionary[combo[x]]//2
                else:
                    damage += self.bow_attack_dictionary[combo[x]]
            else:
                damage += self.bow_attack_dictionary[combo[x]]
                
            if poisoned:
                damage += self.bow_attack_dictionary["poison shot"]
        
        return damage

    def spell_damage(self, combo):
        damage = 0
        crippled = 0
        
        for x in range(len(combo)):
            if combo[x] == "cripple":
                crippled += 1
                
            if x != 0:
                if combo[x-1] == "meditate":
                    damage += self.spell_attack_dictionary[combo[x]]*2
                elif (combo[x-1] == "ice lance" and combo[x] == "lightning bolt") or (combo[x] == "ice lance" and combo[x-1] == "lightning bolt"):
                    damage += self.spell_attack_dictionary[combo[x]]+5
                elif combo[x-1] == "ice lance" and combo[x] == "fireball":
                    damage += self.spell_attack_dictionary[combo[x]]//2
                else:
                    damage += self.spell_attack_dictionary[combo[x]]
            else:
                damage += self.spell_attack_dictionary[combo[x]]
            
            if crippled != 0:
                damage += self.spell_attack_dictionary["cripple"]*crippled
                crippled += 1
        
        if combo == ["meditate", "meditate", "meditate", "meditate", "fireball"]:
            damage = self.spell_attack_dictionary["fireball"]*10
        
        return damage