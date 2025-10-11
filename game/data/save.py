import json
import os

from game.game_manager import GameManager
from game.player import Player

BASE_DIR = os.path.dirname(__file__)
SAVE_FILE = os.path.join(BASE_DIR, "save_data.json")

def save_game(game_manager):
    if not os.path.exists(SAVE_FILE):
        raise FileNotFoundError("SAVE_FILE not found.")

    with open(SAVE_FILE, "r") as f:
        content = f.read().strip()
        if content:
            try:
                saves = json.loads(content)
            except json.JSONDecodeError:
                raise ValueError("JSON file is corrupt.")

        else:
            saves = []

    player_name = game_manager.player.name

    saves = [s for s in saves if s["player"]["name"] != player_name]

    saves.append(game_manager.to_dict())

    with open(SAVE_FILE, "w") as f:
        json.dump(saves, f, indent=4)

def load_game(player_name):
    if not os.path.exists(SAVE_FILE):
        raise FileNotFoundError("SAVE_FILE not found.")

    with open(SAVE_FILE, "r") as f:
        content = f.read().strip()
        if content:
            try:
                saves = json.loads(content)
            except json.JSONDecodeError:
                raise ValueError("JSON file is corrupt.")

        else:
            saves = []

    for s in saves:
        if s["player"]["name"] == player_name:
            return GameManager.from_dict(s)


    raise ValueError(f"No save found for '{player_name}'")

def has_save(player_name):
    if not os.path.exists(SAVE_FILE):
        raise FileNotFoundError("SAVE_FILE not found.")

    with open(SAVE_FILE, "r") as f:
        content = f.read().strip()
        if content:
            try:
                saves = json.loads(content)
            except json.JSONDecodeError:
                raise ValueError("JSON file is corrupt.")

        else: saves = []

    for s in saves:
        if s["player"]["name"] == player_name:
            return True

    return False

def print_player_list():
    if not os.path.exists(SAVE_FILE):
        raise FileNotFoundError("SAVE_FILE not found.")

    with open(SAVE_FILE, "r") as f:
        content = f.read().strip()
        if content:
            try:
                saves = json.loads(content)
            except json.JSONDecodeError:
                raise ValueError("JSON file is corrupt.")

        else:
            saves = []

    if len(saves) == 0:
        print("No saves found...")
        return
    for s in saves:
        print(s["player"]["name"])