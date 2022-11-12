from datetime import datetime
import pytz


class TimeZone:
    def __init__(self) -> None:
        self.all_timezones = pytz.all_timezones
        self.timeZoneSelected = 0

    
    def changeTimeZone(self, timezone):    
        self.timeZoneSelected = pytz.timezone(timezone)
        

    def getTime(self):
        if self.timeZoneSelected:
            dt = datetime.now(self.timeZoneSelected)

        else:
            dt = datetime.now()

        return f"{dt.hour}:{dt.minute}:{dt.second}"


