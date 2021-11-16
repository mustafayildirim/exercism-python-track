class Clock:
    hour = 0
    minute = 0
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.__adjusttime__()

    def __adjusttime__(self):
        while self.minute < 0:
            self.hour -= 1
            self.minute += 60

        while self.minute > 59:
            self.hour += 1
            self.minute -= 60

        while self.hour < 0:
            self.hour += 24

        while self.hour > 23:
            self.hour -= 24


    def __repr__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        if self.hour == other.hour and self.minute == other.minute:
            return True
        return False

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
