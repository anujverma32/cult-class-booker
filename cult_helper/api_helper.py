import requests
import json
from models import Users


class CultApiHelper:
    """
    CultApiHelper provides methods to interact with the Cult.fit API for fitness classes.

    Attributes:
        host (str): Base URL for the Cult.fit API.
        params (dict): Default query parameters for API requests.
        headers (dict): Default headers for API requests.

    Methods:
        get_all_classes():
            Fetches all available fitness classes from the Cult API.
            Raises:
                Exception: If the API request fails.

        get_class(class_id):
            Fetches details of a specific class by its ID.
                class_id (int): The ID of the class to fetch.
                dict: JSON response containing class details.
            Raises:
                Exception: If the API request fails.

        book_class(class_id):
            Raises:
                Exception: If the API request fails.

        waitlist_class(class_id):
            Raises:
                Exception: If the API request fails.
    """

    def __init__(self, user: Users):
        self.host = "https://www.cult.fit/api/cult"
        self.params = {"productType": "FITNESS"}
        self.headers = {
            "Accept": "application/json",
            "at": user.cult_token,
            "clientVersion": "11.07",
            "lat": user.latitude,
            "lon": user.longitude,
            "Content-Type": "application/json; charset=utf-8",
            "osName": "ios",
        }

    def get_all_classes(self):
        """
        Fetches all classes from the Cult API.

        Returns:
            dict: JSON response containing class data.
        """
        url = f"{self.host}/classes/v2"
        try:
            response = requests.request(
                "GET", url, headers=self.headers, params=self.params
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise Exception(f"Failed to fetch classes: {err}")

    def get_class(self, class_id):
        url = f"{self.host}/class/v3/{class_id}"
        try:
            response = requests.request(
                "GET", url, headers=self.headers, params=self.params
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise Exception(f"Failed to fetch class {class_id}: {err}")

    def book_class(self, class_id):
        """
        Books a class by its ID.

        Args:
            class_id (int): The ID of the class to book.

        Returns:
            dict: JSON response containing booking confirmation.
        """
        url = f"{self.host}/class/{class_id}/book"
        data = {"productType": "FITNESS"}
        try:
            response = requests.request(
                "POST", url, headers=self.headers, data=json.dumps(data)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise Exception(
                f"Failed to book class {class_id}: {err.response.json().get('message', 'Unknown error')}"
            )

    def waitlist_class(self, class_id):
        """
        Adds a class to the waitlist by its ID.

        Args:
            class_id (int): The ID of the class to waitlist.

        Returns:
            dict: JSON response containing waitlist confirmation.
        """
        url = f"{self.host}/class/{class_id}/waitlist"
        data = {"productType": "FITNESS"}
        try:
            response = requests.request(
                "POST", url, headers=self.headers, data=json.dumps(data)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            raise Exception(
                f"Failed to waitlist class {class_id}: {err.response.json().get('message', 'Unknown error')}"
            )
