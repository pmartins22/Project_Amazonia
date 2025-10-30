# This file handles all operations related to saving and loading game data.
# It manages a JSON file (`save_data.json`) that stores the state of one or more games.
# Functions are provided to load, save, check for, and list saved games.

import json
import os

from game.game_manager import GameManager

BASE_DIR = os.path.dirname(__file__)
SAVE_FILE = os.path.join(BASE_DIR, "save_data.json")


def _load_saves():
    """
    Loads all save data from the JSON file.

    This is an internal helper function that reads the save file, handles potential
    errors like a missing or corrupted file, and returns the content.

    :return: A list of dictionaries, where each dictionary represents a saved game.
    :rtype: list
    :raises FileNotFoundError: If the save file does not exist.
    :raises ValueError: If the save file is corrupted and cannot be decoded from JSON.
    :raises PermissionError: If the script lacks permissions to read the file.
    :raises IOError: For other I/O errors during file reading.
    """
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
    """
    Saves the current game state to the save file.

    This function serializes the GameManager object into a dictionary and writes it
    to the save file. If a save for the same player already exists, it is overwritten.

    :param game_manager: The main game manager object to be saved.
    :type game_manager: GameManager
    :raises TypeError: If game_manager is not an instance of GameManager.
    :raises PermissionError: If the script lacks permissions to write to the file.
    :raises IOError: For other I/O errors during file writing.
    """
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
    """
    Loads a game state for a specific player from the save file.

    It searches for a save entry matching the given player name and reconstructs
    the GameManager object from the stored data.

    :param player_name: The name of the player whose game should be loaded.
    :type player_name: str
    :return: A GameManager instance populated with the saved state.
    :rtype: GameManager
    :raises ValueError: If player_name is invalid, no save is found, or the save data is corrupted.
    """
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
    """
    Checks if a save exists for a specific player.

    :param player_name: The name of the player to check for.
    :type player_name: str
    :return: True if a save exists for the player, False otherwise.
    :rtype: bool
    :raises ValueError: If player_name is an invalid string.
    """
    if not isinstance(player_name, str) or not player_name.strip():
        raise ValueError("player_name must be a non-empty string")

    try:
        saves = _load_saves()
    except FileNotFoundError:
        return False

    return any(s.get("player", {}).get("name") == player_name for s in saves)


def print_player_list():
    """
    Prints a list of all players who have a saved game.

    This function reads the save file and prints the name of each player found.
    If no saves are found, it prints a corresponding message.
    """
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