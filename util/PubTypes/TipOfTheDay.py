from util.PubTypes import BasicPublication as BasicPub
from datetime import datetime
import decimal
from typing import TypeVar, Type

T = TypeVar('T', bound='TipOfTheDay')


class TipOfTheDay(BasicPub.BasicPublication):
    _CONTENT = ("------------------ TIP OF THE DAY------------------"
                + "\n Date: {date} "
                + "\n Text: {text} "
                + "\n Rating: {rating} "
                + "\n")

    def __init__(self, def_text: str, def_rating: decimal.Decimal) -> None:
        super().__init__(def_text)
        self._rating = def_rating
        self._publish_date = datetime.now()

    @classmethod
    def from_str(cls: Type[T], text: str, rating_str: str) -> T:
        try:
            rating = decimal.Decimal(rating_str)
        except decimal.InvalidOperation as rating_error:
            print("Invalid rating.")
            print(rating_error)
            raise rating_error
        else:
            return TipOfTheDay(text, rating)

    def publish(self) -> None:
        self._write_to_file(self._CONTENT.format(
            date=self._publish_date.strftime(BasicPub.DATE_FORMAT),
            text=self._text,
            rating=self._rating
            )
        )
