from utils.day_period import DayPeriod


class GameManager:
    def __init__(self, player, time = 8.0, days_survived = 0):
        self.player = player
        self.time = time
        self.days_survived = days_survived

    def pass_time(self, time):
        self.time += time
        if self.time >= 24.0:
            self.days_survived += int(self.time // 24.0)
            self.time = self.time % 24

    def format_time(self):
        hours = int(self.time)
        minutes = int((self.time - hours) * 60)
        return f"{hours:02d}:{minutes:02d}"






    def get_day_period(self):
        if self.time >= 0 and self.time < 6:
            return DayPeriod.DAWN
        elif self.time >= 6 and self.time < 12:
            return DayPeriod.MORNING
        elif self.time >= 12 and self.time < 18:
            return DayPeriod.AFTERNOON
        elif self.time >= 18 and self.time < 24:
            return DayPeriod.NIGHT