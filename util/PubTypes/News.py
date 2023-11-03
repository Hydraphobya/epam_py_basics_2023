from util.PubTypes import BasicPublication as BasicPub
from datetime import datetime
import pyodbc


class News(BasicPub.BasicPublication):
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
            date=self._publish_date.strftime(BasicPub.DATE_FORMAT),
            text=self._text
            )
        )

    def db_publish(self, db_cursor: pyodbc.Cursor) -> None:
        insert_str = (f"insert into News values('{self._text}', "
                      f"'{self._city}', "
                      f"'{self._publish_date.strftime(BasicPub.DATE_FORMAT)}' )"
                      )
        db_cursor.execute(insert_str)


if __name__ == "__main__":
    News("Fake news. ", "New Orleans")
