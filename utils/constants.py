from datetime import datetime
from utils.enums import Class_state


class Constants:

    noon_time = datetime.strptime("12:00:00", "%H:%M:%S").time()

    avaliable_class_states = [
        Class_state.AVAILABLE,
        Class_state.WAITLIST_AVAILABLE,
    ]
