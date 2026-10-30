import math
# GLOBAL VARIABLE
import game_state as state

# --- ENTITY STAT STRUCTURE ---
class Entity:
    def __init__(self, name, hp, atk, acc, crt, blk, spd, gold):
        self.ID = name
        self.M_HP = hp
        self.C_HP = hp
        self.ATK = atk
        self.ACC = acc
        self.CRT = crt
        self.BLK = blk
        self.SPD = spd
        self.GOLD = gold

    def dodge(self):
            SPD=max(3, self.SPD)
            Chance=round(1+(math.log10(math.sqrt(SPD)-1+(SPD*0.1)))/2,2)
            print(f"Dodge chance {(round((Chance-1)*100,4))}%") #debug line
            return Chance

    def buff(self, STAT, x: int): # player.buff("SPD", 15) stat up
        current_val = getattr(self, STAT)
        setattr(self, STAT, current_val + x)
        print(f"{self.ID} {STAT} UP {x}") #debug line

    def nerf(self, STAT, x: int): # bear.nerf("ATK",12) stat down
        current_val = getattr(self, STAT)
        setattr(self, STAT, current_val - x)
        print(f"{self.ID} {STAT} DOWN {x}") #debug line

# --- ITEM STAT STRUCTURE ---
class Item:
    def __init__(self,name, hp, atk, acc, crt, blk, spd, gold, type):
        self.ID = name
        self.HP = hp
        self.ATK = atk
        self.ACC = acc
        self.CRT = crt
        self.BLK = blk
        self.SELL = gold
        self.TYPE = type

    def obtain(self, amount):
        if self.ID in p_inv:
            p_inv[self.ID] += amount
        else:
            p_inv[self.ID] = amount
        with open(SAVE_FILE, "w") as file:
            json.dump(save_data, file, indent=4)

    def equip(self,Entity):
            if p_equip[self.TYPE]["equipped"] == False:
                p_equip[self.TYPE]["item"] = self.ID
                p_equip[self.TYPE]["equipped"] = True
                with open(SAVE_FILE, "w") as file:
                    json.dump(save_data, file, indent=4)
                print(f"{Entity.ID} equipped {self.ID}!") #debug line
                Entity.M_HP  = Entity.M_HP  + self.HP
                Entity.ATK = Entity.ATK + self.ATK
                Entity.ACC = Entity.ACC + self.ACC
                Entity.CRT = Entity.CRT + self.CRT
                Entity.BLK = Entity.BLK + self.BLK
            else:
                print("Weapon already equipped!") #debug line

    def unequip(self,Entity):
            if p_equip[self.TYPE]["equipped"] == True:
                p_equip[self.TYPE]["item"] = None
                p_equip[self.TYPE]["equipped"] = False
                with open(SAVE_FILE, "w") as file:
                    json.dump(save_data, file, indent=4)
                print(f"{Entity.ID} unequipped {self.ID}!") #debug line
                Entity.M_HP  = Entity.M_HP  - self.HP
                Entity.ATK = Entity.ATK - self.ATK
                Entity.ACC = Entity.ACC - self.ACC
                Entity.CRT = Entity.CRT - self.CRT
                Entity.BLK = Entity.BLK - self.BLK
            else:
                print("Weapon isn't equipped!") #debug line

    def consume(self,Entity):
        if self.TYPE == "Edible":
            Entity.C_HP = max=(Entity.M_HP,Entity.C_HP + self.HP)
            print(f"{Entity.ID} consumed a {self.ID}!\n") #debug line
            print(f"{Entity.C_HP}/{Entity.M_HP}") #debug line
        else:
            print("Item is not Edible.")

## -- INITIALIZE ALL GAME_STATE VARIABLES -- ##
def player_initialization(data):
    state.stats = data["player_stats"]
    state.options = data["options"]
    state.inventory = data["inventory"]
    state.equipment = data["equipment"]

    p_stats = state.stats
    player = Entity(
        name=p_stats["ID"],
        hp=p_stats["M_HP"],
        atk=p_stats["ATK"],
        acc=p_stats["ACC"],
        crt=p_stats["CRT"],
        blk=p_stats["BLK"],
        spd=p_stats["SPD"],
        gold=p_stats["GOLD"])
    player.C_HP = p_stats["C_HP"] #Ensures player C_HP is based on the file
    state.player = player



# Entity Sheet     ID    HP  ATK ACC  CRT BLK SPD GOLD
wolf =   Entity("Wolf"  ,85 ,15 ,0.45,0.3,0  ,8  ,60  )
bear =   Entity("Bear"  ,110,28 ,0.25,0.1,0  ,4  ,95  )

# Item Sheet           ID           HP ATK ACC  CRT BLK SPD GOLD  TYPE
sword =       Item("Sword"         ,0 ,15 ,0.05,0  ,0.1,0  ,35 ,"Weapon")
breastplate = Item("Breastplate"   ,45,0  ,0   ,0  ,0.2,-1 ,65 ,"Chest")
s_potion =    Item("Small Potion"  ,35,0  ,0   ,0  ,0  ,0  ,25 ,"Edible")

