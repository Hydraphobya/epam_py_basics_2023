import pyodbc

import util.DBConnection as DBConnection
import util


if __name__ == "__main__":
    db = DBConnection.DBConnection()
    cursor = db.get_cursor()
    cursor.execute('create table if not exists  News (news_text text, news_city text, news_date date)')
    cursor.execute('create table if not exists Advertisement(ad_text text, ad_expiration_date date)')
    cursor.execute('create table if not exists TipOfTheDay (tip_text text, tip_rating real, tip_date date)')

    pub_pub = util.ConsolePublisher.ConsolePublisher()
    input_text = ""
    while input_text.lower() != "q":
        input_text = input(pub_pub.initial_message_get())
        if input_text == "1":
            pub_pub.publish_news(cursor)
            cursor.execute('select * from News')
            news = cursor.fetchall()
            print(news)
        elif input_text == "2":
            pub_pub.publish_private_ad(cursor)
            cursor.execute('select * from Advertisement')
            ad = cursor.fetchall()
            print(ad)
        elif input_text == "3":
            pub_pub.publish_tip(cursor)
            cursor.execute('select * from TipOfTheDay')
            tip = cursor.fetchall()
            print(tip)


