from util.PubTypes import News, PrivateAd, TipOfTheDay, BasicPublication
import os
import json
import Lab_4
import decimal

JSON_FILE = "c:\\Users\\Hanna_Hlushakova\\Documents\\Cources\\Python\\Files\\new_publish.json"


class JSONPublisher:
    def __init__(self, file_path: str = JSON_FILE) -> None:
        self._file_path = file_path

    def _read_json_file(self) -> list:
        draft = []
        if os.path.exists(self._file_path):
            with open(self._file_path, mode='r', encoding='utf8') as file:
                draft = json.loads(file.read())["publications"]
        else:
            print(f"File under path {self._file_path} not found!")
        return draft

    def _delete_file(self) -> None:
        if os.path.exists(self._file_path):
            os.remove(self._file_path)
        else:
            print(f"File under path {self._file_path} not found!")
        return

    def file_processing(self) -> None:
        draft = self._read_json_file()
        if len(draft) > 0:
            for pub in draft:
                JSONPublisher._publication_processing(pub)
            self._delete_file()

    @staticmethod
    def _publication_processing(draft: json) -> None:
        #   load text
        pub_text = draft["text"]
        #   normalize text
        normalized_text = Lab_4.normalize_str(pub_text)
        #   load publication type
        pub_type = draft["type"]
        if pub_type == "News":
            News.News(normalized_text, draft["city"]).publish()
        elif pub_type == "Ad":
            try:
                PrivateAd.PrivateAd.from_str(normalized_text, draft["expiration_date"]).publish()
            except ValueError as exp_dt_error:
                print("Invalid date.")
                print(exp_dt_error)
                return
        elif pub_type == "Tip":
            try:
                TipOfTheDay.TipOfTheDay.from_str(normalized_text, draft["rating"]).publish()
            except decimal.InvalidOperation as rating_error:
                print("Invalid rating.")
                print(rating_error)
                return

    @staticmethod
    def show_publications() -> str:
        return BasicPublication.BasicPublication.show_publications()
