import decimal
from .PubTypes import News, PrivateAd, TipOfTheDay
import pyodbc


class ConsolePublisher:
    def __init__(self) -> None:
        pass

    @staticmethod
    def initial_message_get() -> str:
        selection_text = ("Hello Dear User. Please, chose one from the next options:"
                          + "\n Enter 1 to publish News; "
                          + "\n Enter 2 to publish Ad; "
                          + "\n Enter 3 to publish Tip; "
                          + "\n Enter q to quit. \n"
                          )
        return selection_text

    @staticmethod
    def publish_news(db_cursor: pyodbc.Cursor = None) -> None:
        text = input("Text: ")
        city = input("City: ")
        news = News.News(text, city)
        if db_cursor:
            news.db_publish(db_cursor)
        else:
            news.publish()

    @staticmethod
    def publish_private_ad(db_cursor: pyodbc.Cursor = None) -> None:
        ad_text = input("Text: ")
        ad_expiration_dt_str = input("Expiration date (YYYY-MM-DD): ")
        try:
            ad = PrivateAd.PrivateAd.from_str(ad_text, ad_expiration_dt_str)
        except ValueError as publish_private_ad_error:
            print("Failed to publish private ad. Please check the date format it should be - YYYY-MM-DD")
            print(publish_private_ad_error)
        else:
            if db_cursor:
                ad.db_publish(db_cursor)
            else:
                ad.publish()

    @staticmethod
    def publish_tip(db_cursor: pyodbc.Cursor = None) -> None:
        text = input("Text: ")
        rating_str = input("Rating: ")
        try:
            tip = TipOfTheDay.TipOfTheDay.from_str(text, rating_str)
        except decimal.InvalidOperation as publish_tip_error:
            print("Failed to publish tip of the day. Please enter correct rating as decimal")
            print(publish_tip_error)
        else:
            if db_cursor:
                tip.db_publish(db_cursor)
            else:
                tip.publish()
