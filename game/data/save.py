import json
import os

from game.game_manager import GameManager
from game.player import Player

SAVE_FILE = "save_data.json"

def save_game(game_manager):
    if not os.path.exists(SAVE_FILE):
        raise FileNotFoundError("SAVE_FILE not found.")

    with open(SAVE_FILE, "r") as f:
        saves = json.load(f)

    player_name = game_manager.player.name

    saves = [s for s in saves if s["player"]["name"] != player_name]

    saves.append(game_manager.to_dict())

    with open(SAVE_FILE, "w") as f:
        json.dump(saves, f, indent=4)

def load_game(player_name):
    if not os.path.exists(SAVE_FILE):
        raise FileNotFoundError("SAVE_FILE not found.")

    with open(SAVE_FILE, "r") as f:
        saves = json.load(f)

    for s in saves:
        if s["player"]["name"] == player_name:
            return GameManager.from_dict(s)


    raise ValueError(f"No save found for '{player_name}'")