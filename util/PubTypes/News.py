from util.PubTypes import BasicPublication as BasicPub
from datetime import datetime


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


if __name__ == "__main__":
        n = News("Fake news. ", "New Orleans")
        n.publish()
