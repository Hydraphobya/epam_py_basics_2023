from util.PubTypes import BasicPublication as BasicPub
from datetime import datetime
from typing import TypeVar, Type
import pyodbc


T = TypeVar('T', bound='PrivateAd')


class PrivateAd(BasicPub.BasicPublication):
    _CONTENT = ("------------------ ADVERTISEMENT------------------"
                + "\n Text: {text} "
                + "\n Expiration date: {date} "
                + "\n Days left: {days_left}"
                + "\n")

    def __init__(self, def_text: str, expiration_date: datetime = None) -> None:
        super().__init__(def_text)
        self._expiration_date = expiration_date
        self._days_left = 0

    @classmethod
    def from_str(cls: Type[T], text: str, expiration_dt_str: str) -> T:
        try:
            expiration_dt = datetime.strptime(expiration_dt_str, BasicPub.DATE_FORMAT)
        except ValueError as exp_dt_error:
            print("Invalid date.")
            print(exp_dt_error)
            raise exp_dt_error
        else:
            return PrivateAd(text, expiration_dt)

    def publish(self) -> None:
        days_left = (self._expiration_date - datetime.now()).days
        if days_left < 0:
            days_left = 0
        self._write_to_file(self._CONTENT.format(
            text=self._text,
            date=self._expiration_date.strftime(BasicPub.DATE_FORMAT),
            days_left=days_left
            )
        )

    def db_publish(self, db_cursor: pyodbc.Cursor) -> None:
        insert_str = f"insert into Advertisement values('{self._text}', '{self._expiration_date}')"
        db_cursor.execute(insert_str)
