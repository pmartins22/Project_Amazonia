import json
import os

from game.game_manager import GameManager

BASE_DIR = os.path.dirname(__file__)
SAVE_FILE = os.path.join(BASE_DIR, "save_data.json")


def _load_saves():
    if not os.path.exists(SAVE_FILE):
        raise FileNotFoundError(f"Save file not found at: {SAVE_FILE}")

    try:
        with open(SAVE_FILE, "r") as f:
            content = f.read().strip()
            return json.loads(content) if content else []
    except json.JSONDecodeError as e:
        raise ValueError(f"Save file is corrupted: {str(e)}")
    except PermissionError:
        raise PermissionError(f"No permission to read save file: {SAVE_FILE}")
    except IOError as e:
        raise IOError(f"Error reading save file: {str(e)}")


def save_game(game_manager):
    if not isinstance(game_manager, GameManager):
        raise TypeError("game_manager must be an instance of GameManager")

    try:
        saves = _load_saves()
    except FileNotFoundError:
        saves = []

    player_name = game_manager.player.name
    saves = [s for s in saves if s.get("player", {}).get("name") != player_name]
    saves.append(game_manager.to_dict())

    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(saves, f, indent=4)
    except PermissionError:
        raise PermissionError(f"No permission to write to save file: {SAVE_FILE}")
    except IOError as e:
        raise IOError(f"Error writing to save file: {str(e)}")


def load_game(player_name):
    if not isinstance(player_name, str) or not player_name.strip():
        raise ValueError("player_name must be a non-empty string")

    saves = _load_saves()

    for s in saves:
        if s.get("player", {}).get("name") == player_name:
            try:
                return GameManager.from_dict(s)
            except (KeyError, ValueError, TypeError) as e:
                raise ValueError(f"Corrupted save data for '{player_name}': {str(e)}")

    raise ValueError(f"No save found for '{player_name}'")


def has_save(player_name):
    if not isinstance(player_name, str) or not player_name.strip():
        raise ValueError("player_name must be a non-empty string")

    try:
        saves = _load_saves()
    except FileNotFoundError:
        return False

    return any(s.get("player", {}).get("name") == player_name for s in saves)


def print_player_list():
    try:
        saves = _load_saves()
    except FileNotFoundError:
        print("No saves found...")
        return

    if not saves:
        print("No saves found...")
        return

    for s in saves:
        player_name = s.get("player", {}).get("name", "Unknown")
        print(player_name)