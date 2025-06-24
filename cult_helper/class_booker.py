from pprint import pprint
from cult_helper.prefrence_matcher import Prefrence_matcher
from utils.enums import Weekday, Class_timing, Class_type, Class_state
from cult_helper.api_helper import CultApiHelper
from models import Preferences, Users
from scheduler import scheduler


def cult_class_booker_for_all_users():
    with scheduler.app.app_context():
        users = Users.query.all()
        for user in users:
            _book_cult_class_for_user(user)


def _book_cult_class_for_user(user: Users):
    cult_api_helper = CultApiHelper(user)
    print(user)
    for pref in user.preferences:
        print(pref)

    # all_classes = cult_api_helper.get_all_classes()


def _iterate_over_classes(all_classes: dict):
    for class_date in all_classes["classByDateMap"].values():
        curr_date = class_date["id"]
        for class_time in class_date["classByTimeList"]:
            curr_time = class_time["id"]
            for center in class_time["centerWiseClasses"]:
                center_id = center["centerId"]
                for cult_class in center["classes"]:
                    if prefrence_matcher.match(
                        curr_date, curr_time, center_id, cult_class["workoutName"]
                    ):
                        print(
                            curr_date, curr_time, center_id, cult_class["workoutName"]
                        )
                        if cult_class["state"] == Class_state.AVAILABLE.value:
                            cult_api_helper.book_class(cult_class["id"])
                        elif (
                            cult_class["state"] == Class_state.WAITLIST_AVAILABLE.value
                        ):
                            cult_api_helper.waitlist_class(cult_class["id"])
                        elif cult_class["state"] == Class_state.WAITLIST_FULL.value:
                            print(
                                f"Class {cult_class['id']} is waitlist full, skipping..."
                            )
                        elif cult_class["state"] == Class_state.BOOKED.value:
                            print(
                                f"Class {cult_class['id']} is already booked, skipping..."
                            )
                        else:
                            print(
                                f"Class {cult_class['id']} is in an unknown state: {cult_class['state']}, skipping..."
                            )
