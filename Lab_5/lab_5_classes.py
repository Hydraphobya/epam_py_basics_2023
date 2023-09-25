"""
Create a tool, which will do user generated news feed:

1.User select what data type he wants to add

2.Provide record type required data

3.Record is published on text file in special format

You need to implement:

1.News – text and city as input. Date is calculated during publishing.

2.Privat ad – text and expiration date as input. Day left is calculated during publishing.

3.Your unique one with unique publish rules.
Each new record should be added to the end of file. Commit file in git for review.
"""
from datetime import datetime
import decimal

FILE_NAME = "Lab_5_publications.txt"
DATE_FORMAT = "%Y-%m-%d"


class BasicPublication:
    def __init__(self, def_text: str) -> None:
        self._text = def_text

    @staticmethod
    def _write_to_file(text_to_publish: str) -> None:
        with open(FILE_NAME, mode="a") as file:
            file.write(text_to_publish)


class News(BasicPublication):
    _CONTENT = ("------------------ NEWS------------------"
                + "\n City: {city} "
                + "\n Date: {date} "
                + "\n News: {text}"
                + "\n")

    def __init__(self, def_text: str, def_city: str) -> None:
        super().__init__(def_text)
        self._city = def_city
        self._publish_date = datetime.now()

    def publish(self) -> None:
        self._write_to_file(self._CONTENT.format(
            city=self._city,
            date=self._publish_date.strftime(DATE_FORMAT),
            text=self._text
        )
        )


class PrivateAd(BasicPublication):
    _CONTENT = ("------------------ ADVERTISEMENT------------------"
                + "\n Text: {text} "
                + "\n Expiration date: {date} "
                + "\n Days left: {days_left}"
                + "\n")

    def __init__(self, def_text: str, expiration_date: datetime) -> None:
        super().__init__(def_text)
        self._expiration_date = expiration_date
        self._days_left = 0

    def publish(self) -> None:
        days_left = (self._expiration_date - datetime.now()).days
        if days_left < 0:
            days_left = 0
        self._write_to_file(self._CONTENT.format(
            text=self._text,
            date=self._expiration_date.strftime(DATE_FORMAT),
            days_left=days_left
        )
        )


class TipOfTheDay(BasicPublication):
    _CONTENT = ("------------------ TIP OF THE DAY------------------"
                + "\n Date: {date} "
                + "\n Text: {text} "
                + "\n Rating: {rating} "
                + "\n")

    def __init__(self, def_text: str, def_rating: decimal.Decimal) -> None:
        super().__init__(def_text)
        self._rating = def_rating
        self._publish_date = datetime.now()

    def publish(self) -> None:
        self._write_to_file(self._CONTENT.format(
            date=self._publish_date.strftime(DATE_FORMAT),
            text=self._text,
            rating=self._rating
        )
        )


if __name__ == '__main__':
    selection_text = ("Hello Dear User. Please, chose one from the next options:"
                      + "\n Enter 1 to load News; "
                      + "\n Enter 2 to load Ad; "
                      + "\n Enter 3 to load Tip; "
                      + "\n Enter q to quit. \n"
                      )

    input_text = ""
    while input_text.lower() != "q":
        input_text = input(selection_text)
        if input_text == "1":
            news_text = input("Text: ")
            news_city = input("City: ")
            news = News(news_text, news_city)
            news.publish()
        elif input_text == "2":
            ad_text = input("Text: ")
            ad_expiration_dt_str = input("Expiration date (YYYY-MM-DD): ")
            try:
                ad_expiration_dt = datetime.strptime(ad_expiration_dt_str, DATE_FORMAT)
            except ValueError:
                print("Invalid date.")
                continue
            ad = PrivateAd(ad_text, ad_expiration_dt)
            ad.publish()
        elif input_text == "3":
            tip_text = input("Text: ")
            tip_rating = 0
            try:
                tip_rating = decimal.Decimal(input("Rating: "))
            except decimal.InvalidOperation:
                print("Invalid rating.")
                continue
            tip = TipOfTheDay(tip_text, tip_rating)
            tip.publish()
