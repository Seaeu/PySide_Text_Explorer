import os
import json
# GLOBAL VARIABLE
import game_state as state
# Other Files.py
import stats as stat

# --- SAVE FILE MANAGEMENT ---
SAVE_FILE = "savegame.json"
# --- Debug Categories ---
REQUIRED_CATEGORIES = ["options", "inventory", "equipment", "player_stats", "game_stage", "world_status"]
#Default Player Data
def get_preset_data():
    return {
    "options": {
        "text_speed": 5,
    },
    "inventory": {
        "Small Potion": 3
    },
    "equipment": {
        "Head": {"equipped": False,"item": None},
        "Chest": {"equipped": False,"item": None},
        "Legs": {"equipped": False,"item": None},
        "Feet": {"equipped": False,"item": None},
        "Weapon": {"equipped": False,"item": None},
        "Secondary": {"equipped": False,"item": None}
    },
    "player_stats": {
        "ID": "Player",
        "M_HP": 100,
        "C_HP": 100,
        "ATK": 12,
        "ACC": 0.75,
        "CRT": 0.2,
        "BLK": 0.4,
        "SPD": 6,
        "GOLD": 0
    },
    "game_stage": 0,
    "world_status": {
        "zone_0": {
            "world_name":"World Map",
            "nodes": [
                {
                "name":"Tranquil Forest",
                "x": 0,
                "y": 250,
                "radius": 50,
                "callback": "emit_signal",
                "visible": True,
                },{
                "name":"WIP",
                "x": 0,
                "y": 100,
                "radius": 50,
                "callback": None,
                "visible": True,
                }
            ],
            "connections": [
                {
                "source":"Tranquil Forest",
                "dest":"WIP",
                }
            ],
            },
        "zone_1": {
            "world_name":"Tranquil Forest",
            "nodes": [
                {
                "name":"Temp",
                "x": 0,
                "y": -75,
                "radius": None,
                "callback": None,
                "visible": True,
                },{
                "name":"Village",
                "x": 0,
                "y": -50,
                "radius": None,
                "callback": None,
                "visible": True,
                },{
                "name":"Shop",
                "x": -100,
                "y": -50,
                "radius": None,
                "callback": None,
                "visible": True,
                },{
                "name":"Battle",
                "x": 100,
                "y": 50,
                "radius": None,
                "callback": None,
                "visible": True,
                }
            ],
            "connections": [
                {
                "source":"Temp",
                "dest":"Shop"
                },{
                "source":"Temp",
                "dest":"Battle"
                }
            ]
        }
    }
}

def verify_save_integrity():
    try:
        with open(SAVE_FILE, "r") as file:
            debug = json.load(file)
        is_valid = all(category in debug for category in REQUIRED_CATEGORIES)
        if is_valid:
            return debug
        else:
            print("CRITICAL: Save file is corrupted! It is missing required subcategories.")
            return None

    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"CRITICAL: File cannot be parsed or read. Error: {e}")
        return None

def new_game():
    current_options = state.data["options"]
    fresh_presets = get_preset_data()
    fresh_presets["options"] = current_options
    state.data = fresh_presets
    with open(SAVE_FILE, "w") as file:
        json.dump(fresh_presets, file, indent=4)

def save_game():
    try:
        with open(SAVE_FILE, "w") as file:
            json.dump(state.data, file, indent=4)
        print("Game saved successfully!")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game():
    try:
        with open(SAVE_FILE, "r") as file:
            pass
    except FileNotFoundError:
        print("No save file found. Creating a fresh profile...")
        presets = get_preset_data()
        with open(SAVE_FILE, "w") as file:
            json.dump(presets, file, indent=4)

        state.data = presets
        print("Game data loaded successfully from fresh presets!")
        return presets
    loaded_data = verify_save_integrity()
    if loaded_data is None:
        print("\n=============================================")
        print("GAME LAUNCH FAILED: Your save file is broken.")
        print("Please check savegame.json or restore a backup.")
        print("=============================================")
        YESTONEWGAME = input("\n\nWould you like to reset your save file? Type yes to continue.\nInput: ")
        if YESTONEWGAME == "yes":
            new_game()
            print("Reload your game for changes to arrive.")
        return None
    state.data = loaded_data
    stat.player_initialization(state.data)
    print("Successful load! Game_State fulfilled.")
    return loaded_data

