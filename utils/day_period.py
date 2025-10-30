# This file defines the DayPeriod enum, which represents the different
# periods of a day in the game (DAWN, MORNING, AFTERNOON, NIGHT).

from enum import Enum, auto


class DayPeriod(Enum):
    """
    Enumeration for the different periods of the day.

    This is used throughout the game to handle time-specific events,
    such as animal spawn rates.
    """
    DAWN = auto()
    MORNING = auto()
    AFTERNOON = auto()
    NIGHT = auto()