"""
{
    "publications": [
        {
            "type": "News" or "Ad" or "Tip", -- mandatory
            "text": "main text", -- mandatory
            "city": "Prague", -- mandatory for News
            "rating": "0,5", -- mandatory for Tip
            "expiration_date": "YYYY-MM-DD" -- mandatory for ad
        },
        {
            "type": "News" or "Ad" or "Tip", -- mandatory
            "text": "main text", -- mandatory
            "city": "Prague", -- mandatory for News
            "rating": "0,5", -- mandatory for Tip
            "expiration_date": "YYYY-MM-DD" -- mandatory for ad
        }
    ]
}
"""
import os
import json
from Lab_4 import normalize_str
import Lab_5 as PubTypes
from datetime import datetime
import decimal

DATE_FORMAT = "%Y-%m-%d"


class PubReader:
    def __init__(self, file_path: str = "new_publish.json") -> None:
        self._file_path = file_path

    def _read_draft(self) -> list:
        draft = []
        if os.path.exists(self._file_path):
            with open(self._file_path, mode='r', encoding='utf8') as file:
                draft = json.loads(file.read())["publications"]
        else:
            print(f"File under path {self._file_path} not found!")
        return draft

    def _delete_draft(self) -> None:
        if os.path.exists(self._file_path):
            os.remove(self._file_path)
        else:
            print(f"File under path {self._file_path} not found!")
        return

    def file_processing(self) -> None:
        draft = self._read_draft()
        if len(draft) > 0:
            for pub in draft:
                pub_reader._publish_draft(pub)
            self._delete_draft()

    @staticmethod
    def _publish_draft(draft: json) -> None:
        #   load text
        pub_text = draft["text"]
        #   normalize text
        normalized_text = normalize_str(pub_text)
        #   load publication type
        pub_type = draft["type"]
        if pub_type == "News":
            PubTypes.News(normalized_text, draft["city"]).publish()
        elif pub_type == "Ad":
            try:
                ad_expiration_dt = datetime.strptime(draft["expiration_date"], DATE_FORMAT)
            except ValueError:
                print("Invalid date.")
                return
            PubTypes.PrivateAd(normalized_text, ad_expiration_dt).publish()
        elif pub_type == "Tip":
            try:
                tip_rating = decimal.Decimal(draft["rating"])
            except decimal.InvalidOperation:
                print("Invalid rating.")
                return
            PubTypes.TipOfTheDay(normalized_text, tip_rating).publish()
    @staticmethod
    def show_formatting() -> None:
        with open("file_format.txt", mode='r', encoding='utf8') as file:
            print(file.read())


if __name__ == "__main__":
    while True:
        user_choice = input(" 0. Show the file formatting rules"
                            + "\n 1. Load file"
                            + "\n 2. Use default file"
                            + "\n 3. Quit"
                            + "\n")
        if user_choice == "0":
            PubReader.show_formatting()
        elif user_choice == "1":
            user_file_path = input("Please, enter the file path: ")
            pub_reader = PubReader(user_file_path)
            pub_reader.file_processing()
        elif user_choice == "2":
            pub_reader = PubReader()
            pub_reader.file_processing()
        elif user_choice == "3":
            break
