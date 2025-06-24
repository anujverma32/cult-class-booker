from datetime import datetime
from utils.enums import Weekday, Class_timing, Class_type
from utils.constants import Constants
from models import Preferences


class Prefrence_matcher:
    """
    Prefrence_matcher matches user preferences against class schedule details.

    Args:
        prefrences (Prefrences): An object containing user preferences for class timing, center, class type, and preferred days.

    Methods:
        match(date_str: str, time_str: str, center_id: int, workout_name: str) -> bool:
            Checks if the given class details match all user preferences.

        __match_for_timing(time_str: str) -> bool:
            Checks if the class time matches the user's preferred timing (morning/evening).

        __match_for_center(center_id: int) -> bool:
            Checks if the class center matches the user's preferred center.

        __match_for_class_type(workout_name: str) -> bool:
            Checks if the class type matches the user's preferred class type.

        __match_for_day(date_str: str) -> bool:
            Checks if the class date falls on a user-preferred day of the week.
    """

    def __init__(self, prefrences: Preferences):
        self.prefrences = prefrences

    def match(
        self, date_str: str, time_str: str, center_id: int, workout_name: str
    ) -> bool:
        return (
            self.__match_for_timing(time_str)
            and self.__match_for_center(center_id)
            and self.__match_for_class_type(workout_name)
            and self.__match_for_day(date_str)
        )

    def __match_for_timing(self, time_str: str) -> bool:
        parsed_time = datetime.strptime(time_str, "%H:%M:%S").time()
        if self.prefrences.timing == Class_timing.MORNING:
            return parsed_time < Constants.noon_time
        elif self.prefrences.timing == Class_timing.EVENING:
            return parsed_time > Constants.noon_time
        else:
            return False

    def __match_for_center(self, center_id: int) -> bool:
        return center_id == self.prefrences.center

    def __match_for_class_type(self, workout_name: str):
        return Class_type[workout_name] == self.prefrences.class_type

    def __match_for_day(self, date_str: str):
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
        return Weekday(parsed_date.weekday()) in self.prefrences.days_of_week
